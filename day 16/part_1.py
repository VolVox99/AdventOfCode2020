with open('input.txt') as f:
    sections = f.read().split('\n\n')




def parse_reqs(reqs):
    ranges = []
    for req in reqs.split('\n'):
        _name, rng = req.split(': ')
        rngs = rng.split(' or ')
        for single_range in rngs:
            ranges.append([int(i) for i in single_range.split('-')])
            

    return ranges

def parse_tickets(string):
    tickets = []
    for ticket in string.splitlines()[1:]:
        for i in ticket.split(','):
            tickets.append(int(i))

    return tickets


reqs, mine, nearby = sections
reqs = parse_reqs(reqs)
mine = parse_tickets(mine)
nearby = parse_tickets(nearby)


invals = []

for ticket in nearby:
    valid = False
    for rng in reqs:
        top, bottom = rng
        if top <= ticket <= bottom:
            valid = True

    if not valid:
        invals.append(ticket)


print(sum(invals))