import pygame
import pathlib

from pygame import rect

from renderable import Renderable
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

class Button(Renderable):
    def __init__(self) -> None:
        core = pathlib.Path(pathlib.Path(__file__).parent, "assets")

        self.text = pygame.font.SysFont(pygame.font.get_default_font(), 64)

        self.down = pygame.image.load(pathlib.Path(core, "pressed.png"))
        self.up = pygame.image.load(pathlib.Path(core, "released.png"))

        pygame.mixer.music.load(pathlib.Path(core, "thud.mp3"))
        pygame.mixer.music.set_volume(0.2)

        self.state = False
        self.count = 0

    def on_event(self, event: pygame.event.Event):
        if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.state = event.type == MOUSEBUTTONDOWN
                if self.state:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()

                    pygame.mixer.music.play()

                    self.count += 1

    def render(self, screen: pygame.surface.Surface):
        obj = self.down if self.state else self.up
        counter = self.text.render(str(self.count), True, (0, 0, 0))
        rect = obj.get_rect()

        rect.update((screen.get_width() - rect.width) / 2, (screen.get_height() - rect.height) / 2, rect.width, rect.height)

        screen.blit(obj, rect)
        screen.blit(counter, (rect.centerx - counter.get_width() / 2, rect.centery - counter.get_height() / 2))