with open('input.txt') as f:
    lines = f.read().splitlines()





#giving each a unique id so we know if we have visited before
for i in range(len(lines)):
    lines[i] = f'{i} {lines[i]}'


def get_num(val):
    op = val[0]
    num = int(val[1:])
    return num * -1 if op == '-' else num





accumulator = 0
line_ct = 0

line_ids = []

while True:
    line = lines[line_ct]
    line_id, inst, val = line.split(' ')
    if line_id in line_ids:
        break
    line_ids.append(line_id)
    if inst == 'acc':
        accumulator += get_num(val)

    elif inst == 'jmp':
        line_ct += get_num(val) - 1

    line_ct += 1




print(accumulator)