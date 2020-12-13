with open('input.txt') as f:
    lines = f.read().splitlines()


start, timestamps = lines
start = int(start)


def get_mul(num, start):
    beg_mul = start//num
    while True:
        if (res := num * beg_mul) > start:
            return res

        beg_mul += 1




deps = []
for time in timestamps.split(','):
    if time == 'x':
        continue

    deps.append([int(time), get_mul(int(time), start)])


deps_dep = [i[1] for i in deps]
for i in range(len(deps)):
    if deps[i][1] == min(deps_dep):
        print((deps[i][1] - start) * deps[i][0])
        break



