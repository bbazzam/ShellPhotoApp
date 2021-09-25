import random
# from cv2 import *
import logging
import time
import uuid

from os import listdir
from os.path import isfile, join
from random import randrange, uniform
from datetime import datetime

class Camera:

   def __init__(self):
      self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
      self.loadCamera()

   def loadCamera(self):
      self.log.info("Loading Camera")

      return

   def takePicture(self):
       filename = "tmp/"+str(uuid.uuid1()) + ".jpg"

       self.log.info("Taking Picture")
      #  cam = cv2.VideoCapture(0)   # 0 -> index of camera
      #  s, img = cam.read()
      #  if s:    # frame captured without any errors
      #     cv2.namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
      #     cv2.imshow("cam-test",img)
      #     waitKey(0)
      #     destroyWindow("cam-test")
      #     cv2.imwrite(filename,img) #save image
       return filename