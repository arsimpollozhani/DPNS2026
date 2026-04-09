import numpy as np
import cv2

cap = cv2.VideoCapture("demo.avi")

while (cap.isOpened()):
    # Frame by frame capture
    ret, frame = cap.read()

    ## Operations on frame ##
    # Convert to Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Display resulting frame
    cv2.imshow("frame", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()