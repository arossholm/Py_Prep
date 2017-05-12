def fib(n):
    a, b = 1,1
    for i in range(n - 2):
        newb = a + b
        a = b
        b = newb
        #a, b = b, a + b
    return b

def fibonacci_dyn(n):
    if n < 0:
        print("Incorrect input")
    elif n < 2:
        return FibArray[n]
    else:
        temp_fib = fibonacci_dyn(n - 1) + fibonacci_dyn(n - 2)
        FibArray.append(temp_fib)
    return temp_fib


# Driver Program

def fibonacci_dyn2(n):
    if n < 2:
        Fib_array2[n] = 1
    elif Fib_array2[n] == 0:
        Fib_array2[n] = fibonacci_dyn2(n-1) + fibonacci_dyn2(n-2)
    return Fib_array2[n]



Fib_array2 = [0]*200
FibArray = [1,1]
n_fib = 40
print("Fibonachi in for loop n = {} => {}" .format(15, fib(15)))
#print('fibonacci_dyn({}) {}' .format(n_fib,fibonacci_dyn(n_fib)))
print('fibonacci_dyn2({}) {}' .format(n_fib,fibonacci_dyn2(n_fib)))