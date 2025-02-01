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
        hero.x = 900
        hero.y = 700
        hero.rect.x = 900
        hero.rect.y = 700
        hero.hp = 20
        hero.update()
        g1 = Wall(-500, 1000, 1920 + 500, 2000, camera_group)
        g2 = Wall(-500, -500, 1920 + 500, 0, camera_group)
        g3 = Wall(-1000, -500, 0, 1080 + 500, camera_group)
        g4 = Wall(1920, -500, 1920 + 1000, 1500, camera_group)
        w = Wall(0, 205, 270, 210, camera_group)
        k = Wall(200, 300, 205, 800, camera_group)
        c = Collectible(150, 40, 1, camera_group)
        f = Collectible(600, 300, 2, camera_group)
        v = Collectible(1000, 80, 3, camera_group)
        Collectible(1700, 400, 3, camera_group)
        Collectible(200, 400, 1, camera_group)
        Enemy(600, 300, 1, 300, hero, camera_group)
        Enemy(800, 120, 1, 300, hero, camera_group)
        Enemy(80, 200, 1, 300, hero, camera_group)
        Enemy(500, 300, 1, 300, hero, camera_group)
    pygame.mixer.music.load('data/level_music.mp3')
    pygame.mixer.music.play()
    t = pygame.time.get_ticks()
    return level, t
