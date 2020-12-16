from collections import defaultdict

with open('input.txt') as f:
    nums = [int(i) for i in f.read().split(',')]


spoken_ct = defaultdict(lambda: 0)
last = defaultdict(lambda: [])
for i, k in enumerate(nums):
    spoken_ct[k] = 1
    last[k].append(i + 1)

    
curr_n = 0
last_n = nums[-1]
i = len(nums) + 1



while True:
    if i > 2020:
        print(curr_n)
        break
    
    if spoken_ct[last_n] == 1:
        curr_n = 0

    else:
        curr_n = last[last_n][-1] - last[last_n][-2]
        
    
    last[curr_n].append(i)
    spoken_ct[curr_n] += 1
    last_n = curr_n


    i += 1


