import character as character_module
from level.level import *
import level.tile as tile_module
import enemy as enemy_module
import random
import pygame
import pygame_menu

clock = pygame.time.Clock()
# инициализация
pygame.init()

# зададим размер экрана приложения
SIZE = (WIDTH, HEIGHT) = (500, 500)
# задаем сам экран с нужным размером
screen = pygame.display.set_mode(SIZE)

# название вкладки
pygame.display.set_caption("Candy Dream")
BACKGROUND_MENU_PATH = "img/menu.png"

# создаем изображение для меню
backgound_img = pygame_menu.baseimage.BaseImage(
    image_path=BACKGROUND_MENU_PATH,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
    drawing_offset=(0, 0)
)
# создаем свою тему для меню
theme = pygame_menu.themes.Theme(
    background_color=backgound_img,
    title_background_color=(0, 0, 0),
    widget_font=pygame_menu.font.FONT_BEBAS,
    title_font=pygame_menu.font.FONT_BEBAS,
    widget_font_size=40,
    title_font_size=35,
    title_font_color=(0, 0, 0),
    widget_font_color=(0, 0, 0),
    widget_margin=(0, 0),
    widget_padding=30,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE
)

pygame.init()


def draw_text(surface, text, rate, x, y, color):
    font = pygame.font.Font('img/NerkoOne-Regular.ttf', rate)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


background_game_img = pygame.image.load("img/background1.png")
size = width, height = 500, 500
pygame.display.set_caption('Candy Dream')

all_sprites = pygame.sprite.Group()

tiles_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
empty_tile_group = pygame.sprite.Group()
candy_group = pygame.sprite.Group()

player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

lvl = Level('img/lvl.txt')
player, level_x, level_y = lvl.generate_level(tile_module, character_module, enemy_module,
                                              player_group,
                                              tiles_group, walls_group,
                                              empty_tile_group, enemy_group, all_sprites)

enemy_hitable = pygame.image.load('img/candy.png')
enemy_time = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_time, 3500)
candy_in_game = []

label = pygame.font.Font('img/NerkoOne-Regular.ttf', 40)
label_lose = label.render('You lost!', True, (255, 0, 0))
label_win = label.render('You win!', True, (0, 255, 0))
label_restart = label.render('start again', True, (255, 255, 255))
label_restart_rect = label_restart.get_rect(topleft=(150, 200))


def startGame():
    FPS = 20
    tick = 0
    cl = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                quit()
            if event.type == enemy_time:
                candy_in_game.append(enemy_hitable.get_rect(topleft=(500, random.randint(70, 250))))
            player_group.update(event)

        if not player.win and player.alive:
            screen.blit(background_game_img, (0, 0))
            tiles_group.draw(screen)
            player_group.draw(screen)
            enemy_group.draw(screen)
            if candy_in_game:
                for (i, e) in enumerate(candy_in_game):
                    screen.blit(enemy_hitable, e)
                    e.x -= 5
                    if e.x < -5:
                        candy_in_game.pop(i)
                    if player.rect.colliderect(e):
                        player.collected_candies += 10
                        candy_in_game.pop(i)
            all_sprites.update()
            tick += 1
            cl.tick(FPS)
            draw_text(screen, "SCORE", 14, 220, 5, (0, 0, 0))
            draw_text(screen, str(player.collected_candies), 20, 220, 14, (255, 0, 0))
            draw_text(screen, "HEALTH", 14, 270, 5, (0, 0, 0))
            draw_text(screen, str(player.health), 20, 270, 14, (0, 255, 0))

        elif player.win:
            collected_candies = label.render(f'your score: {player.collected_candies}', True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(label_win, (180, 10))
            screen.blit(collected_candies, (150, 30))
            screen.blit(label_restart, label_restart_rect)
            mouse_coords = pygame.mouse.get_pos()
            if label_restart_rect.collidepoint(mouse_coords) and pygame.mouse.get_pressed()[0]:
                player.rect = player.rect.move(-player.rect.x + 20, -player.rect.y + 20)
                player.image = player.frames[1]
                player.health = 50
                player.collected_candies = 0
                player.win = False

        else:
            collected_candies = label.render(f'your score: {player.collected_candies}', True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(label_lose, (180, 10))
            screen.blit(collected_candies, (150, 30))
            screen.blit(label_restart, label_restart_rect)
            mouse_coords = pygame.mouse.get_pos()
            if label_restart_rect.collidepoint(mouse_coords) and pygame.mouse.get_pressed()[0]:
                player.rect = player.rect.move(-player.rect.x + 20, -player.rect.y + 20)
                player.image = player.frames[1]
                player.health = 50
                player.collected_candies = 0
                player.alive = True
        pygame.display.flip()


menu = pygame_menu.Menu('', WIDTH, HEIGHT, theme=theme)
menu.add.button('PLAY', startGame)
menu.add.button('EXIT', pygame_menu.events.EXIT)
menu.mainloop(screen)
