#coding:utf-8
"""Sort test"""

NUM_LIST = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 7, 4, 5, 3, 6, 9, 8]
]

NUMS = NUM_LIST[1]
print NUMS
LENGTH = len(NUMS)

COUNT_SWAP = 0
COUNT = 0

# bubble_sort
for i  in range(LENGTH):
    for j in range(LENGTH-i-1):
        COUNT += 1
        if NUMS[j] > NUMS[j + 1]:
            NUMS[j], NUMS[j + 1] = NUMS[j+1], NUMS[j]
            COUNT_SWAP += 1

print NUMS, COUNT_SWAP, COUNT
