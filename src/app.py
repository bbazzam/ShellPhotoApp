#'''
 # @ Author: Ben Azzam
 # @ Create Time: 2021-09-24 17:42:33
 # @ Modified by: Ben Azzam
 # @ Modified time: 2021-09-25 00:41:24
 # @ Description:
 #'''

import datetime
import logging
import re
import threading
import keyboard
import time
import os 

from threading import Thread

from signal import pause
from audioplayer import AudioPlayer
from camera import Camera
from emailClient import EmailClient

class App: 
   MIN_ELAPSE_TIME_SEC = 10
   MAX_TMP_FILE_COUNT = 3
   PHOTO_TMP_DIR = "tmp/"
   LISTEN_KEY = 'enter'

   def __init__(self, configFile):
     self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
     self.audioPlayer = AudioPlayer()
     self.camera = Camera()
     self.emailClient = EmailClient(configFile)

     self.initSoundPlayer()
     logging.basicConfig(level=logging.DEBUG)
     self.lastTimeRunSec = 1
     self.stop_event = threading.Event()
     self.thread = Thread(target = self.threaded_function())
     self.thread.start()
     self.thread.join()

   def initSoundPlayer(self):
      print("Loading audio file")
      self.audioPlayer.loadAudio("audio")
      self.audioPlayer.playSound(False)
      return

   def photoDirCleanup(self):
      # Only keep N number of photos so we don't kill the mem
      # recursive call to keep deleting until we hit the max allowed 
      try:
         list_of_files = os.listdir(App.PHOTO_TMP_DIR)
         full_path = [App.PHOTO_TMP_DIR + "{0}".format(x) for x in list_of_files]
         self.log.debug("Number of files stored %d", len(list_of_files))
         if len(list_of_files) > App.MAX_TMP_FILE_COUNT:
            self.log.info("Number of photos stored %d exceeds max %d allowed", len(list_of_files), App.MAX_TMP_FILE_COUNT)
            oldest_file = min(full_path, key=os.path.getctime)
            os.remove(oldest_file)  
            self.log.info("Removing file %s", oldest_file)
         return

      except:
         self.log.exception("Exception during cleanup ")
      return

  # Thread that will sit and wait for the enter event    
   def threaded_function(self):
      while not self.stop_event.is_set():
         keyboard.wait(App.LISTEN_KEY)
         self.log.debug(time.time())
         if (time.time() - self.lastTimeRunSec > App.MIN_ELAPSE_TIME_SEC):
            self.audioPlayer.playSound(False)
            picture = self.camera.takePicture(App.PHOTO_TMP_DIR)
            if (picture != None):
               self.emailClient.sendPicture(picture)
            else:
               self.log.error("Return none from camera module, not emailing")
            self.photoDirCleanup()
            self.lastTimeRunSec = time.time()
         else:
            self.log.info("Wait num seconds before trying again %f", App.MIN_ELAPSE_TIME_SEC - (time.time() - self.lastTimeRunSec))
   
