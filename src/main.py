import os
from app import App
def main(args):
    """
    """
    app = App()
    app.startSound()
    print("Starting audio")

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
