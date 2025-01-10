import pygame
from PIL import Image

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
                     '8_10.png']
}


# класс главного героя
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, h, w, *groups):
        super().__init__(*groups)
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
            if self.facing == 'down':
                self.y += self.v
            elif self.facing == 'up':
                self.y -= self.v
            elif self.facing == 'right':
                self.x += self.v
            elif self.facing == 'left':
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


class Wall(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
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


class Enemy:
    def __init__(self):
        pass


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('Ходилка-бродилка')
    size = w1, h1 = 600, 600
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))

    main_character = Hero(x=30, y=30, h=105, w=130)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(main_character)

    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()

    w = Wall(251, 205, 270, 405)
    k = Wall(100, 300, 400, 310)

    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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

        horizontal_borders.draw(screen)
        vertical_borders.draw(screen)
        all_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
