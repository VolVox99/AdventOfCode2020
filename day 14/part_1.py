with open('input.txt') as f:
    lines = f.read().splitlines()


memory = {}

def apply_bit_mask(binary_val, mask):
    masked_bin = ''
    for b, m in zip(binary_val, mask):
        if m == 'X': 
            masked_bin += str(b)

        else:
            masked_bin += str(m)

    return masked_bin


def to_binary(inp):
    bin_string = bin(inp)[2:]
    return ''.join(bin_string.zfill(36))


def un_binary(inp):
    return int(inp, 2)


for ln in lines:
    if 'mask' in ln:
        mask = ln.split(' = ')[-1]

    else:
        address, val = ln.split(' = ')
        address = address[address.index('[') + 1: address.index(']')]
        binary = to_binary(int(val))
        memory[address] =  un_binary(apply_bit_mask(binary, mask))
        


print(sum(memory.values()))
# print(memory)
