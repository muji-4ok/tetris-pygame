class BaseShape:
    def __init__(self, field, x, y):
        self.field = field
        self.x = x
        self.y = y
        self.state = 1
        self.states = []
        self.width = len(field[0])
        self.height = len(field)
        self.x_range = range(self.width)
        self.y_range = range(self.height)
        self.color = 0
        self.max_rotations = 1

    def rotate(self, direction):
        self.state = self.state + 1 if direction == 1 else self.state - 1
        self.state %= 4

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def display(self):
        for i, row in enumerate(self.states[self.state]):
            for j, block in enumerate(row):
                if block:
                    x = self.x + j
                    y = self.y + i
                    self.field[y][x] = self.color

    def clear(self):
        for i, row in enumerate(self.states[self.state]):
            for j, block in enumerate(row):
                if block:
                    x = self.x + j
                    y = self.y + i
                    self.field[y][x] = 0

    def collides(self):
        for i, row in enumerate(self.states[self.state]):
            for j, block in enumerate(row):
                if block:
                    x = self.x + j
                    y = self.y + i
                    if self.field[y][x]:
                        return True, x, y

        return False, 0, 0

    def is_out_of_bounds(self):
        for i, row in enumerate(self.states[self.state]):
            for j, block in enumerate(row):
                if block:
                    x = self.x + j
                    y = self.y + i
                    if x not in self.x_range or y not in self.y_range:
                        return True, x, y

        return False, 0, 0

    def overlaps(self):
        for i, row in enumerate(self.states[self.state]):
            for j, block in enumerate(row):
                if block:
                    x = self.x + j
                    y = self.y + i
                    in_bounds = x in self.x_range and y in self.y_range
                    if not in_bounds or self.field[y][x]:
                        return True, x, y

        return False, 0, 0


class Stick(BaseShape):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)
        self.color = 3
        self.max_rotations = 2
        self.states = [
            [
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1]
            ],
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1]
            ],
            [
                [0, 0, 1],
                [0, 0, 1],
                [0, 0, 1],
                [0, 0, 1]
            ],
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 1, 1]
            ]
        ]


class Cube(BaseShape):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)
        self.color = 4
        self.states = [
            [
                [1, 1],
                [1, 1]
            ],
            [
                [1, 1],
                [1, 1]
            ],
            [
                [1, 1],
                [1, 1]
            ],
            [
                [1, 1],
                [1, 1]
            ]
        ]


class LeftZig(BaseShape):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)
        self.color = 6
        self.states = [
            [
                [0, 1],
                [1, 1],
                [1, 0]
            ],
            [
                [1, 1, 0],
                [0, 1, 1]
            ],
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1]
            ]
        ]


class RightZig(BaseShape):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)
        self.color = 2
        self.states = [
            [
                [1, 0],
                [1, 1],
                [0, 1]
            ],
            [
                [0, 1, 1],
                [1, 1, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1]
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1]
            ]
        ]


class LeftLeg(BaseShape):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)
        self.color = 1
        self.states = [
            [
                [0, 1],
                [0, 1],
                [1, 1]
            ],
            [
                [1, 0, 0],
                [1, 1, 1]
            ],
            [
                [1, 1],
                [1, 0],
                [1, 0]
            ],
            [
                [1, 1, 1],
                [0, 0, 1]
            ]
        ]


class RightLeg(BaseShape):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)
        self.color = 7
        self.states = [
            [
                [1, 0],
                [1, 0],
                [1, 1]
            ],
            [
                [1, 1, 1],
                [1, 0, 0]
            ],
            [
                [1, 1],
                [0, 1],
                [0, 1]
            ],
            [
                [0, 0, 1],
                [1, 1, 1]
            ]
        ]


class Triangle(BaseShape):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)
        self.color = 5
        self.state = 0
        self.states = [
            [
                [0, 1, 0],
                [1, 1, 1]
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 1],
                [1, 1],
                [0, 1]
            ]
        ]
