#!/usr/bin/env python3

import decimal

def highlight_differences(a, b):
    if len(a) != len(b):
        raise ValueError('Strings must be of the same length')

    result = ''

    for char_a, char_b in zip(a, b):
        if char_a != char_b:
            result += f'\033[91m{char_a}\033[0m'  # ANSI escape code for red text
        else:
            result += char_a

    return result

def nth_hex_digit_of_pi(n):
    decimal.getcontext().prec = n + 2  # Set precision to calculate n+1 digits
    decimal.getcontext().rounding = decimal.ROUND_FLOOR

    pi = decimal.Decimal(0)

    for k in range(n + 1):
        term1 = decimal.Decimal(1) / 16**k
        term2 = decimal.Decimal(4) / (8*k + 1)
        term3 = decimal.Decimal(2) / (8*k + 4)
        term4 = decimal.Decimal(1) / (8*k + 5)
        term5 = decimal.Decimal(1) / (8*k + 6)

        term = term1 * (term2 - term3 - term4 - term5)
        prev = str(pi)
        pi += term

        print(term)
        now = str(pi)
        ml = max(len(prev), len(now))
        prev = prev.rjust(ml, ' ')
        now = now.rjust(ml, ' ')
        result = highlight_differences(now, prev)
        print(result)

    hex_pi = format(int(pi * 16), f'x')  # Convert to hexadecimal
    return (pi, hex_pi[-1])

# Example: Compute the 100th hexadecimal digit of Pi
for n in range(2, 100):
    result, hex_pi = nth_hex_digit_of_pi(n)
    l = len(str(result))
    verify = decimal.Decimal(open('pi1000000.txt', 'r').read(l))
    correct = 0
    for a, b in zip(str(result), str(verify)):
        if a == b:
            correct += 1
        else:
            break
    print(correct)
    #result = highlight_differences(str(result), str(verify))
    print(f"The {n}th hexadecimal digit of Pi is: {result}")
