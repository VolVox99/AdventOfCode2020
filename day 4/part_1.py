import re


with open('input.txt') as f:
    passports = f.read()
    
passports = passports.split("\n\n")
required = [
    'byr',
    'iyr',
    'eyr', 
    'hgt', 
    'hcl', 
    'ecl',
    'pid'
]

valid_count = 0

for port in passports:
    valid = True
    for req in required:
        if req not in port:
            valid = False

    if valid:
        valid_count += 1



print(valid_count)
