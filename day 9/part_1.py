with open('input.txt') as f:
    nums = f.read().splitlines()

nums = [int(num) for num in nums]

def can_be_summed(ls, num):
    for n in ls:
        res = num - n
        if res != num/2 and res in ls:
            return True

    return False

preamble = 25
for i, num in enumerate(nums):
    if i <= preamble:
        continue

    preamble_nums = nums[i - preamble:i]
    if not can_be_summed(preamble_nums, num):
        print(num)

    

