import sys
import numpy as np


def fib(n):
    a, b = 1,1
    for i in range(n - 2):
        newb = a + b
        a = b
        b = newb
        #a, b = b, a + b
    return b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binary_search(data, target, data_low, data_high):
    print('TBA')

    print("Data min = {} Data high = {}" .format(data_low, data_high))

    """
    Return True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """

    if data_low > data_high:
        return False # interval is empty; no match
    else:
        print(data_low + data_high)
        mid = (data_low + data_high) // 2
        print(mid)

    if target == data[mid]: # found a match
        print("place found = {}" .format(mid) )
        return True

    elif target < data[mid]:
        # recur on the portion left of the middle
        return binary_search(data, target, data_low, mid-1)
    else:
    # recur on the portion right of the middle
        return binary_search(data, target, mid+1, data_high)



def fibonacci_dyn(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci_dyn(n - 1) + fibonacci_dyn(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


# Driver Program



FibArray = [0,1]
def main(argv):
    print("Fractional of {} = {}".format(5, factorial(5)))

    print("Fibonachi in for loop n = {} => {}" .format(15, fib(15)))
    sorted_array = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    print("Input array:\n{}".format(sorted_array))
    data_low = 0
    data_high = len(sorted_array)
    binary_search(sorted_array, 12, data_low, data_high)
    pass

    n_fib = 22
    #global FibArray
    FibArray = [0] * n_fib
    print('fibonacci_dyn(n_fib) {}' .format(fibonacci_dyn(n_fib)))


if __name__ == "__main__":
    main(sys.argv)