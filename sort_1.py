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

# # bubble_sort version 1
# for i  in range(LENGTH):
#     for j in range(LENGTH-i-1):
#         COUNT += 1
#         if NUMS[j] > NUMS[j + 1]:
#             NUMS[j], NUMS[j + 1] = NUMS[j+1], NUMS[j]
#             COUNT_SWAP += 1

# print NUMS, COUNT_SWAP, COUNT   # COUNT_SWAP = 7, COUNT = 36


# bubble_sort version 2
for i in range(LENGTH):
    BUBBLE_TIMES = 0        # 本次循环进行的元素交换次数，若元素交换的次数为0，则代表数组为目标顺序，退出循环
    for j in range(LENGTH - i - 1):
        COUNT += 1
        if NUMS[j] > NUMS[j + 1]:
            NUMS[j], NUMS[j + 1] = NUMS[j + 1], NUMS[j]
            COUNT_SWAP += 1
            BUBBLE_TIMES += 1
    if BUBBLE_TIMES == 0:
        print BUBBLE_TIMES
        break

print NUMS, COUNT_SWAP, COUNT       # COUNT_SWAP = 7, COUNT = 26
