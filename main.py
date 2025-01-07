import pygame
from PIL import Image

im = Image.open('data/Анимации_для_главного_героя.png')
for y in range(8):
    for x in range(10):
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
class Hero:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.height = h
        self.width = w

        self.anim_index = 0
        self.anim_frames = 60

        self.rect = pygame.Rect(x, y, height, width)

        self.facing = 'down'
        self.moving = False

        self.v = 2

    def draw(self):
        if self.moving:
            self.anim_frames = 10
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

            self.rect = pygame.Rect(self.x, self.y, height, width)

            screen.blit(pygame.image.load(f'data/{animations[f'moving_{self.facing}'][img_index]}'), self.rect)
        else:
            self.anim_frames = 60
            img_index = self.anim_index // self.anim_frames
            if img_index >= len(animations[f'idle_{self.facing}']):
                img_index = 0
                self.anim_index = 0
            self.anim_index += 1

            screen.blit(pygame.image.load(f'data/{animations[f'idle_{self.facing}'][img_index]}'), self.rect)


class Wall:
    def __init__(self):
        pass


class Enemy:
    def __init__(self):
        pass


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('Ходилка-бродилка')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))

    main_character = Hero(x=50, y=50, h=130, w=120)

    all_sprites = pygame.sprite.Group()

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

        main_character.draw()
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
