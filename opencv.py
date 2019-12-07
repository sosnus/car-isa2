print("isa-car2")
print("version 0.1")

import numpy as np
import cv2

def nothing(x):
    #any operation
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("TrackBars")
cv2.createTrackbar("L-H", "TrackBars", 43, 180, nothing)
cv2.createTrackbar("L-S", "TrackBars", 35, 255, nothing)
cv2.createTrackbar("L-V", "TrackBars", 74, 255, nothing)
cv2.createTrackbar("U-H", "TrackBars", 109, 180, nothing)
cv2.createTrackbar("U-S", "TrackBars", 255, 255, nothing)
cv2.createTrackbar("U-V", "TrackBars", 247, 255, nothing)
cv2.createTrackbar("len", "TrackBars", 8, 15, nothing)

font = cv2.FONT_HERSHEY_COMPLEX

while (True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H", "TrackBars")
    l_s = cv2.getTrackbarPos("L-S", "TrackBars")
    l_v = cv2.getTrackbarPos("L-V", "TrackBars")
    u_h = cv2.getTrackbarPos("U-H", "TrackBars")
    u_s = cv2.getTrackbarPos("U-S", "TrackBars")
    u_v = cv2.getTrackbarPos("U-V", "TrackBars")
    moje = cv2.getTrackbarPos("len", "TrackBars")

    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    edge = cv2.Canny(mask, 25, 75)

    # # # # # circles = cv2.HoughCircles(edge, cv2.HOUGH_GRADIENT, 50, 150, param1=1000, param2=500, minRadius=30, maxRadius=150)

    # # # # # if circles is not None:
    # # # # #     circles = np.uint16(np.around(circles))
    # # # # #     for i in circles[0, :]:

    # # # # #         center = (i[0], i[1])
    # # # # #         # circle center
    # # # # #         cv2.circle(edge, center, 1, (0, 100, 100), 3)
    # # # # #         # circle outline
    # # # # #         radius = i[2]
    # # # # #         cv2.circle(edge, center, radius, (255, 0, 255), 3)
    
    # #Kontury
    #
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    
        if area > 100:
            cv2.drawContours(frame, [cnt], 0, (0, 0, 0), 2)
            if len(approx) == moje:
                cv2.putText(frame, "Rectangle", (10, 10), font, 1, (0, 0, 0))

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Kernel', kernel)
    cv2.imshow('Canny Edge', edge)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()