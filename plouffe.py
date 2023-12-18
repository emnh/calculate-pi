#!/usr/bin/env python3

from functools import reduce
from math import factorial, comb, ceil, log2
from decimal import getcontext, Decimal as Dec


def bernoulli(n):
    bs = [Dec(1)]
    for m in range(1, n+1):
        bs.append(1 - sum(comb(m, k)*b / (m - k + 1) for k, b in zip(range(m), bs)))
    return abs(bs[-1])

# Formula taken from Plouffe (2022): https://arxiv.org/abs/2201.12601
def pi(n):
    getcontext().prec = n
    return (2*factorial(n)/((bernoulli(n))*2**n*reduce(Dec.__mul__, [1-(1/Dec(x)**n) for x in [2, 3, 5, 7]])))**(1/Dec(n))

p = pi(1000)
print(p)
