def is_prime(n):
    if 1 < n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
  
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True 

prime_factors = []
for number in range(2, 775147):
    if is_prime(number) and (600851475143 / number).is_integer():
        prime_factors.append(number)

print(max(prime_factors))
