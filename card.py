import init
from init import *


class Card(pygame.sprite.Sprite):
    def __init__(self, key: int, group: pygame.sprite.Group):
        pygame.sprite.Sprite.__init__(self)
        self.key = key
        self.image = pygame.Surface((65, 75))
        self.image.fill(init.GREY)
        self.rect = self.image.get_rect()
        self.add(group)
        self.real_image = pygame.transform.scale(init.images[key], (65, 75))
        self.status = False
        self.out = False

    def switch(self):
        if self.status:
            self.image = self.image = pygame.Surface((65, 75))
            self.image.fill(init.GREY)
        else:
            self.image = self.real_image
        self.status = not self.status

    def set_place(self, place):
        self.rect.center = place

    def is_out(self):
        return self.out

    def make_out(self):
        self.out = True

    def is_shown(self):
        return self.status
