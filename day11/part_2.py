with open('input.txt') as f:
    seats = f.read().splitlines()


empty = 'L'
occ = '#'
floor = '.'
seat_types = [empty, occ]


max_row = len(seats)
max_col = len(seats[0])

def get_visible(seats, coords):

    def get_top(coords, first = True):
        row, col = coords
        if not first and seats[row][col] in seat_types:
            return [row, col]
        if row > 0:
            return get_top([row - 1, col], False)


    def get_bottom(coords, first = True):
        row, col = coords

        if not first and seats[row][col] in seat_types:
            return [row, col]

        if row < max_row - 1:
            return get_bottom([row + 1, col], False)

    def get_left(coords, first = True):
        row, col = coords

        if not first and seats[row][col] in seat_types:
            return [row, col]

        if col > 0:
            return get_left([row, col - 1], False)

    def get_right(coords, first = True):
        row, col = coords

        if not first and seats[row][col] in seat_types:
            return [row, col]

        if col < max_col - 1:
            return get_right([row, col + 1], False)

    def get_top_left(coords, first = True):
        row, col = coords

        if not first and seats[row][col] in seat_types:
            return [row, col]

        if row > 0 and col > 0:
            return get_top_left([row - 1, col - 1], False)

    def get_top_right(coords, first = True):
        row, col = coords

        if not first and seats[row][col] in seat_types:
            return [row, col]

        if row > 0 and col < max_col - 1:
            return get_top_right([row - 1, col + 1], False)

    def get_bottom_left(coords, first = True):
        row, col = coords

        if not first and seats[row][col] in seat_types:
            return [row, col]

        if row < max_row - 1 and col > 0:
            return get_bottom_left([row + 1, col - 1], False)

    def get_bottom_right(coords, first = True):
        row, col = coords

        if not first and seats[row][col] in seat_types:
            return [row, col]

        if row < max_row - 1 and col < max_col - 1:
            return get_bottom_right([row + 1, col + 1], False)

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

            visible = get_visible(seats, (row, col))

            if seat == empty and visible.count(occ) == 0:
                new_seats[row] = copy_replace(new_seats[row], col, occ)

            elif seat == occ and visible.count(occ) >= 5:
                new_seats[row] = copy_replace(new_seats[row], col, empty)

    return new_seats


def final(old, new):
        new = model_round(old)


        if two_d_arr_equal(old, new):
            return get_count_2d_arr(new, occ)
            
        return final(new, model_round(new))


print(final(seats, model_round(seats)))

