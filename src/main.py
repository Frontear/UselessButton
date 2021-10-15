import button
import pygame

from pygame.locals import *

def tick(screen: pygame.Surface, button: button.Button) -> bool:
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
            if event.button == 1:
                button.update(event.type == MOUSEBUTTONDOWN)

    screen.fill((255, 255, 255))
    button.draw(screen)

    return True


def main() -> None:
    pygame.init()

    SCREEN = pygame.display.set_mode((640, 360))
    CLOCK = pygame.time.Clock()

    BUTTON = button.Button()

    while tick(SCREEN, BUTTON):
        pygame.display.update()
        CLOCK.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
