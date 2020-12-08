with open('input.txt') as f:
    lines = f.read().splitlines()


#giving each a unique id so we know if we have visited before
for i in range(len(lines)):
    lines[i] = f'{i} {lines[i]}'


def get_num(val):
    op = val[0]
    num = int(val[1:])
    return num * -1 if op == '-' else num


def check_terminating(lines):
    line_ct = 0
    line_ids = []

    while line_ct < len(lines):
        line = lines[line_ct]
        line_id, inst, val = line.split(' ')

        if line_id in line_ids:
            return False

        line_ids.append(line_id)
        if inst == 'jmp':
            line_ct += get_num(val) - 1

        line_ct += 1

    return True


def get_accumulator(lines):
    accumulator = 0
    line_ct = 0
    line_ids = []

    while line_ct < len(lines):
        line = lines[line_ct]
        line_id, inst, val = line.split(' ')
        if line_id in line_ids:
            return accumulator
        line_ids.append(line_id)
        if inst == 'acc':
            accumulator += get_num(val)

        elif inst == 'jmp':
            line_ct += get_num(val) - 1

        line_ct += 1

    return accumulator



opposite = {'nop': 'jmp', 'jmp':'nop'}

 

def interpret_lines(lines):
    line_ct = 0

    while line_ct < len(lines):
        line = lines[line_ct]
        inst = line.split(' ')[1]
        if inst != 'acc':
            new_lines = lines[::]
            new_lines[line_ct] = new_lines[line_ct].replace(inst, opposite[inst])
            if check_terminating(new_lines):
                return new_lines

        line_ct += 1

    return lines


print(get_accumulator(interpret_lines(lines)))