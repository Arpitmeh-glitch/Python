def fibonacci(n, a=0, b=1):
    if n <= 0:
        return
    print(a)
    fibonacci(n - 1, b, a + b)