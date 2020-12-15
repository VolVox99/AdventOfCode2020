from itertools import product

with open('input.txt') as f:
    lines = f.read().splitlines()


memory = {}
mask = ''

def apply_bit_mask(binary_val, mask):
    masked_bin = ''
    for b, m in zip(binary_val, mask):
        if m == '0': 
            masked_bin += str(b)

        else:
            masked_bin += str(m)

    return masked_bin


def to_binary(inp):
    bin_string = bin(inp)[2:]
    return ''.join(bin_string.zfill(36))

    
#you cant assing items in a string so im using this to circumvent that
def copy_replace(arr, i, new):
    return ''.join([j if idx != i else new for idx, j in enumerate(arr)])


def get_permutations(length):
    return list(product(['0', '1'], repeat = length))


def get_addresses(address):
    possibles = []
    count = address.count('X')
    perms = get_permutations(count)
    for perm in perms:
        ctr = 0
        new_add = address
        for i, a in enumerate(address):
            if a == 'X':
                new_add = copy_replace(new_add, i, perm[ctr])
                ctr += 1

        possibles.append(new_add)

    return possibles

def un_binary(inp):
    return int(inp, 2)



for ln in lines:
    if 'mask' in ln:
        mask = ln.split(' = ')[-1]

    else:
        address, val = ln.split(' = ')
        address = int(address[address.index('[') + 1: address.index(']')])
        for add in get_addresses(apply_bit_mask(to_binary(address), mask)): 
            memory[un_binary(add)] = int(val)
        
    

print(sum(memory.values()))






