#with this code you can capture your screen

import numpy as np
import cv2
from PIL import ImageGrab

while(True):
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
