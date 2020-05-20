
'''
给定一个数组，返回数组的最大和，及开始和结束的位置
'''
def max_subsequence(seq):
    max_val = 0
    this_val = 0
    max_start = 0
    max_end = 0
    for i, val in enumerate(seq):
        this_val += val
        if this_val > max_val:
            max_val = this_val
            max_end = i
        elif this_val < 0:
            this_val = 0
            # 第i个数是小于0的，指向下一个数
            max_start = i + 1
    return max_val, (max_start, max_end)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


list_a = [1, -2, 4, -6, 50, -4, -4, -10, -20, 40, -1, -2, -4, -1, -5, -1]
list_b = [-2,1,-3,4,-1,2,1,-5,4]
a, b = max_subsequence(list_b)
print(a, b)