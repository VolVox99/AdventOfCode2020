with open('input.txt') as f:
    all_answers = f.read().split('\n\n')



total_yes = 0

for group in all_answers:
    group_answers = set(group.replace('\n', ''))
    total_yes += len(group_answers)

print(total_yes)