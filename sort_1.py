#coding:utf-8
"""Sort test
"""

NUM_LIST = [
    [1, 9, 8, 5, 6, 7, 4, 3, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 9, 8]
]

NUMS = NUM_LIST[2]
print NUMS
LENGTH = len(NUMS)

COUNT_SWAP = 0
COUNT = 0

# bubble_sort
for i  in range(LENGTH):
    FLAG = False
    for j in range(LENGTH-i-1):
        COUNT += 1
        if NUMS[j] > NUMS[j+1]:
            TMP = NUMS[j]
            NUMS[j] = NUMS[j+1]
            NUMS[j+1] = TMP
            COUNT_SWAP += 1
    if not FLAG:
        break

print NUMS, COUNT_SWAP, COUNT
