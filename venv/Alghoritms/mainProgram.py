import time
from imutils.video import VideoStream
import serial
import numpy as np
import cv2

def translate(value, oldMin, oldMax, newMin=-100, newMax=100):
    oldRange = oldMax - oldMin
    newRange = newMax - newMin
    NewValue = (((value - oldMin) * newRange) / oldRange) + newMin
    return int(NewValue)

usesPiCamera = False

cameraResolution = (640, 480)
vs = VideoStream(usePiCamera=usesPiCamera, resolution=cameraResolution, framerate=60).start()
time.sleep(2.0)

colorLower = (0, 100, 50)
colorUpper = (100, 255, 255)
colorTolerance = 3
paused = False
roiSize = (16, 16)  # roi size on the scaled down image (converted to HSV)

while True:
    loopStart = time.time()
    if not paused:
        frame = vs.read()

        height, width = frame.shape[0:2]
        scaleFactor = 4
        newWidth, newHeight = width // scaleFactor, height // scaleFactor

        resizedColor = cv2.resize(frame, (newWidth, newHeight), interpolation=cv2.INTER_CUBIC)
        resizedColor_blurred = cv2.GaussianBlur(resizedColor, (5, 5), 0)

        resizedHSV = cv2.cvtColor(resizedColor_blurred, cv2.COLOR_BGR2HSV)

        roi = resizedHSV[newHeight // 2 - roiSize[0] // 2: newHeight // 2 + roiSize[0] // 2,
              newWidth // 2 - roiSize[1] // 2: newWidth // 2 + roiSize[1] // 2, :]

        colorLowerWithTolerance = (colorLower[0] - colorTolerance,) + colorLower[1:]
        colorUpperWithTolerance = (colorUpper[0] + colorTolerance,) + colorUpper[1:]

        mask = cv2.inRange(resizedHSV, colorLowerWithTolerance, colorUpperWithTolerance)
        cv2.erode(mask, None, iterations=5)
        cv2.dilate(mask, None, iterations=5)

        (contours, hierarchy) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        boundingBoxes = []
        biggestObject_BoundingBox = None
        biggestObjectMiddle = None
        if contours:
            largestContour = max(contours, key=cv2.contourArea)
            biggestObject_BoundingBox = cv2.boundingRect(largestContour)

            for i, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if area > ((newWidth * newHeight) / 256):
                    x, y, w, h = cv2.boundingRect(contour)
                    boundingBoxes.append((x, y, w, h))
        else:
            pass

        upscaledColor = cv2.resize(resizedColor, (width, height), interpolation=cv2.INTER_NEAREST)

        for boundingBox in boundingBoxes:
            x, y, w, h = boundingBox
            cv2.rectangle(resizedColor, (x, y), (x + w, y + h), (255, 255, 0), thickness=1)
            cv2.rectangle(upscaledColor, (x * scaleFactor, y * scaleFactor),
                          ((x + w) * scaleFactor, (y + h) * scaleFactor), (255, 255, 0), thickness=2)

        if biggestObject_BoundingBox:
            x, y, w, h = biggestObject_BoundingBox
            biggestObjectMiddle = ((x + w // 2) * scaleFactor, (y + h // 2) * scaleFactor)
            cv2.rectangle(resizedColor, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
            cv2.rectangle(upscaledColor, (x * scaleFactor, y * scaleFactor),
                          ((x + w) * scaleFactor, (y + h) * scaleFactor), (0, 0, 255), thickness=3)
            cv2.circle(upscaledColor, biggestObjectMiddle, 2, (255, 0, 0), thickness=2)
            screenMiddle = width // 2, height // 2
            cv2.line(upscaledColor, screenMiddle, biggestObjectMiddle, (0, 0, 255))   # to rysuje ta linie

        cv2.imshow("video", upscaledColor)
        # cv2.imshow("roi", roi)
        cv2.imshow("mask", mask)

        modTolerances = False


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('w'):
        colorTolerance = min(colorTolerance + 1, 50)
        print("New color range: {}".format(colorTolerance))
    elif key == ord('s'):
        colorTolerance = max(colorTolerance - 1, 0)
        print("New color range: {}".format(colorTolerance))
    elif key == ord('p'):
        paused = not paused

    loopEnd = time.time()
    print("loop execution took {:3.2f}ms".format((loopEnd - loopStart) * 1000))

cv2.destroyAllWindows()
vs.stop()