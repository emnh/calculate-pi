#!/usr/bin/env python3

# The time complexity of the algorithm is O(n(log n)^3)

import timeit
import decimal
import matplotlib.pyplot as plt
from decimal import Decimal
from decimal import getcontext
from pi_chudnovsky_bs_gmpy import pi_chudnovsky_bs

def pi(precision):
    getcontext().prec=precision
#     return sum(1/Decimal(16)**k *
#         (Decimal(4)/(8*k+1) -
#          Decimal(2)/(8*k+4) -
#          Decimal(1)/(8*k+5) -
#          Decimal(1)/(8*k+6)) for k in range (precision))
    k = precision
    return sum(1/Decimal(16)**k *
        (Decimal(4)/(8*k+1) -
         Decimal(2)/(8*k+4) -
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)))

def binary_split(a, b):
    if b == a + 1:
        Pab = -(6*a - 5)*(2*a - 1)*(6*a - 1)
        Qab = 10939058860032000 * a**3
        Rab = Pab * (545140134*a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)

        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab


def chudnovsky(n):
    P1n, Q1n, R1n = binary_split(1, n)
    return (426880 * decimal.Decimal(10005).sqrt() * Q1n) / (13591409*Q1n + R1n)

def splot(x, y):
    # Create a scatter plot
    plt.scatter(x, y)

    # Add labels and title
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Scatter Plot of x and y')

    # Display the plot
    plt.show()

def plot(x, y):
    # Create a scatter plot
    plt.plot(x, y, marker='o', linestyle='-')

    # Add labels and title
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Scatter Plot of x and y')

retval = None
def calc1(n):
    global retval
    retval = chudnovsky(n)  # 3.141592653589793238462643384
    return retval

retval = None
def calc2(n):
    global retval
    retval = pi_chudnovsky_bs(n)  # 3.141592653589793238462643384
    #retval /= 10 ** len(retval - 1)
    retval = str(retval)
    retval = '3.' + retval[1:]
    #retval = decimal.Decimal(str(retval)) / (10 ** len(retval - 1))
    return retval

mycalc = False
if mycalc:
    calc = calc1
else:
    calc = calc2

decimal.getcontext().prec = 100
m = 1000
x = []
y = []
z = []
odigits = 0
maxdiff = 16
i = 2
#for i in range(2, m, 10):
while True:
    i *= 2
    decimal.getcontext().prec = i * 15
    if mycalc:
        precision = decimal.getcontext().prec
    else:
        precision = i
    # Time the function and print the result
    elapsed_time = timeit.timeit(lambda: calc(i), number=1)
    #print(retval)
    #elapsed_time = timeit.timeit(lambda: pi_chudnovsky_bs(precision), number=1)
    if elapsed_time >= 20:
        break
    ls = str(retval)
    l = len(ls)
    verify = decimal.Decimal(open('pi1000000.txt', 'r').read(l))
    #print(f"Elapsed Time: {elapsed_time} seconds, Pi: {retval}")
    #print(retval)
    #print(verify)
    correct = 0
    for a, b in zip(str(retval), str(verify)):
        if a == b:
            correct += 1
        else:
            break
    if not mycalc:
        correct = i
    dps = round(correct / elapsed_time)
    pps = round(precision / elapsed_time)
    diffdigits = correct - odigits
    odigits = correct
    #e2 = timeit.timeit(lambda: pi(len(ls)), number=1)
    #print("cmp", ls[-1], pi(len(ls)), e2)
    print(i, "chudnovsky iterations",
          dps, "digits/second",
          round(dps / pps, 2), "digits/second / precision/second",
          correct, "digits",
          diffdigits, "diffdigits",
          decimal.getcontext().prec, "precision")
    if mycalc and correct >= precision:
        print("precision error")
        break
#     if correct + maxdiff >= decimal.getcontext().prec:
#         decimal.getcontext().prec += maxdiff
    x.append(elapsed_time)
    y.append(correct)
    #x.append(i)
    #y.append(dps)
    #z.append(pps)
plot(x, y)
#plot(x, z)
# Display the plot
plt.show()
