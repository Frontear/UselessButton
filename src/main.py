import pygame
import texture

from pygame.locals import *


def tick(screen: pygame.Surface, *textures: texture.Texture) -> bool:
    for event in pygame.event.get():
        if event.type == QUIT:
            return False

    screen.fill((255, 255, 255))
    textures[0].draw(screen)

    return True


def main() -> None:
    pygame.init()

    SCREEN = pygame.display.set_mode((640, 360))
    CLOCK = pygame.time.Clock()

    RELEASED = texture.Texture("released.png")
    PRESSED = texture.Texture("pressed.png")

    print(RELEASED.image.get_rect())
    print(PRESSED.image.get_rect())

    while tick(SCREEN, RELEASED, PRESSED):
        pygame.display.update()
        CLOCK.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
