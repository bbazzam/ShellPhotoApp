import random
import vlc
import logging
import time

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
       self.log.info("Taking Picture")
       return
