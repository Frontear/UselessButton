from os import path
import pygame
import pathlib


class Button:
    ASSETS = pathlib.Path(pathlib.Path(__file__).parent, "assets")

    def __init__(self) -> None:
        self.pressed = pygame.image.load(
            pathlib.Path(Button.ASSETS, "pressed.png"))
        self.released = pygame.image.load(
            pathlib.Path(Button.ASSETS, "released.png"))

        self.text = pygame.font.SysFont(pygame.font.get_default_font(), 64)

    def draw(self, screen: pygame.Surface, state: bool, count: int):
        surface = self.pressed if state else self.released
        counter = self.text.render(str(count), True, (0, 0, 0))
        rect = surface.get_rect()

        rect.update((screen.get_width() - rect.width) / 2,
                    (screen.get_height() - rect.height) / 2, rect.width, rect.height)

        screen.blit(surface, rect)
        screen.blit(counter, (rect.centerx - counter.get_width() /
                    2, rect.centery - counter.get_height() / 2))
