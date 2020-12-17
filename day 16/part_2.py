with open('input.txt') as f:
    sections = f.read().split('\n\n')

def get_product(arr):
    m = 1
    for i in arr:
        m *= i
    return m

transpose = lambda X: [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]


def parse_reqs(reqs):
    ranges = []
    for req in reqs.split('\n'):
        _name, rng = req.split(': ')
        rngs = rng.split(' or ')
        full_range = []
        for single_range in rngs:
            full_range.append([int(i) for i in single_range.split('-')])

        ranges.append(full_range)

    return ranges

def parse_tickets(string):
    tickets = []
    for ticket in string.splitlines()[1:]:
        temp = []
        for i in ticket.split(','):
            temp.append(int(i))

        tickets.append(temp)

    return tickets


departure_reqs, mine, nearby = sections
departure_reqs = parse_reqs(departure_reqs)
mine = parse_tickets(mine)[0]
num_of_ticks = len(mine)
nearby = parse_tickets(nearby)


def delete_invals(ticks):
    invals = []
    for i, ticket in enumerate(ticks):
        for val in ticket:
            valid = False
            for rng in departure_reqs:
                for outer_rng in rng:
                    bottom, top = outer_rng
                    if bottom <= val <= top:
                        valid = True

            if not valid:
                invals.append(i)
                        
    return [i for j, i in enumerate(ticks) if j not in invals]

nearby = delete_invals(nearby)
departure_reqs = parse_reqs('\n'.join([i for i in sections[0].split('\n')  if 'departure' in i]))


def find_req_indexes(fields, reqs):
    indexes = []

    def matches_req(field, req):
        for val in field:
                temp_bool = []
                for outer_rng in req:
                    bottom, top = outer_rng
                    temp_bool.append(bottom <= val <= top)

                if not any(temp_bool):
                    return False

        return True

    for r_i, req in enumerate(reqs):
        temp = []
        for f_i, field in enumerate(fields):
            if (matches_req(field, req)):
                temp.append([r_i, f_i])

        indexes.append(temp)

    return indexes


def field_ct_eq_1(combs, field):
    field_ct = 0
    req = 0
    for sect in combs:
        for comb in sect:
            if comb[1] == field:
                req = comb[0]
                field_ct += 1

    if field_ct == 1:
        return req

    return -1


departure_fields = []

while len(departure_fields) < 6:
    possible_combinations = find_req_indexes(transpose(nearby), departure_reqs)

    for col in range(num_of_ticks):
        req = field_ct_eq_1(possible_combinations, col)
        if req != -1 and col not in departure_fields:
            departure_fields.append(col)
            departure_reqs.pop(req)
            break

departure_fields[-1] += 10
    
my_ticket_departure_fields = [mine[i] for i in departure_fields]
print(get_product(my_ticket_departure_fields))
