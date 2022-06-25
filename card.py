from init import *


class Card(pygame.sprite.Sprite):
    def __init__(self, key: int, group: pygame.sprite.Group):
        pygame.sprite.Sprite.__init__(self)
        self.key = key
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.add(group)

    def set_color(self, color):
        self.image.fill(color)

    def set_place(self, place):
        self.rect.center = place
