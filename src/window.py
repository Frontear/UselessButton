import pygame
import logging

from pygame.constants import QUIT

class Window:
    _pygame_init = False

    def __init__(self, logger: logging.Logger) -> None:
        if not Window._pygame_init:
            _, fails = pygame.init()

            if fails > 0:
                logger.warning(f"some pygame modules failed to initialize ({fails} failed)..")
            
            Window._pygame_init = True

    def create_display(self, title: str, width: int, height: int, frames: int = 30) -> None:
        self.surface = pygame.display.set_mode((width, height))
        self.ticker = pygame.time.Clock()
        self.fps = frames

        self.surface.fill((200, 200, 200))
        pygame.display.set_caption(title)

    def run(self) -> None:
        exit = False
        while not exit:
            self.ticker.tick(self.fps)

            for e in pygame.event.get():
                if e.type == QUIT:
                    exit = True
            
            pygame.display.update()

    def close(self):
        pygame.quit()

        Window._pygame_init = False