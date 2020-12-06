
with open('input.txt') as f:
    passes = f.read().splitlines()


pwrds_valid = 0


for line in passes:
    
    lower, rest = line.split('-')
    upper = rest.split(' ')[0]
    lower = int(lower)
    upper = int(upper)
    letter, pwrd = rest.split(':')
    letter = letter[-1]
    pwrd = pwrd.strip()


    count = pwrd[lower - 1].count(letter) + pwrd[upper - 1].count(letter)
    if count == 1:
        pwrds_valid += 1



print(pwrds_valid)
