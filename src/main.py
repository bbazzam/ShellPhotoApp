import os
import logging

from app import App
def main(args):
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

    logging.info('Started')
    app = App()
    logging.info('Finished')

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
