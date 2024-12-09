from matplotlib import pyplot as plt
import os
import numpy as np

'''dz nomer 1'''

dir = os.getcwd()
x = np.linspace(-2, 2, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    y = (x ** b + a ** b) / x ** b
    y[y > 20] = np.nan
    y[y < -20] = np.nan
    return y


plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='red')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='green')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()
plt.savefig(dir + '/dz9nomer1.png', dpi=300)
plt.show()

'''dz nomer 2'''

dir = os.getcwd()
x = np.linspace(0, 5, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    y = (x ** b + a ** b) / x ** b
    y[y > 20] = np.nan
    y[y < -20] = np.nan
    return y


plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='red')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='green')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()

plt.axes([0.35, 0.60, 0.25, 0.25])
x = np.linspace(0, 0.5, 1000)
plt.grid()
plt.title('Small x values:')
plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='red')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='green')

plt.axes([0.70, 0.30, 0.25, 0.25])
x = np.linspace(10, 20, 1000)
plt.grid()
plt.title('Big x values:')
plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='red')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='green')

plt.savefig(dir + '/dz9nomer2.png', dpi=300)
plt.show()

'''dz nomer 3'''

dir = os.getcwd()
x = np.linspace(-5, 0, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    y = (x ** b + a ** b) / x ** b
    y[y > 20] = np.nan
    y[y < -20] = np.nan
    return y


plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='red')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='green')
plt.plot(x, [0] * len(x), label='f(x)=0', color='black')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()

plt.axes([0.21, 0.17, 0.50, 0.25])


def f(x, a, b):
    y = (x ** b + a ** b) / x ** b
    y[y > 3] = np.nan
    y[y < -3] = np.nan
    return y


x = np.linspace(-5, 0, 1000)
plt.grid()
plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='red')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='green')
plt.plot(x, [0] * len(x), label='x=0', color='black')

plt.savefig(dir + '/dz9nomer3.png', dpi=300)
plt.show()
