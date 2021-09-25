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
      audioDir = audiodir
      self.log.info("Loading from the directory: %s", audiodir)

      audiofiles = [f for f in listdir(audiodir) if isfile(join(audiodir, f))]
      
      print('Found files:', *audiofiles, sep='  ')
      self.log.info('Found files:', *audiofiles, sep='  ')

      return

   def playSound(self):
       max = len(self.audiofiles)
       self.log.info("max %s", max)

       playIndex = randrange(0,max)
       print("playing audio at index {}, sound {}".format(playIndex, self.audiofiles[playIndex]))
       p = vlc.MediaPlayer("{}/{}".format(self.audiofiles[playIndex]))
       p.play()
       return

