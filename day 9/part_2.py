with open('input.txt') as f:
    nums = f.read().splitlines()

nums = [int(num) for num in nums]

def can_be_summed(ls, num):
    for n in ls:
        res = num - n
        if res != num/2 and res in ls:
            return True

    return False

def find_contiguous(nums, sol):
    def find_sum(nums, start, end):
        return sum(nums[start: end + 1])

    start = 0
    increase = 1

    while start + increase < len(nums):
        output = find_sum(nums, start, start + increase)
        if output == sol:
            return nums[start:start + increase + 1]

        if output > sol:
            start += 1
            increase = 1

        increase += 1

preamble = 25
for i, num in enumerate(nums):
    if i <= preamble:
        continue

    preamble_nums = nums[i - preamble:i]
    if not can_be_summed(preamble_nums, num):
        continguous_nums = find_contiguous(nums, num)
        print(max(continguous_nums) + min(continguous_nums))
        break

    