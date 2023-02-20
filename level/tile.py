import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_image, pos, size, *groups):
        super().__init__(*groups)
        self.image = tile_image
        self.rect = self.image.get_rect().move(
            size[0] * pos[0], size[1] * pos[1])
