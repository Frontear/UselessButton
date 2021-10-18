import button
import pygame
import pathlib

from pygame.locals import *

mouse_down = False
count = 0


def tick(screen: pygame.Surface, button: button.Button) -> bool:
    global mouse_down
    global count

    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
            if event.button == 1:
                mouse_down = event.type == MOUSEBUTTONDOWN

                if mouse_down:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()

                    pygame.mixer.music.play()

                    count += 1

    screen.fill((255, 255, 255))
    button.draw(screen, mouse_down, count)

    return True


def main() -> None:
    pygame.init()

    pygame.mixer.music.load(pathlib.Path(
        pathlib.Path(__file__).parent, "assets", "thud.mp3"))
    pygame.mixer.music.set_volume(0.2)

    SCREEN = pygame.display.set_mode((640, 360))
    CLOCK = pygame.time.Clock()
    BUTTON = button.Button()

    while tick(SCREEN, BUTTON):
        pygame.display.update()
        CLOCK.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
