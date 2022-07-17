from multiprocessing.dummy import Array
import cv2
from cv2 import threshold
import numpy as np
import pyautogui

class Box:
    
    threshold = 0.25

    #? Initialize Public Dictionarys
    Images = {}
    Matchs = {}
    Rectangles = {}
    Weights = {}
    
    RectangleNames_Global = []

    #? Show Image 
    def Show(self, dir: str = None,  image: Array = [],):
        #check if image is empty
        if len(image) != 0:
            cv2.imshow(dir, image)
        else:
            cv2.imshow(dir, self.Images['default'])

    #? Read Image as is (with alpha channel, otherwise it gets cropped), add results to Images Dictionary
    def Read(self, name: str = None, dir= None):
        self.Images[name] = cv2.imread(dir, cv2.IMREAD_UNCHANGED)


    #? 1. Match Templates, adding results to Matchs Dictionary
    #? 2. Group Rectangles, adding results to Rectangles Dictionary
    def Setup(self, name: Array, target: Array = [], image: Array = []):
        #? Verifica se o usuário pretende utilizar a imagem padrão, Null = Sim
        if len(image) != 0:
             #? Verifica se o usuário pretende utilizar o target padrão (o mesmo informado no name), Null = Sim
             if len(target) != 0:
                self.Matchs[name] = cv2.matchTemplate(image, target, cv2.TM_CCOEFF_NORMED)
             else:
                self.Images['default'] = image
                for cname in name:
                    self.Matchs[cname] = cv2.matchTemplate(image, self.Images[cname], cv2.TM_CCOEFF_NORMED)
        else:
             #? Verifica se o usuário pretende utilizar o target padrão (o mesmo informado no name), Null = Sim
             if len(target) != 0:
                self.Matchs[name] = cv2.matchTemplate(self.Images['default'], target, cv2.TM_CCOEFF_NORMED)
             else:
                for cname in name:
                    self.Matchs[cname] = cv2.matchTemplate(self.Images['default'], self.Images[cname], cv2.TM_CCOEFF_NORMED)

        #Save names to use in another areas.
        self.RectangleNames_Global = name

        for current in name:
            w = self.Images[current].shape[1]
            h = self.Images[current].shape[0]
            #? Find the location of the best match
            yloc, xloc = np.where(self.Matchs[current] >= self.threshold)
            #? x,y,w,h
            rectangles = []
            for (x,y) in zip(xloc, yloc):
                #The rectangles are duplicated because will passed in group Function
                rectangles.append([int(x), int(y), int(w), int(h)])
                rectangles.append([int(x), int(y), int(w), int(h)])
            #Rectangles are passed in group function, to get the best matches
            self.Rectangles[current], self.Weights[current] = cv2.groupRectangles(rectangles, 1, 0.2)

    
    #? Draw Rectangles on Image
    def Draw(self, HaveToShow: bool = True, name: str = None, image: Array = [],):
        #Now we can draw the rectangles
        if len(image) != 0:
            #check if name is null
            if name != None:
                for (x,y,w,h) in self.Rectangles[name]:
                    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
        else:
            if name != None:
                for (x,y,w,h) in self.Rectangles[name]:
                    cv2.rectangle(self.Images['default'], (x,y), (x+w, y+h), (0,255,0), 2)
            else:
                for cretangles in self.RectangleNames_Global:
                    for (x,y,w,h) in self.Rectangles[cretangles]:
                        cv2.rectangle(self.Images['default'], (x,y), (x+w, y+h), (0,255,0), 2)
        #? Show Image, If True
        if HaveToShow:
                self.Show()



