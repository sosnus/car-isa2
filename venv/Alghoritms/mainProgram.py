import time
from imutils.video import VideoStream
import serial
import numpy as np
import cv2
import alg
import myserial

myserial.send(sName=myserial.myservo['cam_H'], sVal=90)
myserial.send(sName=myserial.myservo['cam_V'], sVal=90)
myserial.send(sName=myserial.myservo['motor_R'], sVal=90)
myserial.send(sName=myserial.myservo['motor_L'], sVal=90)

time.sleep(1)


def changeData(biggestObjectMiddle):
    placeX = biggestObjectMiddle[0]
    placeY = biggestObjectMiddle[1]
    x = ((placeX - 320) / 320)
    y = ((placeY - 240) / 240) * (-1)

    alg.a_ball_x = biggestObjectMiddle[0]
    alg.a_ball_y = biggestObjectMiddle[1]
    #alg.a_ball_w =
    alg.alg()
    myserial.setMotors(left=alg.motor_temp_l, right=alg.motor_temp_r)
#   myserial.send(sName = myserial.myservo['cam_V'], sVal = alg.temp_servo_val)
#    myserial.receive()
    # print(int(x))


#    x = (x/2)+50

#    time.sleep(0.2)


def translate(value, oldMin, oldMax, newMin=-100, newMax=100):
    oldRange = oldMax - oldMin
    newRange = newMax - newMin
    NewValue = (((value - oldMin) * newRange) / oldRange) + newMin
    return int(NewValue)


usesPiCamera = False

cameraResolution = (640, 480)
vs = VideoStream(usePiCamera=usesPiCamera, resolution=cameraResolution, framerate=60).start()
time.sleep(2.0)

colorLower = (138, 162, 139) # 138 162 139
colorUpper = (200, 255, 255)

redLowerTolerance = 0
greenLowerTolerance = 0
blueLowerTolerance = 0
redUpperTolerance = 0
greenUpperTolerance = 0
blueUpperTolerance = 0
paused = False
roiSize = (16, 16)  # roi size on the scaled down image (converted to HSV)

# Wielkość obrazu stanowi prostokąt o wymiarach 640 x 480 px
# 1/4 obrazu to prostokąt o wymiarach 160 x 120
NumbersIterationForAchieveStatistics = 20
historicBallObject = []
compareScaleFactor = 0.1

