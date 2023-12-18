#!/usr/bin/env python3

import decimal

def nth_hex_digit_of_pi(n):
    decimal.getcontext().prec = n + 2  # Set precision to calculate n+1 digits
    decimal.getcontext().rounding = decimal.ROUND_FLOOR

    pi = decimal.Decimal(0)
    k = 0

    while True:
        term1 = decimal.Decimal(1) / 16**k
        term2 = decimal.Decimal(4) / (8*k + 1)
        term3 = decimal.Decimal(2) / (8*k + 4)
        term4 = decimal.Decimal(1) / (8*k + 5)
        term5 = decimal.Decimal(1) / (8*k + 6)

        term = term1 * (term2 - term3 - term4 - term5)
        pi += term

        if term == 0:
            break

        k += 1

    hex_pi = format(int(pi * 16), f'x')  # Convert to hexadecimal
    return hex_pi[-1]

# Example: Compute the 100th hexadecimal digit of Pi
#n = 100
for n in range(1, 100):
    result = nth_hex_digit_of_pi(n)
    print(f"The {n}th hexadecimal digit of Pi is: {result}")
