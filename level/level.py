import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    return image


class Level:
    tile_images = {
        'wall': load_image('barriere_tile.png'),
        'empty': load_image('empty_tile.png')
    }
    player_image = load_image('cat_walk.png')
    enemy_image = load_image('enemy.png')

    def __init__(self, filename):
        self.filename = filename
        self.data_level = self.load_level()

    def load_level(self):
        # читаем уровень, убирая символы перевода строки
        with open(self.filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

        # и подсчитываем максимальную длину
        max_width = max(map(len, level_map))

        # дополняем каждую строку пустыми клетками ('.')
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))

    def generate_level(self, tile_module, character_module, enemy_module, player_group, tile_group, wall_group,
                       empty_group, enemy_group,
                       all_sprites):
        new_player, x, y = None, None, None
        for y in range(len(self.data_level)):
            for x in range(len(self.data_level[y])):
                if self.data_level[y][x] == '.':
                    tile_module.Tile(self.tile_images['empty'], (x, y), (20, 20), empty_group, tile_group, all_sprites)
                elif self.data_level[y][x] == '#':
                    tile_module.Tile(self.tile_images['wall'], (x, y), (20, 20), wall_group, tile_group, all_sprites)
                elif self.data_level[y][x] == '@':
                    tile_module.Tile(self.tile_images['empty'], (x, y), (20, 20), empty_group, tile_group, all_sprites)
                    new_player = character_module.Character(self.player_image, 3, 4, 20, 20, enemy_group,
                                                            wall_group,
                                                            player_group, all_sprites)
                elif self.data_level[y][x] == '+':
                    tile_module.Tile(self.tile_images['empty'], (x, y), (20, 20), empty_group, tile_group, all_sprites)
                    enemy_module.Enemy(self.enemy_image, (x, y), (17, 17), enemy_group, all_sprites)
        return new_player, x, y
