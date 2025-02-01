import pygame
from utils import horizontal_borders, vertical_borders, collectibles, animations, screen

class Hero(pygame.sprite.Sprite):
    """
    Класс героя. Содержит в себе все параметры героя (здоровье, скорость, направление и др.). Здесь реализована вся
    физика героя с предметами для сбора и стенами. Герой имеет особую возможность обходить стены: эта возможность
    зависит от коэффициента в классе героя.
    """
    def __init__(self, x, y, h, w, group):
        super().__init__(group)
        self.x = x
        self.y = y
        self.height = h
        self.width = w

        self.anim_index = 0
        self.anim_frames = 60

        self.rect = pygame.Rect(x, y, self.height, self.width)

        self.facing = 'down'
        self.moving = False

        self.v = 2

        self.image = pygame.image.load('data/1_1.png')

        self.koef_angle = 9

        self.score = 0

        self.hp = 10

    def update(self):
        rects_h = [i.rect for i in horizontal_borders]
        rects_v = [i.rect for i in vertical_borders]
        collision_index_h = self.rect.collidelist(rects_h)
        collision_index_v = self.rect.collidelist(rects_v)
        if self.moving:
            if collision_index_h != -1:
                rect = rects_h[collision_index_h]
                rect_mid_y = rect.y + rect.h // 2
                rect_mid_x = rect.x + rect.w // 2
                char_mid_y = self.rect.y + self.rect.h // 2
                char_mid_x = self.rect.x + self.rect.w // 2
                if (char_mid_y > rect_mid_y and char_mid_x in range(
                        rect.x + self.rect.w // self.koef_angle, rect.x + rect.w - self.rect.w // self.koef_angle)):
                    self.y += self.v
                elif char_mid_y < rect_mid_y and char_mid_x in range(
                        rect.x + self.rect.w // self.koef_angle, rect.x + rect.w - self.rect.w // self.koef_angle):
                    self.y -= self.v
                else:
                    if char_mid_x > rect_mid_x:
                        self.x += self.v
                    elif char_mid_x < rect_mid_x:
                        self.x -= self.v
            if collision_index_v != -1:
                rect = rects_v[collision_index_v]
                rect_mid_y = rect.y + rect.h // 2
                rect_mid_x = rect.x + rect.w // 2
                char_mid_y = self.rect.y + self.rect.h // 2
                char_mid_x = self.rect.x + self.rect.w // 2
                if char_mid_x > rect_mid_x and char_mid_y in range(
                        rect.y + self.rect.h // self.koef_angle, rect.y + rect.h - self.rect.h // self.koef_angle):
                    self.x += self.v
                elif char_mid_x < rect_mid_x and char_mid_y in range(
                        rect.y + self.rect.h // self.koef_angle, rect.y + rect.h - self.rect.h // self.koef_angle):
                    self.x -= self.v
                else:
                    if char_mid_y > rect_mid_y:
                        self.y += self.v
                    elif char_mid_y < rect_mid_y:
                        self.y -= self.v
        rects_coll = [i.rect for i in collectibles]
        collision_index_coll = self.rect.collidelist(rects_coll)
        if collision_index_coll != -1:
            self.score += collectibles.sprites()[collision_index_coll].cost
            collectibles.sprites()[collision_index_coll].kill()

        if self.moving:
            if self.v == 2:
                self.anim_frames = 10
            elif self.v == 4:
                self.anim_frames = 5
            img_index = self.anim_index // self.anim_frames
            if img_index >= len(animations[f'moving_{self.facing}']):
                img_index = 0
                self.anim_index = 0
            self.anim_index += 1
            if 'down' in self.facing:
                self.y += self.v
            if 'up' in self.facing:
                self.y -= self.v
            if 'right' in self.facing:
                self.x += self.v
            if 'left' in self.facing:
                self.x -= self.v

            self.rect = pygame.Rect(self.x, self.y, self.height, self.width)

            self.image = pygame.image.load(f'data/{animations[f'moving_{self.facing}'][img_index]}')
            screen.blit(self.image, self.rect)
        else:
            self.anim_frames = 60
            img_index = self.anim_index // self.anim_frames
            if img_index >= len(animations[f'idle_{self.facing}']):
                img_index = 0
                self.anim_index = 0
            self.anim_index += 1

            self.image = pygame.image.load(f'data/{animations[f'idle_{self.facing}'][img_index]}')
            screen.blit(self.image, self.rect)
