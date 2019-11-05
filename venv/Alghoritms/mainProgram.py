print("isa-car2")
print("version 0.1")

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# cap.open("rtsp://USER:PASS@IP:PORT/Streaming/Channels/2")

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 50, 150, param1=50, param2=51, minRadius=0, maxRadius=200)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(gray, (i[0], i[1]), i[2], (0, 255, 0), 2)

    cv2.imshow('detected circles', gray)
    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
