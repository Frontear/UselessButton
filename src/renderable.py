import pygame

from abc import ABC, abstractmethod

class Renderable(ABC):
    @abstractmethod
    def on_event(self, event: pygame.event.Event):
        pass

    @abstractmethod
    def render(self, screen: pygame.surface.Surface):
        pass