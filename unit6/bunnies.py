# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

'''0,1,1,2,3,5,8,13,21,34,55,89,144,...'''

def fibonacci(n, f=[0, 1]):
    return fibonacci(n-1, [ f[1], f[0]+f[1] ]) if n > 0 else f[0]

# def fibonacci2(n):
#     return fibonacci(n-1) + fibonacci(n-2) if not n < 2 else n
    
print(fibonacci(0))
#>>> 0
print(fibonacci(1))
#>>> 1
print(fibonacci(15))
#>>> 610
print(fibonacci(24))
print(fibonacci(36))