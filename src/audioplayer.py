#'''
 # @ Author: Ben Azzam
 # @ Create Time: 2021-09-24 19:26:49
 # @ Modified by: Ben Azzam
 # @ Modified time: 2021-09-25 00:41:10
 # @ Description:
 #'''

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

   def loadAudio(self, audiodir):
      # If error hard kill the application do not recover
      self.log.info("Bootstrapping Audio Player")
      self.audioDir = audiodir
      self.log.info("Loading from the directory: %s", self.audioDir)
      self.audiofiles = [f for f in listdir(self.audioDir) if isfile(join(self.audioDir, f))]
      self.audiofiles.remove(".DS_Store")
      self.log.info("[%s]", ', '.join(self.audiofiles))
      self.audioCount = len(self.audiofiles)
      self.log.info("Audio file count %s", self.audioCount)

   def playSound(self, shouldWait=False):
       """
       Parameters
       ----------
       shouldWait : boolean, optional
          Blocks until audio sound completes run
       """
       random.seed(datetime.now())
       playIndex = randrange(0, self.audioCount)
       try: 
         self.log.info("Selected audio at index %s, sound %s", playIndex, self.audiofiles[playIndex])
         p = vlc.MediaPlayer("{}/{}".format(self.audioDir, self.audiofiles[playIndex]))
         self.log.info("Playing Audio: %s/%s", self.audioDir, self.audiofiles[playIndex])
         p.play()
         time.sleep(1.5)
         if (shouldWait): 
            duration = p.get_length() / 1000
            time.sleep(duration)
       except :
          self.log.exception("Issue with audio file index %s", playIndex)
   
