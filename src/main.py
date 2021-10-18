import pygame
import logging

from pygame.locals import *

def main(logger: logging.Logger):
    _, fails = pygame.init()
    if fails > 0:
        logger.warning(f"some pygame modules failed to init ({fails} failed)")
    
    pygame.display.set_mode((640, 360))
    pygame.display.set_caption("Useless Button")
    pygame.display.get_surface().fill((200, 200, 200))

    ticker = pygame.time.Clock()

    run = True
    while run:
        ticker.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                run = False
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    logging.basicConfig(format='[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

    main(logging.getLogger("UselessButton"))