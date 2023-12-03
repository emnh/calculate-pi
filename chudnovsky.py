#!/usr/bin/env python3

# The time complexity of the algorithm is O(n(log n)^3)

import timeit
import decimal
import matplotlib.pyplot as plt

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

    # Display the plot
    plt.show()


retval = None
def calc(n):
    global retval
    retval = chudnovsky(n)  # 3.141592653589793238462643384
    return retval

decimal.getcontext().prec = 10
m = 100
x = []
y = []
for i in range(2, m):
    # Time the function and print the result
    elapsed_time = timeit.timeit(lambda: calc(i), number=1)
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
    dps = round(correct / elapsed_time)
    print(dps, "digits/second",
          correct, "digits",
          decimal.getcontext().prec, "precision")
    if correct * 2 >= decimal.getcontext().prec:
        decimal.getcontext().prec *= 2
    x.append(i)
    y.append(dps)
plot(x, y)
