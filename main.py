import pygame
import gif_pygame
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

im = Image.open('data/Анимации_для_врага1.png')
for x in range(4):
    part = im.crop((x * 64, 0, (x + 1) * 64, 64))
    part.save(f'data/enemies/bat/{x + 1}.png')
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
                     '8_10.png'],
    'coin': ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png'],
    'money_bag': ['1.png', '2.png', '3.png', '4.png'],
    'diamond': ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png'],
    'bat': ['1.png', '2.png', '3.png', '4.png']
}


# класс главного героя
class Hero(pygame.sprite.Sprite):
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


class Hud(pygame.sprite.Sprite):
    def __init__(self, group, level):
        super().__init__(group)
        self.font = pygame.font.SysFont('Serif', 250)
        self.text = self.font.render(f"{main_character.score}/{level_chosen * 120}",
                                     True, (255, 0, 0))
        self.text2 = self.font.render(f"{(pygame.time.get_ticks() - time_level_started) // 1000}", True,
                                      (255, 255, 0))
        self.text3 = self.font.render(f'{main_character.hp}', True, (0, 255, 0))
        self.rect = pygame.Rect(1, 1, 9999, 9999)

    def upd(self):
        self.text = self.font.render(f"{main_character.score}", True, (255, 0, 0))
        self.text2 = self.font.render(f"{(pygame.time.get_ticks() - time_level_started) // 1000}/"
                                      f"{level_chosen * 120}", True, (255, 255, 0))
        self.text3 = self.font.render(f'{main_character.hp}', True, (0, 255, 0))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, type, group):
        super().__init__(group)
        self.x = x
        self.y = y
        self.height = 64
        self.width = 64

        self.type = type
        self.type_text = 'bat' if type == 1 else None

        self.add(enemies)

        self.anim_index = 0
        self.anim_frames = 15

        self.r = 200
        self.rect = pygame.Rect(x, y, self.height, self.width)
        self.watch_rect = pygame.Rect(x - self.r, y - self.r, self.height + self.r * 2, self.width + self.r * 2)

        self.moving = False

        self.v = 1

        self.started_colliding = 0
        self.time_to_damage = 0.5
        self.damage = 1

        self.image = pygame.image.load(f'data/enemies/{'bat' if type == 1 else None}/1.png')

    def update(self):
        x_direction = None
        y_direction = None
        if self.watch_rect.colliderect(main_character.rect):
            if main_character.rect.centerx > self.rect.centerx:
                x_direction = self.v
            else:
                x_direction = -self.v
            if main_character.rect.centery > self.rect.centery:
                y_direction = self.v
            else:
                y_direction = -self.v
            self.rect.x += x_direction
            self.rect.y += y_direction
            self.watch_rect = pygame.Rect(self.rect.x - self.r, self.rect.y - self.r, self.height + self.r * 2,
                                          self.width + self.r * 2)

        if self.rect.colliderect(main_character.rect):
            if not self.started_colliding:
                self.started_colliding = pygame.time.get_ticks()
            if (pygame.time.get_ticks() - self.started_colliding) / 1000 > self.time_to_damage:
                self.started_colliding = 0
                main_character.hp -= self.damage
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

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        # ground
        self.ground_surf = pygame.image.load('data/ground.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

        # camera speed
        self.keyboard_speed = 5
        self.mouse_speed = 0.2

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):
        self.center_target_camera(player)

        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, ground_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            if sprite.image is None:
                sprite.upd()
                self.display_surface.blit(sprite.text, (10, 850))
                self.display_surface.blit(sprite.text2, (960, 850))
                self.display_surface.blit(sprite.text3, (500, 850))
            else:
                self.display_surface.blit(sprite.image, offset_pos)


def start_screen():
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
                    choose_level()
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


def choose_level():
    global need1, level_chosen, time_level_started
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
    need = True

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

    time_level_started = pygame.time.get_ticks()
    start_level(level_chosen)


def finish():
    global need_to_start_main_screen, need_to_quit_level, delay_at_the_end
    time_level_finished = pygame.time.get_ticks()
    while (pygame.time.get_ticks() - time_level_finished) // 1000 != delay_at_the_end and not need_to_quit_level:
        pass
    pygame.mixer.music.stop()
    pygame.mixer.music.load('data/main_menu_theme.mp3')
    pygame.mixer.music.play()
    img = pygame.image.load('data/backgrounds/bg4.png')
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    smallfont = pygame.font.SysFont('Corbel', 35)
    height = screen.get_height()
    text1 = smallfont.render('Congatulations!!!', True, color)
    text2 = smallfont.render('quit', True, color)
    text3 = smallfont.render(f'Your score: {main_character.score}', True, (255, 0, 0))
    main_character.score = 0
    time_level_started = None
    need_to_start_main_screen = False
    need3 = True
    need_to_quit_level = False

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

    start_screen()


def menu():
    global need_to_quit_level, time_level_started
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

    time_level_started += time_menu_is_open


def start_level(level):
    if level == 1:
        main_character.x = 500
        main_character.y = 500
        main_character.rect.x = 500
        main_character.rect.y = 500
        main_character.hp = 10
        main_character.update()
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
        Enemy(600, 600, 1, camera_group)
    pygame.mixer.music.load('data/level_music.mp3')
    pygame.mixer.music.play()


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('Ходилка-бродилка')
    size = w1, h1 = 1920, 1080
    screen = pygame.display.set_mode(size)

    time_level_started = None
    level_chosen = None
    need_to_quit_level = False

    delay_at_the_end = 1

    running = True
    fps = 60
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))

    camera_group = CameraGroup()

    main_character = Hero(x=500, y=500, h=110, w=130, group=camera_group)

    all_sprites = pygame.sprite.Group()

    collectibles = pygame.sprite.Group()

    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()

    enemies = pygame.sprite.Group()

    pygame.mixer.init()
    pygame.mixer.music.load('data/main_menu_theme.mp3')
    pygame.mixer.music.play()
    hit = pygame.mixer.Sound('data/hit.wav')
    hurt = pygame.mixer.Sound('data/hurt.wav')
    start_screen()

    hud = Hud(camera_group, level_chosen)

    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif time_level_started is not None and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                menu()
                if need_to_quit_level:
                    finish()
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
        if ((pygame.time.get_ticks() - time_level_started) // 1000 > 120 or len(collectibles.sprites()) == 0 or
                main_character.hp == 0):
            finish()
        collectibles.update()
        main_character.update()
        enemies.update()
        camera_group.custom_draw(main_character)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
