import random
import vlc
import logging
import time

from os import listdir
from os.path import isfile, join
from random import randrange, uniform
from datetime import datetime

class EmailClient:

   def __init__(self):
      self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
      self.loadEmailClient()

   def loadEmailClient(self):
      self.log.info("Loading Email Client")

      return

   def sendPicture(self):
       self.log.info("Emailing Picture")
       return
