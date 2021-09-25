# from gpiozero import Button
# from picamera import PiCamera
import datetime
import logging
import threading
import keyboard
import time
from threading import Thread

from signal import pause
from audioplayer import AudioPlayer
from camera import Camera
from emailClient import EmailClient

class App: 
   MIN_ELAPSE_TIME_SEC = 10

   def __init__(self):
     self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
     self.audioPlayer = AudioPlayer()
     self.camera = Camera()
     self.emailClient = EmailClient()

     self.initSoundPlayer()
     logging.basicConfig(level=logging.DEBUG)
     self.lastTimeRunSec = time.time()
     self.stop_event = threading.Event()
     self.thread = Thread(target = self.threaded_function())
     self.thread.start()
     self.thread.join()

   

   def initSoundPlayer(self):
      print("Loading audio file")
      self.audioPlayer.loadAudio("audio")
      self.audioPlayer.playSound(False)
      return
      
   def takingPicture(self):
    # image_path = '/home/pi/images/image_%s.jpg' % int(round(time.time() * 1000))
    # camera.capture(image_path)
    self.log.info("Taking picture")

   def emailingPicture(self):
      # image_path = '/home/pi/images/image_%s.jpg' % int(round(time.time() * 1000))
      # camera.capture(image_path)
      self.log.info("Emailing Picture")

   def threaded_function(self):
      while not self.stop_event.is_set():
         keyboard.wait('enter')
         self.log.debug(time.time())
         if (time.time() - self.lastTimeRunSec > App.MIN_ELAPSE_TIME_SEC):
            # print("running")
            # time.sleep(1)
            self.audioPlayer.playSound(False)
            self.camera.takePicture()
            self.emailClient.sendPicture()
            self.lastTimeRunSec = time.time()
         else:
            self.log.info("Wait num seconds before trying again %f", App.MIN_ELAPSE_TIME_SEC - (time.time() - self.lastTimeRunSec))



# pause()


