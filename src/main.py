import sys
import pygame
import pathlib

from pygame.locals import *

def load_asset(name):
    return pygame.image.load(pathlib.Path(pathlib.Path(__file__).parent, "assets", name)).convert_alpha()

def center_surface(screen, surface: pygame.Surface):
    rect = surface.get_rect()
    rect.update((screen.get_width() - rect.width) / 2, (screen.get_height() - rect.height) / 2, rect.width, rect.height)

    return rect

if __name__ == "__main__":
    _, failed  = pygame.init()
    if failed > 0:
        print(f"{failed} module(s) failed to initialize")

    screen = pygame.display.set_mode((640, 360))
    text = pygame.font.SysFont(pygame.font.get_default_font(), 64)
    normal, pressed = load_asset("normal.png"), load_asset("pressed.png")
    n_rect, p_rect = center_surface(screen, normal), center_surface(screen, pressed)

    clicked = False
    button = normal
    rect = n_rect
    changed = True
    count = 0
    count_text = text.render(f"{count}", True, (0, 0, 0))
    c_rect = (rect.centerx - count_text.get_width() / 2, rect.centery - count_text.get_height() / 2)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    m_click = event.type == MOUSEBUTTONDOWN

                    if m_click != clicked:
                        clicked = m_click

                        button = pressed if clicked else normal
                        rect = p_rect if clicked else n_rect
                        if not clicked:
                            changed = True
                        elif rect.collidepoint(pygame.mouse.get_pos()):
                            count += 1
                            count_text = text.render(f"{count}", True, (0, 0, 0))
                            c_rect = (rect.centerx - count_text.get_width() / 2, rect.centery - count_text.get_height() / 2)
                            changed = True


        if changed:
            screen.fill((255, 255, 255))
            screen.blit(button, rect)
            screen.blit(count_text, c_rect)

            pygame.display.flip()

            changed = False