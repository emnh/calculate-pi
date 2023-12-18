#!/usr/bin/env python3

from decimal import Decimal, getcontext

def gauss_legendre_pi(digits):
    getcontext().prec = digits + 2  # Set precision for Decimal arithmetic

    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    print(digits // 14 + 1)
    #for _ in range(digits // 14 + 1):
    for _ in range(25):
        a_next = (a + b) / Decimal(2)
        b = (a * b).sqrt()
        t -= p * (a - a_next) * (a - a_next)
        a = a_next
        p *= Decimal(2)

    pi = (a + b) ** 2 / (Decimal(4) * t)
    return str(pi)[:-1]  # Convert Decimal to string and remove the trailing 'L'

# Example usage:
#decimal_places = 45000000  # Set the desired number of decimal places
decimal_places = 450000  # Set the desired number of decimal places
pi_value = gauss_legendre_pi(decimal_places)
print(f"Pi to {decimal_places} decimal places:\n{pi_value}")

