class Board:

    def __init__(self, grid):
        self.grid = grid
        self.row = 0
        self.col = 0
        self.max_row = len(self.grid)
        self.max_col = len(self.grid[0])
        self.element = '.'

    def check_out_of_bounds(self):
        if self.col >= self.max_col:
            self.col = 0

    def set_element(self):
        self.element = self.grid[self.row][self.col]

    def is_tree(self):
        return self.element == '#'

    def move_right(self):
        self.col += 1
        self.check_out_of_bounds()

    def move_down(self):
        self.row += 1



def func(right = 3, down = 1):

    with open('input.txt') as f:
        board = Board(f.read().splitlines())

    trees_found = 0

    while board.row < board.max_row - 1:
        for _ in range(right):
            board.move_right()

        for _ in range(down):
            board.move_down()

        board.set_element()

        if board.is_tree():
            trees_found += 1


    return trees_found
        

print(func() * func(1, 1) * func(5, 1) * func(7, 1) * func(1, 2))