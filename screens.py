import pygame
from db_funcs import save_results_in_db
from level_generation import start_level
from utils import screen, horizontal_borders, vertical_borders, collectibles, enemies
from utils_for_screens import need_to_quit_level, delay_at_the_end


def start_screen(hero, hud):
    """
    Начальный экран с двумя кнопками: выйти из игры и выбрать уровень. В будущем планируется добавить настройки графики
    и многие другие опции.
    """
    global need1
    img = pygame.image.load('data/backgrounds/bg1.png')
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    smallfont = pygame.font.SysFont('Corbel', 35)
    height = screen.get_height()
    text1 = smallfont.render('Exit', True, color)
    text2 = smallfont.render('choose level', True, color)
    need1 = True

    while need1:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    pygame.quit()
                elif width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 + 50 <= mouse[1] <= height / 2 + 90:
                    return choose_level(hero, hud)
        screen.blit(img, (0, 0))
        mouse = pygame.mouse.get_pos()
        if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 2 - 140, height / 2, 280, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 140, height / 2, 280, 40])
        if width / 2 - 140 <= mouse[0] < width / 2 + 140 and height / 2 + 50 <= mouse[1] <= height / 2 + 90:
            pygame.draw.rect(screen, color_light, [width / 2 - 140, height / 2 + 50, 280, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 140, height / 2 + 50, 280, 40])
        screen.blit(text1, (width / 2 - 25, height / 2))
        screen.blit(text2, (width / 2 - 75, height / 2 + 50))

        pygame.display.update()


def choose_level(hero, hud):
    """
    Экран выбора уровня. Здесь присваются значения очень важным переменным, которые нужны в многих других функциях и
    классах, так например: level_chosen и time_level_started
    """
    global need1, level_chosen, time_level_started
    img = pygame.image.load('data/backgrounds/bg2.png')
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    smallfont = pygame.font.SysFont('Corbel', 35)
    height = screen.get_height()
    text1 = smallfont.render('Go back', True, color)
    text2 = smallfont.render('level 1', True, color)
    text3 = smallfont.render('level 2', True, color)
    need = True
    level_chosen = None
    time_level_started = None

    while need:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    need = False
                elif width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 + 50 <= mouse[1] <= height / 2 + 90:
                    level_chosen = 1
                    need = False
                    need1 = False
                    break
                elif width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 + 90 <= mouse[1] <= height / 2 + 140:
                    level_chosen = 2
                    need = False
                    need1 = False
                    break
        screen.blit(img, (0, 0))
        mouse = pygame.mouse.get_pos()
        if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 2 - 140, height / 2, 280, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 140, height / 2, 280, 40])
        if width / 2 - 140 <= mouse[0] < width / 2 + 140 and height / 2 + 50 <= mouse[1] <= height / 2 + 90:
            pygame.draw.rect(screen, color_light, [width / 2 - 140, height / 2 + 50, 280, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 140, height / 2 + 50, 280, 40])
        if width / 2 - 140 <= mouse[0] < width / 2 + 140 and height / 2 + 90 <= mouse[1] <= height / 2 + 140:
            pygame.draw.rect(screen, color_light, [width / 2 - 140, height / 2 + 100, 280, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 140, height / 2 + 100, 280, 40])
        screen.blit(text1, (width / 2 - 50, height / 2))
        screen.blit(text2, (width / 2 - 25, height / 2 + 50))
        screen.blit(text3, (width / 2 - 25, height / 2 + 100))

        pygame.display.update()
    if level_chosen:
        time_level_started = pygame.time.get_ticks()
        if hud is not None:
            hud.t = pygame.time.get_ticks()
            hud.lc = level_chosen
    if not need1:
        return start_level(level_chosen, hero, time_level_started)
    return 0, 0


