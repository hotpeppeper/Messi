import math


def is_palinndrome(x):
    if x < 0 and (x > 0 and x % 10 == 0):
        return False
    elif x == 0:
        return True
    else:
        str_x = str(x)
        len_x = len(str_x)
        i = 0
        j = len_x - 1
        is_ = True
        while i <= j:
            if str_x[i] != str_x[j]:
                is_ = False
                break
            i += 1
            j -= 1
        return is_

def is_palinndrome2(x):
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    elif x == 0:
        return True
    else:
        bit_x = int(math.log10(x))
        len_x = bit_x + 1
        i = 0
        is_ = True
        while i < len_x / 2:
            r = x // (10**bit_x)
            l = x % 10
            if r != l:
                is_ = False
                break
            x = x - r*10**bit_x
            x = int(x / 10)
            bit_x -= 2
            i += 1
        return is_

def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    revnum = 0
    while(x>revnum):
        revnum = revnum*10 + x % 10
        x = x // 10
    return x == revnum or x == revnum//10


if __name__ == "__main__":
    aa = [-12321, 1234321, 123676321, 123456, 1221]
    for i in aa:
        print(is_palinndrome2(i))
    print(isPalindrome(111999111))