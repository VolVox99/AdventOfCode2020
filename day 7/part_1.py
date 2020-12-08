with open('input.txt') as f:
    rules = f.read().splitlines()



my_bag = 'shiny gold'
bags_dict = {}


can_contain_my_bag = 0
for rule in rules:
    words = rule.split(' ')
    container_bag = words[0] + ' ' + words[1]
    count = words[4]
    if count == 'no' or container_bag == my_bag: continue
    container_can_contain = []

    for i in range(1, int(len(words)/4)):
        bag = words[(i * 4) + 1: (i * 4) + 3]
        container_can_contain.append(bag[0] + ' ' + bag[1])

    bags_dict[container_bag] = container_can_contain


def bags_can_contain(container_bags):

    def bag_can_contain(container_bag):
        try:
            x = bags_dict[container_bag]
            if my_bag in x or my_bag in container_bag:
                return True
            
            return bags_can_contain(x)

        except:
            return False

    if my_bag in container_bags:
        return True

    for bag in container_bags:
        if bag_can_contain(bag):
            return True

            

for key, value in bags_dict.items():
    if bags_can_contain(value):
        can_contain_my_bag += 1


print(can_contain_my_bag)

