import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, enemy_group,
                 wall_group, *groups):
        super().__init__(*groups)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.health = 50

        self.rect = self.rect.move(x, y)
        self.counter = 0
        self.wall = wall_group
        self.enemies = enemy_group
        self.collected_candies = 0

        self.alive = True
        self.win = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def acts(self, event):
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.rect.x >= 10:
            if self.counter >= 6 or self.counter < 3:
                self.counter = 3
            self.image = self.frames[self.counter]
            self.counter += 1
            self.rect.x -= 10

        elif pygame.key.get_pressed()[pygame.K_RIGHT] and self.rect.x <= 450:
            if self.counter >= 9 or self.counter < 6:
                self.counter = 6
            self.image = self.frames[self.counter]
            self.counter += 1
            self.rect.x += 10

        elif pygame.key.get_pressed()[pygame.K_UP] and self.rect.y >= 10:
            if self.counter >= 12 or self.counter < 9:
                self.counter = 9

            self.image = self.frames[self.counter]
            self.counter += 1
            self.rect.y -= 10

        elif pygame.key.get_pressed()[pygame.K_DOWN] and self.rect.y <= 450:
            if self.counter >= 3 or self.counter < 0:
                self.counter = 0
            self.image = self.frames[self.counter]
            self.counter += 1
            self.rect.y += 10

        if 490 >= self.rect.x >= 400 and self.rect.y >= 460 and self.collected_candies >= 100:
            self.win = True

        if pygame.sprite.spritecollide(self, self.enemies, False):
            if self.health == 0:
                self.alive = False
            else:
                self.health -= 0.5

        if pygame.sprite.spritecollideany(self, self.wall):
            self.alive = False

    def update(self, *args):
        if args:
            self.acts(args[0])

