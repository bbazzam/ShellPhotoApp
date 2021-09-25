import vlc
import logging

from os import listdir
from os.path import isfile, join
from random import randrange, uniform

class AudioPlayer:

   def __init__(self):
      self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
      self.audiofiles = []
      self.audioDir = ""
   
   def loadaudio(self, audiodir):
      self.audioDir = audiodir
      self.log.info("Loading from the directory: %s", self.audioDir)

      self.audiofiles = [f for f in listdir(self.audioDir) if isfile(join(self.audioDir, f))]
      
      print('Found files:', self.audiofiles, sep='  ')
      self.log.info('Found files:', self.audiofiles, sep='  ')

      return

   def playSound(self):
       max = len(self.audiofiles)
       self.log.info("max %s", max)

       playIndex = 3 #randrange(0,max)
       print("playing audio at index {}, sound {}".format(playIndex, self.audiofiles[playIndex]))
       self.log.info('Found files:', self.audiofiles, sep='  ')

       p = vlc.MediaPlayer("{}/{}".format(self.audioDir, self.audiofiles[playIndex]))
       p.play()
       return

