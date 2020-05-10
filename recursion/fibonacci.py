# 记录中间状态减少重复计算
fib_table = dict()
def fibonacci(n):
    if n <= 1:
        return n
    if n not in fib_table:
        fib_table[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_table[n]

print(fibonacci(6))
print(fib_table)