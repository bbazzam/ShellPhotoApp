#'''
 # @ Author: Ben Azzam
 # @ Create Time: 2021-09-24 23:42:36
 # @ Modified by: Ben Azzam
 # @ Modified time: 2021-09-25 00:40:53
 # @ Description:
 #'''

import random
import cv2
import logging
import time
import uuid

from os import listdir
from os.path import isfile, join
from random import randrange, uniform
from datetime import datetime

class Camera:
   WINDOW_TIME_DISPLAY_MS = 3000

   def __init__(self, config):
      self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
      self.log.info("Bootstrapping Camera")
      self.loadCamera()
      Camera.WINDOW_TIME_DISPLAY_MS = config.get("windowTimeDisplayMS", Camera.WINDOW_TIME_DISPLAY_MS)

   def loadCamera(self):
      self.cam = cv2.VideoCapture(0)   # 0 -> index of camera
      return

   def takePicture(self, photoDir):
       filename = photoDir + str(uuid.uuid1()) + ".jpg"
       self.log.info("Taking Picture, %s", filename)
       try:
         s, img = self.cam.read()
         if s:    # frame captured without any errors
            cv2.namedWindow("cam-test", cv2.WINDOW_NORMAL)
            if logging.DEBUG >= logging.root.level:
               # Temporarily show the image in debug mode
               self.log.info("Previewing image")
               cv2.imshow("cam-test", img)
               self.log.debug("Displaying window")            
               cv2.waitKey(Camera.WINDOW_TIME_DISPLAY_MS)
               cv2.destroyWindow("cam-test")
               cv2.waitKey(10)
               self.log.debug("Destroyed window")
            self.log.info("Saving Image, %s", filename)
            cv2.imwrite(filename, img) #save image
       except:
          self.log.exception("Issue proessing image bailing, %s ", filename)
          return None
       return filename
