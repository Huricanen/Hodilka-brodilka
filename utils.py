import pygame
from camera import CameraGroup

animations = {
    'idle_down': ['1_1.png', '1_2.png', '1_3.png'],
    'idle_left': ['2_1.png', '2_2.png', '2_3.png'],
    'idle_up': ['3_1.png'],
    'idle_right': ['4_1.png', '4_2.png', '4_3.png'],
    'moving_down': ['5_1.png', '5_2.png', '5_3.png', '5_4.png', '5_5.png', '5_6.png', '5_7.png', '5_8.png', '5_9.png',
                    '5_10.png'],
    'moving_left': ['6_1.png', '6_2.png', '6_3.png', '6_4.png', '6_5.png', '6_6.png', '6_7.png', '6_8.png', '6_9.png',
                    '6_10.png'],
    'moving_up': ['7_1.png', '7_2.png', '7_3.png', '7_4.png', '7_5.png', '7_6.png', '7_7.png', '7_8.png', '7_9.png',
                  '7_10.png'],
    'moving_right': ['8_1.png', '8_2.png', '8_3.png', '8_4.png', '8_5.png', '8_6.png', '8_7.png', '8_8.png', '8_9.png',
                     '8_10.png'],
    'coin': ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png'],
    'money_bag': ['1.png', '2.png', '3.png', '4.png'],
    'diamond': ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png'],
    'bat': ['1.png', '2.png', '3.png', '4.png']
}

pygame.init()
pygame.display.set_caption('Ходилка-бродилка')
size = w1, h1 = 1920, 1080
screen = pygame.display.set_mode(size)

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
enemies = pygame.sprite.Group()

hit = pygame.mixer.Sound('data/hit.wav')
hurt = pygame.mixer.Sound('data/hurt.wav')

camera_group = CameraGroup()
