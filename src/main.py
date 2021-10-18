import window
import pygame
import logging

from pygame.locals import *

def main():
    logging.basicConfig(format='[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
    screen = window.Window(logging.getLogger("UselessButton"))
    
    screen.create_display("UselessButton", 640, 360, 60)
    screen.run()
    screen.close()

if __name__ == "__main__":
    main()