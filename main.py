from random import randint

import pygame as p

import shapes


class Game:
    WIDTH = 200
    HEIGHT = 400
    SIZE = WIDTH, HEIGHT
    BLOCK_SIZE = 20
    screen = p.display.set_mode(SIZE)
    p.display.set_caption('Application')
    COLORS = {
        0: p.image.load('black.png'),
        1: p.image.load('red.png'),
        2: p.image.load('yellow.png'),
        3: p.image.load('blue.png'),
        4: p.image.load('orange.png'),
        5: p.image.load('purple.png'),
        6: p.image.load('teal.png'),
        7: p.image.load('green.png')
    }
    SHAPES = {
        0: shapes.Stick,
        1: shapes.RightZig,
        2: shapes.LeftZig,
        3: shapes.RightLeg,
        4: shapes.LeftLeg,
        5: shapes.Cube,
        6: shapes.Triangle
    }
    field = []

    def __init__(self):
        p.init()

        for i in range(20):
            self.field.append([])

            for j in range(10):
                self.field[i].append(0)

        shape = randint(0, 6)
        self.piece = self.SHAPES[shape](self.field, 3, 0)
        p.time.set_timer(p.USEREVENT, 500)

    def create_piece(self):
        self.piece.display()
        shape = randint(0, 6)
        self.piece = self.SHAPES[shape](self.field, 3, 0)

        if self.piece.collides()[0]:
            print('Game over')
            quit(0)

    def update(self):
        self.piece.move(0, 1)

        if self.piece.overlaps()[0]:
            self.piece.move(0, -1)
            self.create_piece()

    def handle_rotation(self, direction):
        self.piece.rotate(direction)

        if self.piece.overlaps()[0]:
            self.piece.rotate(-direction)

    @staticmethod
    def is_full(row):
        for block in row:
            if not block:
                return False

        return True

    def clear_lines(self):
        for i, row in enumerate(self.field):
            if not self.is_full(row):
                continue

            for j in reversed(range(1, i + 1)):
                self.field[j] = self.field[j - 1]

            self.field[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def handle_movement(self, key):
        if key == p.K_RIGHT:
            self.piece.move(1, 0)
            if self.piece.overlaps()[0]:
                self.piece.move(-1, 0)
        elif key == p.K_LEFT:
            self.piece.move(-1, 0)
            if self.piece.overlaps()[0]:
                self.piece.move(1, 0)
        elif key == p.K_SPACE:
            while not (self.piece.overlaps()[0]):
                self.piece.move(0, 1)

            self.piece.move(0, -1)
            self.create_piece()
        elif key == p.K_UP:
            self.handle_rotation(1)
        elif key == p.K_DOWN:
            self.handle_rotation(-1)

    def handle_events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                quit()
            elif event.type == p.USEREVENT:
                self.update()
            elif event.type == p.KEYDOWN:
                self.handle_movement(event.key)

    def display(self):
        self.piece.clear()

        self.handle_events()

        self.clear_lines()

        self.piece.display()

        for i, row in enumerate(self.field):
            for j, block in enumerate(row):
                self.screen.blit(self.COLORS[block],
                                 (j * self.BLOCK_SIZE, i * self.BLOCK_SIZE))

        p.display.update()


if __name__ == '__main__':
    game = Game()

    while True:
        game.display()
