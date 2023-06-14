import math


def prime_numbers(n):
    if n <= 1:
        print("Por favor informe um número >=1")
    else:
        # Essa abordagem usa o crivo de Eratóstenes (O(n log n))
        # para encontrar uma lista de primos de 2 a n:
        primes = list(range(2, n+1))
        for i in range(2, (math.isqrt(n)) + 1):
            if i in primes:
                for j in range(i ** 2, n+1, i):
                    if j in primes:
                        primes.remove(j)
        return primes


def recursive_prime_numbers(n):
    # Para usar a recursão seria necessário uma função auxiliar. 
    # Por isso, optei por usar uma função lambda.
    is_prime = lambda num, divisor: True if divisor <= 1 else False if num % divisor == 0 else is_prime(num, divisor - 1)

    if n <= 1:
        print("Por favor informe um número >= 1")
        return []
    elif n == 2:
        return [2]
    else:
        primes = prime_numbers(n - 1)
        if is_prime(n, math.isqrt(n)):
            primes.append(n)
        return primes
a = prime_numbers(1000)
b = recursive_prime_numbers(1000)
print (a ==b)