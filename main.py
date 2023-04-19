import math
import sympy
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline
# %config InlineBackend.figure_format='retina'
plt.style.use('dark_background')


def get_coordinate(num):
    return num * np.cos(num), num * np.sin(num)


def create_plot(nums, figsize=8, s=None, show_annot=False):
    nums = np.array(list(nums))
    x, y = get_coordinate(nums)
    plt.figure(figsize=(figsize, figsize))
    plt.axis("off")
    plt.scatter(x, y, s=s)

    fig, ax = plt.subplots(figsize=(10, 10))
    for num in nums:
        ax.annotate(num, (x[num], y[num]))
    plt.show()


def create_plot2(nums, figsize=8, s=None, show_annot=False):
    nums = np.array(range(20))
    x, y = get_coordinate(nums)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(x, y)
    for num in nums:
        ax.annotate(num, (x[num], y[num]))
    ax.axis("off")
    plt.show()


primes = sympy.primerange(0, 10)
create_plot2(primes)
