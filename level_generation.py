import pygame
from props import Wall, Collectible
from enemy import Enemy
from utils import camera_group


def start_level(level, hero, t):
    """
    Функция по генерации уровня. В зависимости от номера уровня генерируются препятствия, предметы для сбора и монстры.
    """
    if level == 1:
        hero.x = 1920 // 2
        hero.y = 1080 // 2
        hero.rect.x = 1920 // 2
        hero.rect.y = 1080 // 2
        hero.hp = 50
        hero.update()
        g1 = Wall(-500, 1000, 1920 + 500, 2000, camera_group)
        g2 = Wall(-500, -500, 1920 + 500, 0, camera_group)
        g3 = Wall(-1000, -500, 0, 1080 + 500, camera_group)
        g4 = Wall(1920, -500, 1920 + 1000, 1500, camera_group)
        w = Wall(500, 200, 800, 210, camera_group)
        k = Wall(1920 - 800, 200, 1920 - 500, 210, camera_group)
        w = Wall(500, 1080 - 210 - 50, 800, 1080 - 200 - 50, camera_group)
        k = Wall(1920 - 800, 1080 - 210 - 50, 1920 - 500, 1080 - 200 - 50, camera_group)
        w = Wall(500, 200, 510, 400, camera_group)
        k = Wall(1920 - 510, 200, 1920 - 500, 400, camera_group)
        w = Wall(500, 1080 - 400 - 50, 510, 1080 - 200 - 50, camera_group)
        k = Wall(1920 - 510, 1080 - 400 - 50, 1920 - 500, 1080 - 200 - 50, camera_group)
        c = Collectible(1920 - 200, 1080 - 200, 3, camera_group)
        f = Collectible(1920 - 200, 100, 3, camera_group)
        v = Collectible(100, 100, 3, camera_group)
        v = Collectible(100, 1080 - 200, 3, camera_group)
        boss = Enemy(1920 - 200, 100, 1, 2000, hero, camera_group)
        boss.damage = 5
        boss.time_to_damage = 0.2
        boss.v = 1
        boss1 = Enemy(1920 - 200, 1080 - 200, 1, 2000, hero, camera_group)
        boss1.damage = 5
        boss1.time_to_damage = 0.2
        boss1.v = 1
        boss2 = Enemy(100, 100, 1, 2000, hero, camera_group)
        boss2.damage = 5
        boss2.time_to_damage = 0.2
        boss2.v = 1
        boss3 = Enemy(100, 1080 - 200, 1, 2000, hero, camera_group)
        boss3.damage = 5
        boss3.time_to_damage = 0.2
        boss3.v = 1
    if level == 2:
        hero.x = 100
        hero.y = 100
        hero.rect.x = 100
        hero.rect.y = 100
        hero.hp = 10
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
