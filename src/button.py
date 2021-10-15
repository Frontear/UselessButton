from os import path
import pygame
import pathlib

class Button:
    ASSETS = pathlib.Path(pathlib.Path(__file__).parent, "assets")
    
    def __init__(self) -> None:
        self.pressed = pygame.image.load(pathlib.Path(Button.ASSETS, "pressed.png"))
        self.released = pygame.image.load(pathlib.Path(Button.ASSETS, "released.png"))
        self.state = False

    def update(self, mouse_down: bool):
        self.state = mouse_down

    def draw(self, screen: pygame.Surface):
        surface = self.pressed if self.state else self.released
        rect = surface.get_rect()

        rect.update((screen.get_width() - rect.width) / 2, (screen.get_height()- rect.height) / 2, rect.width, rect.height)

        screen.blit(surface, rect)