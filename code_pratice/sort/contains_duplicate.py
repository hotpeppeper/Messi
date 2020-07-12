'''
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
'''


def contains_duplicate(nums, k, t):
    i = 0
    j = len(nums) - 1
    bok = False
    while i != j:
        if j - i < k:
            i += 1
            j = len(nums) - 1
        elif j - i > k:
            j -= 1
        else:
            if abs(nums[i] - nums[j]) == t:
                bok = True
                break
            else:
                j = len(nums) - 1
                i += 1
    return bok

print(contains_duplicate([1,2,3,1], 3, 0))
print(contains_duplicate([1,0,1,1], 1, 2))
print(contains_duplicate([1,5,9,1,5,9], 2, 3))