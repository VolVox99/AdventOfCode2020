with open('input.txt') as f:
    seats = f.read().splitlines()


empty = 'L'
occ = '#'
floor = '.'


max_row = len(seats)
max_col = len(seats[0])

def get_adj(seats, coords):
    def get_top(coords):
        row, col = coords
        if row > 0:
            return [row - 1, col]

    def get_bottom(coords):
        row, col = coords
        if row < max_row - 1:
            return [row + 1, col]

    def get_left(coords):
        row, col = coords
        if col > 0:
            return [row, col - 1]

    def get_right(coords):
        row, col = coords
        if col < max_col - 1:
            return [row, col + 1]

    def get_top_left(coords):
        top = get_top(coords)
        if not top:
            return False
        return get_left(top)

    def get_top_right(coords):
        top = get_top(coords)
        if not top:
            return False
        return get_right(top)

    def get_bottom_left(coords):
        bottom = get_bottom(coords)
        if not bottom:
            return False
        return get_left(bottom)

    def get_bottom_right(coords):
        bottom = get_bottom(coords)
        if not bottom:
            return False
        return get_right(bottom)

    funcs = [get_top, get_bottom, get_left, get_right, get_top_left, get_top_right, get_bottom_left, get_bottom_right
    ]
    vals = [func(coords) for func in funcs]
    return [seats[c[0]][c[1]] for c in vals if c]

#you cant assing items in a string so im using this to circumvent that
def copy_replace(arr, i, new):
    return [j if idx != i else new for idx, j in enumerate(arr)]


def two_d_arr_equal(arr_1, arr_2):

    for x, y in zip(arr_1, arr_2):
        for i, j in zip(x, y):
            if i != j:
                return False
    return True


def get_count_2d_arr(arr, item):
    count = 0
    for i in arr:
        count += i.count(item)

    return count


def model_round(seats):
    new_seats = seats[::]
    for row in range(max_row):
        for col in range(max_col):
            seat = seats[row][col]
            if seat == floor:
                continue

            adjs = get_adj(seats, (row, col))

            if seat == empty and adjs.count(occ) == 0:
                new_seats[row] = copy_replace(new_seats[row], col, occ)


            elif seat == occ and adjs.count(occ) >= 4:
                new_seats[row] = copy_replace(new_seats[row], col, empty)

    return new_seats


def final(old, new):
        new = model_round(old)

        if two_d_arr_equal(old, new):
            return get_count_2d_arr(new, occ)
            
        return final(new, model_round(new))

print(final(seats, model_round(seats)))