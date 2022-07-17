import cv2
from cv2 import threshold 
import numpy as np

def ShowImage(img, dir):
    cv2.imshow(dir, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


#? Read Images as is (with alpha channel, otherwise it gets cropped).
league_screen = cv2.imread('sample/league_screen.png', cv2.IMREAD_UNCHANGED)
target = cv2.imread('sample/target.png', cv2.IMREAD_UNCHANGED)

#? Convert to Grayscale
result = cv2.matchTemplate(league_screen, target, cv2.TM_CCOEFF_NORMED)

#? Find the location of the best match
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

w = target.shape[1]
h = target.shape[0]

#? Threshold is set to 0.60 to get only the best match
threshold = 0.60
#? Find the location of the best match
yloc, xloc = np.where(result >= threshold)

#? x,y,w,h
rectangles = []
for (x,y) in zip(xloc, yloc):
    #The rectangles are duplicated because will passed in group Function
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])

#Rectangles are passed in group function, to get the best matches
rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

#Now we can draw the rectangles
for (x,y,w,h) in rectangles:
    cv2.rectangle(league_screen, (x,y), (x+w, y+h), (0,255,0), 2)

ShowImage(league_screen, 'league_screen')
