import numpy as np
import cv2

img = cv2.imread('../pocketWatch.jpg',0)

if img is None:
    print("Could not open or find the image")
    exit()
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
