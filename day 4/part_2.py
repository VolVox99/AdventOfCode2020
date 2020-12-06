
with open('input.txt') as f:
    passports = f.read()
    
passports = passports.split("\n\n")


def validate_height(string):
    if 'cm' in string:
        num = int(string[:string.index('cm')])
        return 150 <= num <= 193

    elif 'in' in string:
        num = int(string[:string.index('in')])
        return 59 <= num <= 76


def validate_hair_color(string):
    string = string[1:]
    first_req = len(string) == 6
    second_req = True
    valids = [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
    for letter in string:
        if letter not in valids:
            second_req = False

    return first_req and second_req

required = [
    ['byr', lambda x: len(x) == 4 and 1920 <= int(x) <= 2002],
    ['iyr', lambda x: len(x) == 4 and 2010 <= int(x) <= 2020],
    ['eyr', lambda x: len(x) == 4 and 2020 <= int(x) <= 2030], 
    ['hgt', validate_height], 
    ['hcl', validate_hair_color], 
    ['ecl', lambda x: len(x) == 3 and x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']],
    ['pid', lambda x: len(x) == 9]
]

valid_count = 0


def is_valid(req, func):
    start = port.index(req)

    value = port[start:].split(':')[1]
    if ' ' in value:
        end_of_val = value.index(' ')

    elif '\n' in value:
        end_of_val = value.index('\n')
    
    else:
        end_of_val = len(value) - 1

    value = value[:end_of_val + 1]

    value = value.replace(' ', '')
    value = value.replace('\n', '')
    
    return func(value)


for port in passports:
    found = True
    for req, _, in required:
        if req not in port:
            found = False
    if not found: continue

    valid = True
    for req, func in required:
        if not is_valid(req,  func):
            valid = False

    if valid:
        valid_count += 1

print(valid_count)
