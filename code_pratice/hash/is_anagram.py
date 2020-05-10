
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_dict = dict()
    for char in s:
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1

    for char in t:
        if char in s_dict:
            s_dict[char] -= 1

    b_res = True
    for _, v in s_dict.items():
        if v != 0:
            b_res = False
            break
    return b_res

ss = [['anagram', 'naagram'], ['rat', 'cat']]
for s in ss:
    print(is_anagram(s[0], s[1]))