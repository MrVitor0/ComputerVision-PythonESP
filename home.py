import cv2
from cv2 import threshold 
import numpy as np
from time import time, sleep
import pyautogui

from windowcapture import WindowCapture

import ESP

Box = ESP.Box()

loop_time = time()

# # initialize the WindowCapture class
wincap = WindowCapture('Pixelmon Brasil')

#Define Objects to Find
Box.Read('bench','images/bench.png')

loop_time = time()
while(True):
     # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
  
    Box.Setup(["bench"],
    [],
    screenshot)
    Box.Draw(True)


