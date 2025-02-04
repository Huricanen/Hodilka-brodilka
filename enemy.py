import pygame

from utils import enemies, screen, animations, hurt, hit


class Enemy(pygame.sprite.Sprite):
    """
    Класс врага. У врага есть прямоугольник его поле зрения и прямоугольник где он начинает наносить урон герою.
    Урон можно менять, время для нанесения урона можно менять. В будущем рассматривается несколько видов врагов.
    """
    def __init__(self, x, y, type, r, hero, group):
        super().__init__(group)
        self.x = x
        self.y = y
        self.height = 64
        self.width = 64

        self.hero = hero

        self.type = type
        self.type_text = 'bat' if type == 1 else None

        self.add(enemies)

        self.anim_index = 0
        self.anim_frames = 15

        self.r = r
        self.rect = pygame.Rect(x, y, self.height, self.width)
        self.watch_rect = pygame.Rect(x - self.r, y - self.r, self.height + self.r * 2, self.width + self.r * 2)

        self.moving = False

        self.v = 1

        self.started_colliding = 0
        self.time_to_damage = 0.5
        self.damage = 1

        self.image = pygame.image.load(f'data/enemies/{"bat" if type == 1 else None}/1.png')

    def update(self):
        x_direction = None
        y_direction = None
        if self.watch_rect.colliderect(self.hero.rect):
            if self.hero.rect.centerx > self.rect.centerx:
                x_direction = self.v
            elif self.hero.rect.centerx < self.rect.centerx:
                x_direction = -self.v
            else:
                x_direction = 0
            if self.hero.rect.centery > self.rect.centery:
                y_direction = self.v
            elif self.hero.rect.centery < self.rect.centery:
                y_direction = -self.v
            else:
                y_direction = 0
            self.rect.x += x_direction
            self.rect.y += y_direction
            self.watch_rect = pygame.Rect(self.rect.x - self.r, self.rect.y - self.r, self.height + self.r * 2,
                                          self.width + self.r * 2)

        if self.rect.colliderect(self.hero.rect):
            if not self.started_colliding:
                self.started_colliding = pygame.time.get_ticks()
            if (pygame.time.get_ticks() - self.started_colliding) / 1000 > self.time_to_damage:
                self.started_colliding = 0
                self.hero.hp -= self.damage
                hit.play()
                hurt.play()
        else:
            self.started_colliding = 0

        img_index = self.anim_index // self.anim_frames
        if img_index >= len(animations[self.type_text]):
            img_index = 0
            self.anim_index = 0
        self.anim_index += 1

        self.image = pygame.image.load(f'data/enemies/{self.type_text}/{animations[self.type_text][img_index]}')
        screen.blit(self.image, self.rect)
