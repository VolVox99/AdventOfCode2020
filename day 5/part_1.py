with open('input.txt') as f:
    passes = f.read().splitlines()


reference = {
    'F': lambda l, u: [l, int((l + u + 1)/2) - 1], 
    'B': lambda l, u: [int((l + u + 1)/2), u],
    'R': lambda l, u: [int((l + u + 1)/2), u],    
    'L': lambda l, u: [l, int((l + u + 1)/2) - 1],    
}


def decode(brding, i = 0, lower = 0, upper = 127):
    
    lower, upper = reference[brding[i]](lower, upper)
    if lower == upper:
        return lower
    
    return decode(brding, i + 1, lower, upper)

def get_seat_id(row, col):
    return row * 8 + col


seat_ids = []

for brding in passes:
    row = decode(brding[:7])
    col = decode(brding[7:], lower = 0, upper = 7)
    seat_ids.append(get_seat_id(row, col))

print(max(seat_ids))