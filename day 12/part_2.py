with open('input.txt') as f:
    lines = f.read().splitlines()

def move(dr, num):
    if dr == 'N':
        way_point_state.y += num

    elif dr == 'S':
        way_point_state.y -= num

    elif dr == 'E':
        way_point_state.x += num

    elif dr == 'W':
        way_point_state.x -= num


def rotate(direction, deg):
    if deg == 360:
        return

    if deg == 180:
        way_point_state.x *= -1
        way_point_state.y *= -1

    elif deg == 90 or deg == 270:
        if direction == 'R':
            way_point_state.x, way_point_state.y = way_point_state.y, -1 * way_point_state.x

        else:
            way_point_state.x, way_point_state.y = -1 * way_point_state.y, way_point_state.x


    elif deg == 270:
        if direction == 'R':
            way_point_state.x, way_point_state.y = -1 * way_point_state.y, way_point_state.x

        else:
           way_point_state.x, way_point_state.y = way_point_state.y, -1 * way_point_state.x


def forward(num):
    for _ in range(num):
        ship_state.x += way_point_state.x
        ship_state.y += way_point_state.y

moves = ['N', 'S', 'E', 'W']
rots = ['L', 'R']
dirs = {0: 'N',  1:'E', 2:'S', 3:'W'}

class way_point_state:
    x = 10
    y = 1


class ship_state:
    x = 0
    y = 0
    #north = 0, east = 1, south = 2, west = 3
    dr = 1

for ln in lines:
    action, num = ln[0], int(ln[1:])

    if action in moves:
        move(action, num)

    elif action in rots:
        rotate(action, num)
    
    else:
        forward(num)

print(abs(ship_state.x) + abs(ship_state.y))
