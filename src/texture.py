import pygame
import pathlib


class Texture(pygame.sprite.Sprite):
    ASSETS = pathlib.Path(pathlib.Path(__file__).parent, "assets")

    def __init__(self, file: str) -> None:
        super().__init__()

        self.image = pygame.image.load(pathlib.Path(Texture.ASSETS, file))
        self.rect = self.image.get_rect()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
