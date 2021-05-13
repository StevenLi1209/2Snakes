import pygame
import random
import sys
from pygame.math import Vector2


class Snake:
    def __init__(self):
        m = CELL_N / 2
        self.body = [Vector2(m, m), Vector2(m - 1, m), Vector2(m - 2, m),
                     Vector2(m - 3, m), Vector2(m - 4, m), Vector2(m - 5, m)]
        self.direction = Vector2(0, 0)
        self.new_body = False

        self.head_up = pygame.image.load('snake_graphics/head_up.png')
        self.head_down = pygame.image.load('snake_graphics/head_down.png')
        self.head_right = pygame.image.load('snake_graphics/head_right.png')
        self.head_left = pygame.image.load('snake_graphics/head_left.png')
        self.head = self.head_right

        self.tail_up = pygame.image.load('snake_graphics/tail_up.png')
        self.tail_down = pygame.image.load('snake_graphics/tail_down.png')
        self.tail_right = pygame.image.load('snake_graphics/tail_right.png')
        self.tail_left = pygame.image.load('snake_graphics/tail_left.png')
        self.tail = self.tail_right

        self.body_up = pygame.image.load('snake_graphics/body_up.png')
        self.body_down = pygame.image.load('snake_graphics/body_down.png')
        self.body_right = pygame.image.load('snake_graphics/body_right.png')
        self.body_left = pygame.image.load('snake_graphics/body_left.png')

        self.turn_right = pygame.image.load('snake_graphics/turn_right.png')
        self.turn_left = pygame.image.load('snake_graphics/turn_left.png')
        self.turn_up = pygame.image.load('snake_graphics/turn_up.png')
        self.turn_down = pygame.image.load('snake_graphics/turn_down.png')

    def update_head(self):
        connection = self.body[1] - self.body[0]
        if connection == Vector2(1, 0):
            self.head = self.head_left
        elif connection == Vector2(-1, 0):
            self.head = self.head_right
        elif connection == Vector2(0, 1):
            self.head = self.head_up
        elif connection == Vector2(0, -1):
            self.head = self.head_down

    def update_tail(self):
        length = len(self.body)
        connection = self.body[length - 2] - self.body[length - 1]
        if connection == Vector2(1, 0):
            self.tail = self.tail_right
        elif connection == Vector2(-1, 0):
            self.tail = self.tail_left
        elif connection == Vector2(0, 1):
            self.tail = self.tail_down
        elif connection == Vector2(0, -1):
            self.tail = self.tail_up

    def update_body(self, prev, nxt, body_rect):
        if prev.x == nxt.x and prev.y > nxt.y:
            MAIN_WINDOW.blit(self.body_up, body_rect)
        elif prev.x == nxt.x and prev.y < nxt.y:
            MAIN_WINDOW.blit(self.body_down, body_rect)
        elif prev.y == nxt.y and prev.x > nxt.x:
            MAIN_WINDOW.blit(self.body_left, body_rect)
        elif prev.y == nxt.y and prev.x < nxt.x:
            MAIN_WINDOW.blit(self.body_right, body_rect)
        else:
            if prev.x == -1 and nxt.y == -1 or prev.y == -1 and nxt.x == -1:
                MAIN_WINDOW.blit(self.turn_left, body_rect)
            elif prev.x == -1 and nxt.y == 1 or prev.y == 1 and nxt.x == -1:
                MAIN_WINDOW.blit(self.turn_down, body_rect)
            elif prev.x == 1 and nxt.y == -1 or prev.y == -1 and nxt.x == 1:
                MAIN_WINDOW.blit(self.turn_up, body_rect)
            elif prev.x == 1 and nxt.y == 1 or prev.y == 1 and nxt.x == 1:
                MAIN_WINDOW.blit(self.turn_right, body_rect)

    def place_body(self):
        self.update_head()
        self.update_tail()
        for index, body_part in enumerate(self.body):
            body_rect = pygame.Rect(body_part.x * CELL_S, body_part.y * CELL_S,
                                    CELL_S, CELL_S)
            if index == 0:
                MAIN_WINDOW.blit(self.head, body_rect)
            elif index == len(self.body) - 1:
                MAIN_WINDOW.blit(self.tail, body_rect)
            else:
                prev = self.body[index + 1] - body_part
                nxt = self.body[index - 1] - body_part
                self.update_body(prev, nxt, body_rect)

    def move_snake(self):
        if self.new_body:
            new_body = self.body[:]
            new_body.insert(0, new_body[0] + self.direction)
            self.body = new_body
            self.new_body = False
        else:
            copy = self.body[:-1]
            copy.insert(0, copy[0] + self.direction)
            self.body = copy

    def restart(self):
        m = CELL_N / 2
        self.body = [Vector2(m, m), Vector2(m - 1, m), Vector2(m - 2, m),
                     Vector2(m - 3, m), Vector2(m - 4, m), Vector2(m - 5, m)]
        self.direction = Vector2(0, 0)


