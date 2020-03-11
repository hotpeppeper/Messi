
roman_dict = {
                'I': 1,
                'IV': 3,
                'V': 5,
                'IX': 8,
                'X': 10,
                'XL': 30,
                'L': 50,
                'XC': 80,
                'C': 100,
                'CD': 300,
                'D': 500,
                'CM': 800,
                'M': 1000}
# 特别处理IV，IX，XL，XC，CD，CM几种情况，因为出现这几个符号是，左边的会被多加一次，所以提前减掉

def roman_to_int(s):
    res = 0
    for i, j in enumerate(s):
        str2 = s[max(i-1,0):i+1]
        res += roman_dict.get(str2, roman_dict[j])
    return res

if __name__ == "__main__":
    strs = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
    for s in strs:
        print(roman_to_int(s))

    # output 3,4,9,58,1994