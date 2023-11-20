def sum_divisors(number):
    total = 0
    divisor = 1

    if number < 1:
        return 0

    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1  # This line should be inside the while loop

    return total

print(sum_divisors(0))  # 0
print(sum_divisors(3))  # 1
print(sum_divisors(36))  # 55
print(sum_divisors(102))  # 1 + 2 + 3 + 6 + 17 + 34 + 51 = 114