
'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

> 示例：

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

def two_sum(nums, dest):
    look_up = dict()
    for i, num in enumerate(nums):
        if dest - num in look_up:
            return [look_up[dest - num], i]
        # 记录当前数和位置
        look_up[num] = i
    return []


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 11, 9]
    dest = 10
    a = two_sum(nums, dest)
    print(a)
