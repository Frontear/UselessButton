import pygame
from pygame.locals import *

def tick(surface: pygame.Surface) -> bool:
    for event in pygame.event.get():
        if event.type == QUIT:
            return False

    surface.fill((255, 255, 255))
    
    return True

def main() -> None:
    pygame.init()
    
    SURFACE = pygame.display.set_mode((640, 360))
    CLOCK = pygame.time.Clock()

    while tick(SURFACE):
        pygame.display.update()
        CLOCK.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()