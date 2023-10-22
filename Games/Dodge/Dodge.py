import pygame
import time
import random

pygame.init()

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dodge")

x_pos, y_pos = map(lambda x: x//2, screen.get_size())

playing = True
clock = pygame.time.Clock()


class Box:
    def __init__(self, x_pos, y_pos, width, height, color, speed, image):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.image = image

    def draw(self, screen):

        pygame.draw.rect(screen, self.color, [
            self.x_pos, self.y_pos, self.width, self.height], 0)

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos,
                           self.width, self.height)


class Player(Box):
    def __init__(self, x_pos, y_pos, width, height, color, speed, image):
        super().__init__(x_pos, y_pos, width, height, color, speed, image)

    def move(self, pressed, screen_size):
        if pressed[pygame.K_UP] and (self.y_pos > 0):
            self.y_pos -= self.speed
        if pressed[pygame.K_DOWN] and (self.y_pos < screen_size[1] - self.height):
            self.y_pos += self.speed
        if pressed[pygame.K_LEFT] and (self.x_pos > 0):
            self.x_pos -= self.speed
        if pressed[pygame.K_RIGHT] and self.x_pos < screen_size[0] - self.width:
            self.x_pos += self.speed


class Enemy(Box):
    def __init__(self, screen_size, width, height, color, speed, image):

        spawn_points = [[0, random.randint(0, 600)], [screen_size[0] - width, random.randint(
            0, 600)], [random.randint(0, 800), 0], [random.randint(0, 800), screen_size[1] - height]]
        spawn_point = random.choice(spawn_points)

        super().__init__(*spawn_point, width, height, color, speed, image)

    def chasing_player(self, player):
        if self.x_pos < player.x_pos:
            self.x_pos += self.speed
        if self.x_pos > player.x_pos:
            self.x_pos -= self.speed
        if self.y_pos < player.y_pos:
            self.y_pos += self.speed
        if self.y_pos > player.y_pos:
            self.y_pos -= self.speed


def check_collision(player, enemy):
    if abs(player.x_pos - enemy.x_pos) < player.width and abs(player.y_pos - enemy.y_pos) < player.height:
        return True
    return False


def write(screen, string, font, size, centerx, centery, color):
    end_font = pygame.font.SysFont(font, size, True, False)
    text = end_font.render(string, True, color)
    text_box = text.get_rect()
    text_box.centerx = centerx
    text_box.centery = centery

    screen.blit(text, text_box)


player = Player(x_pos-25, y_pos-25, 20, 20, BLUE, 7, "pngwing.com.png")

enemies = []
for i in range(3):
    enemies.append(Enemy(screen.get_size(), 20, 20, GREEN, 3, "pngegg.png"))
# enemy = Enemy(screen.get_size(), 50, 50, GREEN, 7, "pngegg.png")
start_time = time.time()

enemy_spawn_time = 2
enemy_spawn_count = 0

while playing:

    clock.tick(60)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        playing = False

    player.move(pygame.key.get_pressed(), screen.get_size())

    screen.fill(WHITE)

    player.draw(screen)

    if time.time() - start_time > enemy_spawn_time + enemy_spawn_count:
        enemies.append(Enemy(screen.get_size(), 20,
                       20, GREEN, 3, "pngegg.png"))
        enemy_spawn_count += 1

    


    for enemy in enemies:
        enemy.chasing_player(player)
        enemy.draw(screen)

        # if check_collision(player, enemy):
        collide = pygame.Rect.colliderect(player.get_rect(), enemy.get_rect())

        if collide:
            write(screen, "END", "arial", 100,
                  size[0]/2, size[1]/2, BLACK)
            playing = False
    
    survival_time = str(round(time.time()-start_time, 2))
    write(screen, survival_time, "arial",
                  30, round(size[0] / 2), 10, BLACK)

    pygame.display.update()

# time.sleep(1)
pygame.quit()
