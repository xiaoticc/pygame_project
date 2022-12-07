import pygame
import pygame_menu  # библиотека для создания меню

# инициализация
pygame.init()

# зададим размер экрана приложения
SIZE = (WIDTH, HEIGHT) = (600, 400)
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


def startGame():
    # главный цикл игры-приложения
    running = True
    while running:
        # перебираем все события, что случились
        for event in pygame.event.get():
            # если событие - это нажатие на крестик, то мы останавливаем цикл игры
            if event.type == pygame.QUIT:
                running = False
        # заливаем экран цветом
        screen.fill((0, 0, 0))
        # отвечает за плавность смены кадров
        pygame.display.flip()
    # выход
    pygame.quit()


# создаем меню с нашей темой
menu = pygame_menu.Menu("Let's start your dream!", WIDTH, HEIGHT, theme=theme)
# добавляем кнопки и действия к ним
menu.add.button('PLAY', startGame)
menu.add.button('Exit', pygame_menu.events.EXIT)
# цикл меню
menu.mainloop(screen)
