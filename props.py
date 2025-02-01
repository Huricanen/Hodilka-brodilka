import pygame
from utils import vertical_borders, horizontal_borders, screen, animations, collectibles


class Wall(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, group):
        super().__init__(group)
        if x2 - x1 <= y2 - y1:
            self.add(vertical_borders)
            self.image = pygame.Surface([x2 - x1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, type, group):
        super().__init__(group)
        self.image = None
        self.w = 75
        self.h = 75
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.w, self.h)

        self.type = type

        if type == 1:
            self.cost = 5
        elif type == 2:
            self.cost = 10
        elif type == 3:
            self.cost = 20

        self.add(collectibles)

        self.type_text = f'{"coin" if self.type == 1 else ("money_bag" if self.type == 2 else "diamond")}'

        self.image = pygame.image.load(f'data/{self.type_text}/1.png')

        self.anim_frames = 30 if type == 2 else 5
        self.anim_index = 0

    def update(self):
        img_index = self.anim_index // self.anim_frames
        if img_index >= len(animations[self.type_text]):
            img_index = 0
            self.anim_index = 0
        self.anim_index += 1

        self.image = pygame.image.load(f'data/{self.type_text}/{animations[self.type_text][img_index]}')
        screen.blit(self.image, self.rect)
