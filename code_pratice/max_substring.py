'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''

def max_substring(string):
    if string == '' or len(string) == 0:
        return 0
    res = j = 0
    lookup = dict()
    for i, s in enumerate(string):
        if s in lookup:
            j = lookup[s]
        res = max(res, i - j + 1)
        lookup[s] = i + 1
    return res

print(max_substring('abcdefabc'))  # 6
print(max_substring('abcabcbb'))  # 3
print(max_substring('aecabaecfgaecfgh'))  # 7
