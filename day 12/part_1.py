with open('test.txt') as f:
    lines = f.read().splitlines()

def move(dr, num):
    if dr == 'N':
        state.y += num

    elif dr == 'S':
        state.y -= num

    elif dr == 'E':
        state.x += num

    elif dr == 'W':
        state.x -= num


def rotate(direction, deg):
    deg *= -1 if direction == 'L' else 1
    state.dr += (deg / 90) % 4
    if state.dr >= 4:
        state.dr %= 4


def forward(num):
    move(dirs[state.dr], num)

moves = ['N', 'S', 'E', 'W']
rots = ['L', 'R']
dirs = {0: 'N',  1:'E', 2:'S', 3:'W'}

class state:
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




print(abs(state.x) + abs(state.y))
