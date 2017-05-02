# A Dynamic Programming based Python Program for the Egg Dropping Puzzle
# http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
INT_MAX = 32767

def eggDrop(n, k):
    # A 2D table where entery eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]
    print("eggFloor")
    print(eggFloor)
    # We need one trial for one floor and 0 trials for 0 floors
    for i in range(1, n + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
    print("eggFloor2")
    print(eggFloor)
    # We always need j trials for one egg and j floors.
    for j in range(1, k + 1):
        eggFloor[1][j] = j
    print("eggFloor3")
    print(eggFloor)
    # Fill rest of the entries in table using optimal substructure
    # property
    # eggFloor[egg(i)][floor(j)]
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            eggFloor[i][j] = INT_MAX
            for x in range(1, j + 1):
                res = 1 + max(eggFloor[i - 1][x - 1], eggFloor[i][j - x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res
                print (eggFloor)

    # eggFloor[n][k] holds the result
    print("eggFloor Resultat")
    print (eggFloor)
    return eggFloor[n][k]


print(eggDrop(2,10))