def finish(hero):
    """
    Экран подсчёта результатов. Музыка останавливается, все спрайты убираются и сохраняется лучший результат в БД.
    """
    global need_to_start_main_screen, need_to_quit_level, delay_at_the_end, level_chosen, time_level_started
    time_level_finished = pygame.time.get_ticks()
    while (pygame.time.get_ticks() - time_level_finished) // 1000 != delay_at_the_end and not need_to_quit_level:
        pass
    pygame.mixer.music.stop()
    pygame.mixer.music.load('data/main_menu_theme.mp3')
    pygame.mixer.music.play()
    img = pygame.image.load('data/backgrounds/bg4.png')
    save_results_in_db(level_chosen,
                       [hero.score,
                        f'{(time_level_finished - time_level_started) // 1000}/{level_chosen * 120}'])
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    smallfont = pygame.font.SysFont('Corbel', 35)
    height = screen.get_height()
    text1 = smallfont.render('Congatulations!!!', True, color)
    text2 = smallfont.render('quit', True, color)
    text3 = smallfont.render(f'Your score: {hero.score}', True, (255, 0, 0))
    hero.score = 0
    level_chosen = 0
    time_level_started = 0
    need_to_start_main_screen = False
    need3 = True
    need_to_quit_level = False
    mouse = pygame.mouse.get_pos()

    while need3:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 + 100 <= mouse[1] <= height / 2 + 140:
                    need_to_start_main_screen = True
                    need3 = False
                    break
        screen.blit(img, (0, 0))
        mouse = pygame.mouse.get_pos()
        if width / 2 - 140 <= mouse[0] < width / 2 + 140 and height / 2 + 100 <= mouse[1] <= height / 2 + 140:
            pygame.draw.rect(screen, color_light, [width / 2 - 140, height / 2 + 100, 280, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 140, height / 2 + 100, 280, 40])
        screen.blit(text1, (width / 2 - 90, height / 2))
        screen.blit(text2, (width / 2 - 25, height / 2 + 100))
        screen.blit(text3, (width / 2 - 85, height / 2 + 50))

        pygame.display.update()

    [i.kill() for i in horizontal_borders]
    [i.kill() for i in vertical_borders]
    [i.kill() for i in collectibles]
    [i.kill() for i in enemies]

    return level_chosen, time_level_started, need_to_start_main_screen, need_to_quit_level


class Hud(pygame.sprite.Sprite):
    """
    Класс информации о счете. Хранит информацию о здоровье, времени, проведенном на уровне, и о очках, заработанных
    за сбор предметов.
    """
    def __init__(self, group, lc, t, hero):
        super().__init__(group)
        self.hero = hero
        self.t = t
        self.lc = lc
        self.font = pygame.font.SysFont('', 250)
        self.text = self.font.render(f"{self.hero.score}", True, (255, 0, 0))
        self.text2 = self.font.render(f"{(pygame.time.get_ticks() - self.t) // 1000}", True,
                                      (255, 255, 0))
        self.text3 = self.font.render(f'{self.hero.hp}hp', True, (0, 255, 0))
        self.rect = pygame.Rect(1, 1, 9999, 9999)

    def upd(self):
        self.text = self.font.render(f"{self.hero.score}p.", True, (255, 0, 0))
        self.text2 = self.font.render(f"{(pygame.time.get_ticks() - self.t) // 1000}/"
                                      f"{self.lc * 120}", True, (255, 255, 0))
        self.text3 = self.font.render(f'{self.hero.hp}hp', True, (0, 255, 0))


def menu(need_to_quit_level, time_level_started, hud):
    """
    Экран меню на Escape. Во время открытого меню время игры корректируется, чтобы пока меню открыто время не
    увеличивалось в hud. В меню есть две опции: вернуться на уровень или выйти в основное меню.
    """
    pygame.mixer.music.stop()
    img = pygame.image.load('data/backgrounds/bg3.png')
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    smallfont = pygame.font.SysFont('Corbel', 35)
    height = screen.get_height()
    text1 = smallfont.render('Quit level', True, color)
    text2 = smallfont.render('Go back', True, color)
    need4 = True
    time_menu_first_opened = pygame.time.get_ticks()
    while need4:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    need_to_quit_level = True
                    need4 = False
                    break
                elif width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 + 50 <= mouse[1] <= height / 2 + 90:
                    pygame.mixer.music.play()
                    need4 = False
                    break
        time_menu_is_open = pygame.time.get_ticks() - time_menu_first_opened
        screen.blit(img, (0, 0))
        mouse = pygame.mouse.get_pos()
        if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 2 - 140, height / 2, 280, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 140, height / 2, 280, 40])
        if width / 2 - 140 <= mouse[0] < width / 2 + 140 and height / 2 + 50 <= mouse[1] <= height / 2 + 90:
            pygame.draw.rect(screen, color_light, [width / 2 - 140, height / 2 + 50, 280, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2 - 140, height / 2 + 50, 280, 40])
        screen.blit(text1, (width / 2 - 50, height / 2))
        screen.blit(text2, (width / 2 - 25, height / 2 + 50))

        pygame.display.update()

    hud.t += time_menu_is_open

    return need_to_quit_level
