# from gpiozero import Button
# from picamera import PiCamera
import logging
import keyboard
import time

from signal import pause
from audioplayer import AudioPlayer

class App: 

   def __init__(self):
     self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
     self.audioPlayer = AudioPlayer()
     self.initSoundPlayer()

# camera = PiCamera()


   def take_picture_with_camera(self):
    # image_path = '/home/pi/images/image_%s.jpg' % int(round(time.time() * 1000))
    # camera.capture(image_path)
      print('Took photo')
 
# button = Button(4)
# button.when_pressed = take_picture_with_camera
 
   def initSoundPlayer(self):
      print("Loading audio file")
      self.audioPlayer.loadaudio("audio")
      self.audioPlayer.playSound()
      return


# pause()


