import pygame
from PIL import Image

from hero import Hero
from screens import start_screen, finish, Hud, need_to_quit_level, menu
from db_funcs import auto_login
from utils import screen, collectibles, enemies, camera_group

im = Image.open('data/Анимации_для_главного_героя.png')
for y in range(8):
    for x in range(10):
        if y == 3 and x == 1:
            part = im.crop((120 * x - 5, 130 * y, 120 * (x + 1), 130 * (y + 1)))
        else:
            part = im.crop((120 * x, 130 * y, 120 * (x + 1), 130 * (y + 1)))
        if len(part.getcolors()) == 1:
            pass
        else:
            part.save(f'data/{y + 1}_{x + 1}.png')
im.close()

im = Image.open('data/Анимации_для_врага1.png')
for x in range(4):
    part = im.crop((x * 64, 0, (x + 1) * 64, 64))
    part.save(f'data/enemies/bat/{x + 1}.png')
im.close()


"""
Основная часть игры. Здесь происходит создание игрока, экрана и основного цикла
"""

if __name__ == '__main__':

    scores = auto_login()

    running = True
    fps = 60
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))

    main_character = Hero(x=500, y=500, h=110, w=130, group=camera_group)

    all_sprites = pygame.sprite.Group()

    pygame.mixer.init()
    pygame.mixer.music.load('data/main_menu_theme.mp3')
    pygame.mixer.music.play()
    level_chosen = 0
    time_level_started = 0
    while not level_chosen or not time_level_started:
        level_chosen, time_level_started = start_screen(main_character, hud=None)

    hud = Hud(camera_group, level_chosen, time_level_started, main_character)

    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif time_level_started and level_chosen and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                need_to_quit_level = menu(need_to_quit_level, time_level_started, hud)
            elif pygame.key.get_pressed()[pygame.K_w]:
                main_character.facing = 'up'
                main_character.moving = True
            elif pygame.key.get_pressed()[pygame.K_d]:
                main_character.facing = 'right'
                main_character.moving = True
            elif pygame.key.get_pressed()[pygame.K_s]:
                main_character.facing = 'down'
                main_character.moving = True
            elif pygame.key.get_pressed()[pygame.K_a]:
                main_character.facing = 'left'
                main_character.moving = True
            else:
                main_character.moving = False
                main_character.v = 2
            if pygame.key.get_pressed()[pygame.K_LSHIFT] and main_character.moving:
                main_character.v = 4
            else:
                main_character.v = 2
        if need_to_quit_level:
            need_to_quit_level = False
            time_level_started, level_chosen, ntsms, need_to_quit_level = finish(main_character)
            if ntsms:
                while not level_chosen or not time_level_started:
                    level_chosen, time_level_started = start_screen(main_character, hud)
        elif ((pygame.time.get_ticks() - time_level_started) // 1000 > level_chosen * 120
                or len(collectibles.sprites()) <= 0 or
                main_character.hp <= 0) and time_level_started and level_chosen:
            time_level_started, level_chosen, ntsms, need_to_quit_level = finish(main_character)
            if ntsms:
                while not level_chosen or not time_level_started:
                    level_chosen, time_level_started = start_screen(main_character, hud)
        collectibles.update()
        main_character.update()
        enemies.update()
        camera_group.custom_draw(main_character)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
