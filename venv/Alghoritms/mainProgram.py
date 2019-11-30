print("isa-car2")
print("version 0.1")

import cv2
import filtration
import numpy as np

cap = cv2.VideoCapture(0)
# cap.open("rtsp://USER:PASS@IP:PORT/Streaming/Channels/2")
filtration = filtration.Filtration()

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Salida', gray)
    #
    #
    # image =frame
    # b = image.copy()
    #  # set green and red channels to 0
    # b[:, :, 1] = 0
    # b[:, :, 2] = 0
    #
    # g = image.copy()
    # # set blue and red channels to 0
    # g[:, :, 0] = 0
    # g[:, :, 2] = 0
    # r = image.copy()
    # # set blue and green channels to 0
    # r[:, :, 0] = 0
    # r[:, :, 1] = 0
    #
    #  # RGB - Blue
    # cv2.imshow('B-RGB', b)
    #
    #  # RGB - Green
    # cv2.imshow('G-RGB', g)
    #
    #  # RGB - Red
    # cv2.imshow('R-RGB', r)
    list_of_contours = [
        [
            [3, 4], [41, 120], [0, 5], [0, 2], [0, 1], [2, 3], [2, 1], [5, 2], [5, 1]
        ],
        [
            [3, 4], [56, 89], [0, 5], [0, 2], [0, 1], [2, 3], [2, 1], [5, 2], [5, 1]
        ]
    ]
    ##  cv2.waitKey(0)
    filtration.set_params(list_of_contours, gray)
    filtration.filtrating()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
