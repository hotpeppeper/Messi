def int_reverse(i):
    # 边界
    boud = (1<<31) * -1 if i < 0 else (1<<31)
    abs_i = abs(i)
    res = 0
    while abs_i != 0:
        res = res * 10 + abs_i % 10
        abs_i //= 10
        if res > boud:
            return 0
    return res if i > 0 else -res

print(int_reverse(123))
print(int_reverse(1234567890))
print(int_reverse(987))
print(int_reverse(123765))