class Food:
    def __init__(self):
        self.x = random.randint(0, CELL_N - 1)
        self.y = random.randint(0, CELL_N - 1)
        self.pos = Vector2(self.x, self.y)

    def place_food(self):
        food_rect = pygame.Rect(self.pos.x * CELL_S, self.pos.y * CELL_S,
                                CELL_S, CELL_S)
        MAIN_WINDOW.blit(food, food_rect)

    def new_position(self):
        self.__init__()


def place_background():
    c1 = (90, 155, 0)
    c2 = (159, 231, 122)
    c3 = (123, 190, 84)
    for row in range(CELL_N):
        if row % 2 == 0:
            for i in range(0, CELL_N, 2):
                block_rect = pygame.Rect(i * CELL_S, row * CELL_S,
                                         CELL_S, CELL_S)
                pygame.draw.rect(MAIN_WINDOW, c1, block_rect)
        else:
            for i in range(1, CELL_N, 2):
                block_rect = pygame.Rect(i * CELL_S, row * CELL_S,
                                         CELL_S, CELL_S)
                pygame.draw.rect(MAIN_WINDOW, c2, block_rect)
                block_rect = pygame.Rect(i * CELL_S, (row - 1) * CELL_S,
                                         CELL_S, CELL_S)
                pygame.draw.rect(MAIN_WINDOW, c3, block_rect)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.high_score = 0
        for block in self.snake.body:
            if block == self.food.pos:
                self.__init__()

    def update(self):
        self.snake.move_snake(), self.check_eat(), self.check_hit()

    def place_elements(self):
        place_background()
        self.food.place_food()
        self.snake.place_body()
        self.place_score()
        if self.snake.direction == Vector2(0, 0):
            msg = 'Press   any   arrow   key   to   start!!!'
            msg_visual = msg_font.render(msg, True, (255, 255, 255))
            MAIN_WINDOW.blit(msg_visual, ((CELL_S * CELL_N) / 2 - 230,
                                          ((CELL_S * CELL_N) / 2 - 45)))

    def check_eat(self):
        if self.food.pos == self.snake.body[0]:
            self.food.new_position()
            self.snake.new_body = True
            for block in self.snake.body:
                if block == self.food.pos:
                    self.food.new_position()

    def check_hit(self):
        for body in self.snake.body[1:]:
            if body == self.snake.body[0]:
                if (len(self.snake.body) - 6) > self.high_score:
                    self.high_score = len(self.snake.body) - 6
                self.game_over()
        if not 0 <= self.snake.body[0].x < CELL_N or \
                not 0 <= self.snake.body[0].y < CELL_N:
            if (len(self.snake.body) - 6) > self.high_score:
                self.high_score = len(self.snake.body) - 6
            self.game_over()

    def game_over(self):
        self.snake.restart()

    def place_score(self):
        board = pygame.Rect(0, (CELL_N * CELL_S), (CELL_N * CELL_S), 60)
        pygame.draw.rect(MAIN_WINDOW, (255, 255, 255), board)
        score = 'Score: ' + f'{len(self.snake.body) - 6}'
        scoreboard = score_font.render(score, True, (0, 0, 0))
        MAIN_WINDOW.blit(scoreboard, (20, (CELL_S * CELL_N + 8)))

        high_score = 'High Score: ' + f'{self.high_score}'
        high_board = score_font.render(high_score, True, (0, 0, 0))
        MAIN_WINDOW.blit(high_board, ((CELL_S * CELL_N - 210),
                                      (CELL_S * CELL_N + 8)))


pygame.init()

CELL_S = 40
CELL_N = 16

MAIN_WINDOW = pygame.display.set_mode((CELL_N * CELL_S, CELL_N * CELL_S + 60))
clock = pygame.time.Clock()
food = pygame.image.load('snake_graphics/candy.png')
score_font = pygame.font.Font('Fonts/pixelated.ttf', 35)
msg_font = pygame.font.Font('Fonts/pixelated.ttf', 35)
game = Main()


def new_speed(speed=150) -> int:
    if len(game.snake.body) - 6 >= 5:
        speed = 165
    if len(game.snake.body) - 6 >= 15:
        speed = 180
    if len(game.snake.body) - 6 >= 25:
        speed = 190
    if len(game.snake.body) - 6 >= 40:
        speed = 200
    return speed


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, new_speed())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.snake.direction.y != 1:
                game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN and game.snake.direction.y != -1:
                game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT and game.snake.direction.x != 1:
                game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT and game.snake.direction.x != -1:
                game.snake.direction = Vector2(1, 0)

    new_speed()
    MAIN_WINDOW.fill((110, 180, 0))
    game.place_elements()
    pygame.display.update()
    clock.tick(60)
