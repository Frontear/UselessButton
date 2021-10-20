import pygame
import logging

from pygame.constants import QUIT
from renderable import Renderable

class Window:
    _pygame_init = False

    def __init__(self, logger: logging.Logger) -> None:
        if not Window._pygame_init:
            _, fails = pygame.init()

            if fails > 0:
                logger.warning(f"some pygame modules failed to initialize ({fails} failed)..")

            self.renderables = []

            Window._pygame_init = True

    def create_display(self, title: str, width: int, height: int, frames: int = 30) -> None:
        self.surface = pygame.display.set_mode((width, height))
        self.ticker = pygame.time.Clock()
        self.fps = frames

        pygame.display.set_caption(title)

    def add_renderable(self, object: Renderable):
        self.renderables.append(object)

    def run(self) -> None:
        exit = False
        while not exit:
            self.ticker.tick(self.fps)

            for e in pygame.event.get():
                if e.type == QUIT:
                    exit = True

                for x in self.renderables:
                    x.on_event(e)

            self.surface.fill((200, 200, 200))

            for x in self.renderables:
                x.render(self.surface)

            pygame.display.update()

    def close(self):
        pygame.quit()

        Window._pygame_init = False