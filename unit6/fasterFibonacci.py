#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci_r(n, f=[0, 1]):
    return fibonacci_r(n-1, [ f[1], f[0]+f[1] ]) if n > 0 else f[0]

def fibonacci(n, f=[0, 1]):
    while n > 0:
        f, n = [f[1], f[0]+f[1]], n-1
    return f[0]

print(fibonacci(36))
#>>> 14930352
print(fibonacci(1))
#>>> 1
print(fibonacci(0))
#>>> 0