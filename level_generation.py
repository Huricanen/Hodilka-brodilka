import pygame
from props import Wall, Collectible
from enemy import Enemy
from utils import camera_group


def start_level(level, hero, t):
    """
    Функция по генерации уровня. В зависимости от номера уровня генерируются препятствия, предметы для сбора и монстры.
    """
    if level == 1:
        hero.x = 500
        hero.y = 500
        hero.rect.x = 500
        hero.rect.y = 500
        hero.hp = 10
        hero.update()
        g1 = Wall(-500, 1000, 1920 + 500, 2000, camera_group)
        g2 = Wall(-500, -500, 1920 + 500, 0, camera_group)
        g3 = Wall(-1000, -500, 0, 1080 + 500, camera_group)
        g4 = Wall(1920, -500, 1920 + 1000, 1500, camera_group)
        w = Wall(251, 205, 270, 405, camera_group)
        k = Wall(100, 300, 400, 310, camera_group)
        c = Collectible(150, 40, 1, camera_group)
        f = Collectible(300, 40, 2, camera_group)
        v = Collectible(200, 80, 3, camera_group)
        Collectible(50, 400, 1, camera_group)
        Collectible(100, 400, 1, camera_group)
        Collectible(150, 400, 1, camera_group)
        Collectible(200, 400, 1, camera_group)
        Enemy(600, 600, 1, 1000, hero, camera_group)
    if level == 2:
        hero.x = 100
        hero.y = 100
        hero.rect.x = 100
        hero.rect.y = 100
        hero.hp = 20
        hero.update()
        g1 = Wall(-500, 1000, 1920 + 500, 2000, camera_group)
        g2 = Wall(-500, -500, 1920 + 500, 0, camera_group)
        g3 = Wall(-1000, -500, 0, 1080 + 500, camera_group)
        g4 = Wall(1920, -500, 1920 + 1000, 1500, camera_group)

        w = Wall(0, 300, 350, 310, camera_group)
        k = Wall(500, 0, 510, 800, camera_group)
        Wall(500, 500, 1000, 510, camera_group)
        Wall(990, 200, 1000, 500, camera_group)
        Wall(700, 0, 710, 300, camera_group)
        Wall(700, 800, 1500, 810, camera_group)
        Wall(1200, 0, 1210, 800, camera_group)
        Wall(300, 600, 310, 1080, camera_group)
        Wall(700, 650, 710, 800, camera_group)
        Wall(1690, 300, 1700, 800, camera_group)
        Wall(1210, 300, 1700, 310, camera_group)
        Wall(1400, 500, 1700, 510, camera_group)
        s = Collectible(550, 100, 3, camera_group)
        Collectible(100, 900, 3, camera_group)
        Collectible(600, 900, 1, camera_group)
        Collectible(630, 900, 1, camera_group)
        Collectible(660, 900, 1, camera_group)
        Collectible(690, 900, 1, camera_group)
        Collectible(720, 900, 1, camera_group)
        Collectible(800, 900, 1, camera_group)
        Collectible(830, 900, 1, camera_group)
        Collectible(860, 900, 1, camera_group)
        Collectible(890, 900, 1, camera_group)
        Collectible(920, 900, 1, camera_group)
        Collectible(1450, 340, 3, camera_group)
        Collectible(1500, 200, 2, camera_group)
        Collectible(1420, 200, 1, camera_group)
        Collectible(1550, 200, 1, camera_group)
        Enemy(200, 900, 1, 500, hero, camera_group)
        Enemy(700, 400, 1, 150, hero, camera_group)
        Enemy(1730, 900, 1, 600, hero, camera_group)
    pygame.mixer.music.load('data/level_music.mp3')
    pygame.mixer.music.play()
    t = pygame.time.get_ticks()
    return level, t
