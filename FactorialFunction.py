import sys
import numpy as np


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binary_search(data, target):
    print('TBA')
    data_min = np.min(data)
    print(data_min)

def main(argv):
    print("Fractional of {} = {}".format(5, factorial(5)))

    sorted_array = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    print("Input array:\n{}".format(sorted_array))

    binary_search(sorted_array, 12)
    pass

if __name__ == "__main__":
    main(sys.argv)