'''
给定两个数组，编写一个函数来计算它们的交集。
'''

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))