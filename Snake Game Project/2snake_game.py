import pygame
import random
import sys
from pygame.math import Vector2


class OneSnake:
    def __init__(self):
        self.body = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7),
                     Vector2(2, 7), Vector2(1, 7)]
        self.direction = Vector2(0, 0)
        self.new_body = False

        self.head_up = pygame.image.load('2Snake_graphics/head_up.png')
        self.head_down = pygame.image.load('2Snake_graphics/head_down.png')
        self.head_right = pygame.image.load('2Snake_graphics/head_right.png')
        self.head_left = pygame.image.load('2Snake_graphics/head_left.png')
        self.head = self.head_right

        self.tail_up = pygame.image.load('2Snake_graphics/tail_up.png')
        self.tail_down = pygame.image.load('2Snake_graphics/tail_down.png')
        self.tail_right = pygame.image.load('2Snake_graphics/tail_right.png')
        self.tail_left = pygame.image.load('2Snake_graphics/tail_left.png')
        self.tail = self.tail_right

        self.body_up = pygame.image.load('2Snake_graphics/body_up.png')
        self.body_down = pygame.image.load('2Snake_graphics/body_down.png')
        self.body_right = pygame.image.load('2Snake_graphics/body_right.png')
        self.body_left = pygame.image.load('2Snake_graphics/body_left.png')

        self.turn_right = pygame.image.load('2Snake_graphics/turn_right.png')
        self.turn_left = pygame.image.load('2Snake_graphics/turn_left.png')
        self.turn_up = pygame.image.load('2Snake_graphics/turn_up.png')
        self.turn_down = pygame.image.load('2Snake_graphics/turn_down.png')

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
        self.body = [Vector2(5, 7), Vector2(4, 7), Vector2(3, 7),
                     Vector2(2, 7), Vector2(1, 7)]
        self.direction = Vector2(0, 0)


