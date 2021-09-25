import random
import vlc
import logging
import time

from os import listdir
from os.path import isfile, join
from random import randrange, uniform
from datetime import datetime

class AudioPlayer:

   def __init__(self):
      self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
      self.audiofiles = []
      self.audioDir = ""
      self.max = 0
   
   def loadaudio(self, audiodir):
      self.audioDir = audiodir
      self.log.info("Loading from the directory: %s", self.audioDir)

      self.audiofiles = [f for f in listdir(self.audioDir) if isfile(join(self.audioDir, f))]
      
      self.log.info("[%s]", ', '.join(self.audiofiles))
      self.audioCount = len(self.audiofiles)
      self.log.info("Audio file count %s", self.audioCount)

      return

   def playSound(self):
       random.seed(datetime.now())

       playIndex = randrange(0, self.audioCount)
       self.log.info("Selected audio at index %s, sound %s", playIndex, self.audiofiles[playIndex])

       p = vlc.MediaPlayer("{}/{}".format(self.audioDir, self.audiofiles[playIndex]))
       self.log.info("Playing Audio: %s/%s", self.audioDir, self.audiofiles[playIndex])
       p.play()
       time.sleep(1.5)
       duration = p.get_length() / 1000
       time.sleep(duration)

       return
