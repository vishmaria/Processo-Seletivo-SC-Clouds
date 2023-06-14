def fibonacci(n):
    if n < 0:
        print("Por favor informe um número >= 0")
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def linear_fibonacci(n):
    if n < 0:
        print("Por favor informe um número >= 0")
    elif n ==0 or n == 1:
        return n
    else:
        # Nessa abordagem, a sequência dessa ser definida para 0 e para 1:
        f0 = 0
        f1 = 1
        for i in range(2, n+1):
            # fn = fn-1 + fn-2
            fn = f0 + f1
            # Passa a ser início da sequência:
            f0 = f1
            f1 = fn
        return f1

a = fibonacci(-1)
b = linear_fibonacci(-1)

print(a, b)