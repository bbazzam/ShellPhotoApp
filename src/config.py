#'''
 # @ Author: Ben Azzam
 # @ Create Time: 2021-09-24 23:42:36
 # @ Modified by: Ben Azzam
 # @ Modified time: 2021-09-25 00:40:53
 # @ Description:
 #'''

import yaml
import logging

class Configuration:

   def __init__(self, configFile):
      self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
      self.log.info("Bootstrapping Config")
      try:
         with open(configFile, "r") as configF:
            self.cfg = yaml.load(configF, Loader=yaml.FullLoader)
      except:
        self.log.exception("Error Loading File ", configFile)

   def get(self, key, default = None):
       if (key in self.cfg):
          return self.cfg[key]
       else:
          return default
 

