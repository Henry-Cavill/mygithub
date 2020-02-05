def Fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(n-1):
        a, b = b, a+b
    return a


if __name__ == '__main__':
    n = Fibonacci(1000)
    print(n)
