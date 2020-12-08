with open('input.txt') as f:
    rules = f.read().splitlines()

my_bag = 'shiny gold'
bags_dict = {}

my_bag_can_contain = 0
for rule in rules:
    words = rule.split(' ')
    container_bag = words[0] + ' ' + words[1]
    count = words[4]
    if count == 'no': continue
    container_can_contain = []

    for i in range(1, int(len(words)/4)):
        start = i * 4
        bag = words[start + 1: start + 3]
        count = int(words[start])
        container_can_contain.append([bag[0] + ' ' + bag[1], count])

    bags_dict[container_bag] = container_can_contain


def get_bags_count(bags, ct_sum = 0):


    def get_bag_count(bag):
        try:
            return bag[1] + bag[1] * get_bags_count(bags_dict[bag[0]])

        except KeyError:
            return bag[1]


    for bag in bags:
        ct_sum += get_bag_count(bag)

    return ct_sum

            
print(get_bags_count(bags_dict[my_bag]))


