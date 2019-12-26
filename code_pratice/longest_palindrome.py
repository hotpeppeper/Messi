'''
给定一个字符串 s，找到 s 中最长的回文子串。
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
'''

class PalindromeCenterSpread:
    def __init__(self, string):
        self.string = string
        self.length = len(string)

    def _center_spread(self, left, right):
        i = left
        j = right
        while i >= 0 and j < self.length and self.string[i] == self.string[j]:
            i -= 1
            j += 1
        return self.string[i + 1 : j], j - i - 1

    def longest_palindrome(self):
        if self.length < 2:
            return self.string
        max_len = 1
        for i in range(self.length):
            odd, odd_len = self._center_spread(i, i)
            even, even_len = self._center_spread(i, i + 1)
            palin = odd if odd_len >= even_len else even
            if len(palin) >= max_len:
                res = palin
                max_len = len(palin)
        return res

if __name__ == "__main__":
    pc = PalindromeCenterSpread('abcba')
    print(pc.longest_palindrome())