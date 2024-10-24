import math

def is_perfect(n):
    divisors_sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n and n != 1


perfect_numbers = [n for n in range(2, 1000000) if is_perfect(n)]
print(perfect_numbers)
