import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_image, pos, size, *groups):
        super().__init__(*groups)
        self.direction = 1
        self.image = enemy_image
        self.rect = self.image.get_rect().move(
            size[0] * pos[0], size[1] * pos[1])
        self.start = self.rect.x
        self.stop = self.rect.x + 50

    def update(self):
        if self.rect.x >= self.stop:
            self.rect.x = self.stop
            self.direction = -1
        if self.rect.x <= self.start:
            self.rect.x = self.start
            self.direction = 1
        self.rect.x += self.direction
