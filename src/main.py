#'''
 # @ Author: Ben Azzam
 # @ Create Time: 2021-09-24 16:30:59
 # @ Modified by: Ben Azzam
 # @ Modified time: 2021-09-25 00:40:23
 # @ Description:
 #'''

import os
import logging
import sys
import argparse
from config import Configuration

from app import App
def main():
    """
    """
    logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("log/shellphoto.log"),
        logging.StreamHandler()
    ]
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=False)
    args = parser.parse_args()
    
    configFile = "config/shellcamera.yml"
    if (args.config != None):
        configFile = args.config
    print('***** config,', args.config)
    
    config = Configuration(configFile)
    
    logging.info('Started')
    app = App(config)
    logging.info('Finished')

if __name__ == '__main__':
    import sys
    main()