class TwoSnake:
    def __init__(self):
        self.body = [Vector2(5, 11), Vector2(4, 11), Vector2(3, 11),
                     Vector2(2, 11), Vector2(1, 11)]
        self.direction = Vector2(0, 0)
        self.new_body = False

        self.head_u = pygame.image.load('2Snake_graphics/head_up copy.png')
        self.head_d = pygame.image.load('2Snake_graphics/head_down copy.png')
        self.head_r = pygame.image.load('2Snake_graphics/head_right copy.png')
        self.head_l = pygame.image.load('2Snake_graphics/head_left copy.png')
        self.head = self.head_r

        self.tail_u = pygame.image.load('2Snake_graphics/tail_up copy.png')
        self.tail_d = pygame.image.load('2Snake_graphics/tail_down copy.png')
        self.tail_r = pygame.image.load('2Snake_graphics/tail_right copy.png')
        self.tail_l = pygame.image.load('2Snake_graphics/tail_left copy.png')
        self.tail = self.tail_r

        self.body_u = pygame.image.load('2Snake_graphics/body_up copy.png')
        self.body_d = pygame.image.load('2Snake_graphics/body_down copy.png')
        self.body_r = pygame.image.load('2Snake_graphics/body_right copy.png')
        self.body_l = pygame.image.load('2Snake_graphics/body_left copy.png')

        self.turn_r = pygame.image.load('2Snake_graphics/turn_right copy.png')
        self.turn_l = pygame.image.load('2Snake_graphics/turn_left copy.png')
        self.turn_u = pygame.image.load('2Snake_graphics/turn_up copy.png')
        self.turn_d = pygame.image.load('2Snake_graphics/turn_down copy.png')

    def update_head(self):
        connection = self.body[1] - self.body[0]
        if connection == Vector2(1, 0):
            self.head = self.head_l
        elif connection == Vector2(-1, 0):
            self.head = self.head_r
        elif connection == Vector2(0, 1):
            self.head = self.head_u
        elif connection == Vector2(0, -1):
            self.head = self.head_d

    def update_tail(self):
        length = len(self.body)
        connection = self.body[length - 2] - self.body[length - 1]
        if connection == Vector2(1, 0):
            self.tail = self.tail_r
        elif connection == Vector2(-1, 0):
            self.tail = self.tail_l
        elif connection == Vector2(0, 1):
            self.tail = self.tail_d
        elif connection == Vector2(0, -1):
            self.tail = self.tail_u

    def update_body(self, prev, nxt, body_rect):
        if prev.x == nxt.x and prev.y > nxt.y:
            MAIN_WINDOW.blit(self.body_u, body_rect)
        elif prev.x == nxt.x and prev.y < nxt.y:
            MAIN_WINDOW.blit(self.body_d, body_rect)
        elif prev.y == nxt.y and prev.x > nxt.x:
            MAIN_WINDOW.blit(self.body_l, body_rect)
        elif prev.y == nxt.y and prev.x < nxt.x:
            MAIN_WINDOW.blit(self.body_r, body_rect)
        else:
            if prev.x == -1 and nxt.y == -1 or prev.y == -1 and nxt.x == -1:
                MAIN_WINDOW.blit(self.turn_l, body_rect)
            elif prev.x == -1 and nxt.y == 1 or prev.y == 1 and nxt.x == -1:
                MAIN_WINDOW.blit(self.turn_d, body_rect)
            elif prev.x == 1 and nxt.y == -1 or prev.y == -1 and nxt.x == 1:
                MAIN_WINDOW.blit(self.turn_u, body_rect)
            elif prev.x == 1 and nxt.y == 1 or prev.y == 1 and nxt.x == 1:
                MAIN_WINDOW.blit(self.turn_r, body_rect)

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
        self.body = [Vector2(5, 11), Vector2(4, 11), Vector2(3, 11),
                     Vector2(2, 11), Vector2(1, 11)]
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
        self.one = OneSnake()
        self.two = TwoSnake()
        self.food1 = Food()
        self.food2 = Food()
        self.high_score = 0
        for block in self.one.body:
            if block == self.food1.pos:
                self.food1.__init__()
            elif block == self.food2.pos:
                self.food2.__init__()
        for block in self.two.body:
            if block == self.food1.pos:
                self.food1.__init__()
            elif block == self.food2.pos:
                self.food2.__init__()

    def update(self):
        self.one.move_snake(), self.one_check_hit(), self.check_eat(),
        self.two.move_snake(), self.two_check_hit()

    def place_elements(self):
        place_background()
        self.food1.place_food()
        self.food2.place_food()
        self.one.place_body()
        self.two.place_body()
        self.place_score()
        self.winner_text()
        if self.one.direction == Vector2(0, 0) and \
                self.two.direction == Vector2(0, 0):
            msg = 'Press   an   arrow   together   to   start!!!'
            msg_visual = msg_font.render(msg, True, (255, 255, 255))
            MAIN_WINDOW.blit(msg_visual, ((CELL_S * CELL_N) / 2 - 265,
                                          ((CELL_S * CELL_N) / 2)))

    def check_eat(self):
        if self.food1.pos == self.one.body[0]:
            self.food1.new_position()
            self.one.new_body = True
            for block in self.one.body:
                if block == self.food1.pos:
                    self.food1.new_position()
        elif self.food2.pos == self.one.body[0]:
            self.food2.new_position()
            self.one.new_body = True
            for block in self.one.body:
                if block == self.food2.pos:
                    self.food2.new_position()

        if self.food1.pos == self.two.body[0]:
            self.food1.new_position()
            self.two.new_body = True
            for block in self.two.body:
                if block == self.food1.pos:
                    self.food1.new_position()
        elif self.food2.pos == self.two.body[0]:
            self.food2.new_position()
            self.two.new_body = True
            for block in self.two.body:
                if block == self.food2.pos:
                    self.food2.new_position()

    def one_check_hit(self):
        for body in self.one.body[1:]:
            if body == self.one.body[0]:
                self.game_over()
        for body in self.two.body[:-1]:
            if body == self.one.body[0]:
                self.game_over()
        if not 0 <= self.one.body[0].x < CELL_N or \
                not 0 <= self.one.body[0].y < CELL_N:
            self.game_over()

    def two_check_hit(self):
        for body in self.two.body[1:]:
            if body == self.two.body[0]:
                self.game_over()
        for body in self.one.body[:-1]:
            if body == self.two.body[0]:
                self.game_over()
        if not 0 <= self.two.body[0].x < CELL_N or \
                not 0 <= self.two.body[0].y < CELL_N:
            self.game_over()

    def game_over(self):
        self.one.restart()
        self.two.restart()

    def place_score(self):
        board = pygame.Rect(0, (CELL_N * CELL_S), (CELL_N * CELL_S), 60)
        pygame.draw.rect(MAIN_WINDOW, (255, 255, 255), board)
        one = 'Player One:  ' + f'{len(self.one.body) - 5}'
        one_score = score_font.render(one, True, (0, 0, 0))
        MAIN_WINDOW.blit(one_score, (20, (CELL_S * CELL_N + 10)))

        two = 'Player Two:  ' + f'{len(self.two.body) - 5}'
        two_score = score_font.render(two, True, (0, 0, 0))
        MAIN_WINDOW.blit(two_score, ((CELL_S * CELL_N - 170),
                                     (CELL_S * CELL_N + 10)))

    def winner_text(self):
        if len(self.one.body) > len(self.two.body):
            winner = 'Player One  in  Lead!'
            winner_board = winner_font.render(winner, True, (0, 189, 242))
            MAIN_WINDOW.blit(winner_board, ((CELL_S * CELL_N - 520),
                                            (CELL_S * CELL_N + 6)))
        elif len(self.one.body) < len(self.two.body):
            winner = 'Player Two  in  Lead!'
            winner_board = winner_font.render(winner, True, (190, 168, 118))
            MAIN_WINDOW.blit(winner_board, ((CELL_S * CELL_N - 520),
                                            (CELL_S * CELL_N + 6)))
        else:
            winner = 'Tied!'
            winner_board = winner_font.render(winner, True, (0, 0, 0))
            MAIN_WINDOW.blit(winner_board, ((CELL_S * CELL_N - 395),
                                            (CELL_S * CELL_N + 6)))


pygame.init()

CELL_S = 40
CELL_N = 18

MAIN_WINDOW = pygame.display.set_mode((CELL_N * CELL_S, CELL_N * CELL_S + 60))
clock = pygame.time.Clock()
food = pygame.image.load('snake_graphics/candy.png')
score_font = pygame.font.Font('Fonts/pixelated.ttf', 28)
msg_font = pygame.font.Font('Fonts/pixelated.ttf', 35)
winner_font = pygame.font.Font('Fonts/pixelated.ttf', 40)
game = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.one.direction.y != 1:
                game.one.direction = Vector2(0, -1)
            elif event.key == pygame.K_w and game.two.direction.y != 1:
                game.two.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN and game.one.direction.y != -1:
                game.one.direction = Vector2(0, 1)
            elif event.key == pygame.K_s and game.two.direction.y != -1:
                game.two.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT and game.one.direction.x != 1:
                game.one.direction = Vector2(-1, 0)
            elif event.key == pygame.K_a and game.two.direction.x != 1:
                game.two.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT and game.one.direction.x != -1:
                game.one.direction = Vector2(1, 0)
            elif event.key == pygame.K_d and game.two.direction.x != -1:
                game.two.direction = Vector2(1, 0)

    MAIN_WINDOW.fill((110, 180, 0))
    game.place_elements()
    pygame.display.update()
    clock.tick(120)
