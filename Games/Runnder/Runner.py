import pygame

pygame.init()

SIZE = [300, 600]
SCREEN = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Runner")

clock = pygame.time.Clock()

blockSize = 100

road = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]


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


class Block(Box):
    def __init__(self, x_pos, y_pos, width, height, color, speed, image):
        super().__init__(x_pos, y_pos, width, height, color, speed, image)


yPos = 0

playing = True
while playing:

    clock.tick(60)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        playing = False

    SCREEN.fill((255, 255, 255))
    yPos += 5

    for i, bs in enumerate(road):
        for j, b in enumerate(bs):
            if b:

                pygame.draw.rect(SCREEN, (0, 0, 0), [
                    j * blockSize, yPos - i * blockSize, blockSize, blockSize], 0)

    pygame.display.update()

pygame.quit()
