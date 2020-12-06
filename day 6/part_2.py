with open('input.txt') as f:
    all_answers = f.read().replace(' ', '').split('\n\n')

everyone_yes = 0

for group in all_answers:
    group_answers = group.split('\n')
    answers_len = len(group_answers)
    total_yes = 0

    if answers_len <= 1:
        total_yes += len(group_answers[0])

    else:
        rest_answers = group_answers[1:]
        for letter in group_answers[0]:
            found = True
            for answer in rest_answers:
                if letter not in answer:
                    found = False
            
        
            total_yes += found

    everyone_yes += total_yes



print(everyone_yes)