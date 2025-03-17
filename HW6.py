import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self, func):
        self.func = func
        self.h = 1e-5

    def __call__(self, x):
        return (self.func(x + self.h) - self.func(x - self.h)) / (2 * self.h)

    def __get__(self, instance, owner):
        return self

class ExponentialFunction:
    def __init__(self, a):
        self.a = a
        self.derivative = Derivative(self)

    def __call__(self, x):
        return self.a * np.exp(x)

exp_func = ExponentialFunction(a=1)

x_values = np.linspace(-2, 2, 400)
f_values = exp_func(x_values)
f_prime_values = exp_func.derivative(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, f_values, label='f(x) = e^x')
plt.plot(x_values, f_prime_values, label="f'(x)")
plt.title('Графики функции и её производной')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()