while True:
    loopStart = time.time()
    if not paused:
        frame = vs.read()
        frame = cv2.flip(frame, 0)
        # np.fliplr(frame)
        # Pobiera szerokość i wysokość obrazu
        height, width = frame.shape[0:2]
        scaleFactor = 4
        # Dzieli obraz na 4 równe obszary
        newWidth, newHeight = width // scaleFactor, height // scaleFactor

        resizedColor = cv2.resize(frame, (newWidth, newHeight), interpolation=cv2.INTER_CUBIC)
        resizedColor_blurred = cv2.GaussianBlur(resizedColor, (5, 5), 0)

        resizedHSV = cv2.cvtColor(resizedColor_blurred, cv2.COLOR_BGR2HSV)

        roi = resizedHSV[newHeight // 2 - roiSize[0] // 2: newHeight // 2 + roiSize[0] // 2,
              newWidth // 2 - roiSize[1] // 2: newWidth // 2 + roiSize[1] // 2, :]
        # Ustawia klorystyczne ramy poszukiwanego obiektu
        colorLowerWithTolerance = ((colorLower[0] + redLowerTolerance), (colorLower[1] + greenLowerTolerance), (colorLower[2] + blueLowerTolerance))
        colorUpperWithTolerance = ((colorUpper[0] + redUpperTolerance), (colorUpper[1] + greenUpperTolerance),(colorUpper[2] + blueUpperTolerance))
        ###print("colorLowerWithTolerance= RGB", colorLowerWithTolerance,"colorUpperWithTolerance= RGB", colorUpperWithTolerance)
        mask = cv2.inRange(resizedHSV, colorLowerWithTolerance, colorUpperWithTolerance)
        cv2.erode(mask, None, iterations=5)
        cv2.dilate(mask, None, iterations=5)

        # Pobiera kontury wszystkich znalezionych obiektów
        (contours, hierarchy) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        boundingBoxes = []
        biggestObject_BoundingBox = None
        biggestObjectMiddle = None
        probablyObjectIsBall = None
        # Rozpoczynamy filtrowanie wszystkich znalezionych obiektów w celu wyodrębnienia piłki
        if contours:
            # Wybieramy największy znaleziony obiekt
            largestContour = max(contours, key=cv2.contourArea)
            if len(historicBallObject) == NumbersIterationForAchieveStatistics:
                historicBallObject.clear()
            if len(historicBallObject) == 0:
                biggestObject_BoundingBox = cv2.boundingRect(largestContour)
                historicBallObject.append(biggestObject_BoundingBox)
            else:
                lastIndexTableHistoricBallObject = len(historicBallObject) -1
                # Filtrujemy obiekty szukając obiektu którego średnica w 10% przypomina średnicę poprzednio znalezionej piłki (% zależne od compareScaleFactor)
                lastObserverBall = historicBallObject[lastIndexTableHistoricBallObject]
                probablyNextBall = cv2.boundingRect(largestContour)
                diameterLastObserverBall = (lastObserverBall[2] * lastObserverBall[3])
                diameterProbablyBall = probablyNextBall[2] * probablyNextBall[3]
                print(diameterProbablyBall)
                condition1 = diameterLastObserverBall * (1 + compareScaleFactor)
                condition2 = diameterLastObserverBall * (1 - compareScaleFactor)
                if diameterProbablyBall < condition1 or diameterLastObserverBall > condition2:
                    biggestObject_BoundingBox = cv2.boundingRect(largestContour)
                    historicBallObject.append(biggestObject_BoundingBox)
            # Wybieramy ze zbioru znalezionych obiektów tylko te których powierzchnia obiektu jest większa niż 75 px
            for i, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                # Jeżeli powierzchnia obiektu jest większa niż 75 px
                if area > ((newWidth * newHeight) / 256):
                    x, y, w, h = cv2.boundingRect(contour)
                    boundingBoxes.append((x, y, w, h))
        else:
            pass

        upscaledColor = cv2.resize(resizedColor, (width, height), interpolation=cv2.INTER_NEAREST)
        # Wyświetlanie pobocznie obserwowanych obiektów
        for boundingBox in boundingBoxes:
            x, y, w, h = boundingBox
            ##           myserial.ballWidth = w
            alg.a_ball_w = w
            cv2.rectangle(resizedColor, (x, y), (x + w, y + h), (255, 255, 0), thickness=1)
            cv2.rectangle(upscaledColor, (x * scaleFactor, y * scaleFactor),
                          ((x + w) * scaleFactor, (y + h) * scaleFactor), (255, 255, 0), thickness=2)
        # Pooniższy kod odpowiada za wyświetlanie kolorowych rzeczy na ekranie
        if biggestObject_BoundingBox:
            x, y, w, h = biggestObject_BoundingBox
            biggestObjectMiddle = ((x + w // 2) * scaleFactor, (y + h // 2) * scaleFactor)
            cv2.rectangle(resizedColor, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
            cv2.rectangle(upscaledColor, (x * scaleFactor, y * scaleFactor),
                          ((x + w) * scaleFactor, (y + h) * scaleFactor), (0, 0, 255), thickness=3)
            cv2.circle(upscaledColor, biggestObjectMiddle, 2, (255, 0, 0), thickness=2)
            screenMiddle = width // 2, height // 2
            cv2.line(upscaledColor, screenMiddle, biggestObjectMiddle, (0, 0, 255))  # to rysuje ta linie

            # print(biggestObjectMiddle)
            if type(biggestObjectMiddle) != 'NoneType':
              changeData(biggestObjectMiddle)
              print("Found object")
            else:
                print("No object")
        np.fliplr(upscaledColor)
        cv2.imshow("video", upscaledColor)
        # cv2.imshow("roi", roi)
        cv2.imshow("mask", mask)

        modTolerances = False

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('w'):
        if (colorLower[0] + redLowerTolerance) < 255:
            redLowerTolerance = redLowerTolerance +1
    elif key == ord('s'):
        if (colorLower[0] + redLowerTolerance)  > 0:
            redLowerTolerance = redLowerTolerance-1
    elif key == ord('e'):
        if (colorLower[1] + greenLowerTolerance) < 255:
                greenLowerTolerance = greenLowerTolerance + 1
    elif key == ord('d'):
        if (colorLower[1] + greenLowerTolerance) > 0:
                greenLowerTolerance = greenLowerTolerance - 1
    elif key == ord('r'):
        if (colorLower[2] + blueLowerTolerance) < 255:
                blueLowerTolerance = blueLowerTolerance + 1
    elif key == ord('f'):
        if (colorLower[2] + blueLowerTolerance) > 0:
                blueLowerTolerance = blueLowerTolerance - 1
    elif key == ord('y'):
        if (colorUpper[0] + redUpperTolerance) < 255:
            redUpperTolerance = redUpperTolerance +1
    elif key == ord('h'):
        if (colorUpper[0] + redUpperTolerance) > 0:
            redUpperTolerance = redUpperTolerance -1
    elif key == ord('u'):
        if (colorUpper[1] + greenUpperTolerance) < 255:
                greenUpperTolerance = greenUpperTolerance + 1
    elif key == ord('j'):
        if (colorUpper[1] + greenUpperTolerance) > 0:
                greenUpperTolerance = greenUpperTolerance - 1
    elif key == ord('i'):
        if (colorUpper[2] + blueUpperTolerance) < 255:
                blueUpperTolerance = blueUpperTolerance + 1
    elif key == ord('k'):
        if (colorUpper[2] + blueUpperTolerance) > 0:
                blueUpperTolerance = blueUpperTolerance - 1
    elif key == ord('p'):
        paused = not paused

    loopEnd = time.time()
    ###print("loop execution took {:3.2f}ms".format((loopEnd - loopStart) * 1000))

cv2.destroyAllWindows()
vs.stop()
