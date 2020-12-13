from functools import reduce

with open('input.txt') as f:
    lines = f.read().splitlines()


times = lines[1].split(',')


def chinese_remainder(n, a):
    summation = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        summation += a_i * mul_inv(p, n_i) * p

    return summation % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 



filt_times = []

offsets = []

for i in range(len(times)):
    if times[i] != 'x':
        filt_times.append(int(times[i]))
        offsets.append(i * -1)

print(chinese_remainder(filt_times, offsets))
