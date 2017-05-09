import random
import numpy as np
def pairSum2(arr, k):
    if len(arr)<2:
        return
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )
    print '\n'.join( map(str, list(output)) )
    print((output))
    print(list(output))

arr = np.random.randint(-9, 9, 20)
print(arr)
pairSum2(arr,6)