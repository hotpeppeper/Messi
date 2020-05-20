# 记录中间状态减少重复计算
fib_table = dict()
def fibonacci(n):
    if n <= 1:
        return n
    if n not in fib_table:
        fib_table[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_table[n]

def fibonacci_dp(n):
    if n == 0 or n == 1:
        return 1
    fib = [0] * (n+1)
    fib[1] = fib[2] = 1
    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def fibonacci_dp2(n):
    if n <= 1:
        return 1
    pre = cur = 1
    for i in range(3, n+1):
        tmp = cur + pre
        pre = cur
        cur = tmp
    return cur

print(fibonacci_dp2(10))
print(fibonacci(10))
print(fib_table)