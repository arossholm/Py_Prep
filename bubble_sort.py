def bubble_sort(in_list):
    swap = True
    N = len(in_list)
    NoR = 0
    while swap:
        swap = False
        for N_pros in range(N):
            for i in range(N_pros-1):
                if in_list[i] > in_list[i+1]:
                    in_list[i+1], in_list[i] = in_list[i], in_list[i+1]
                    swap = True
                    NoR += 1
    print("NoR = {}" .format(NoR))
    return in_list



in_list = [5, 2, 4, 332, 6, 5, 7, 8, 433, 6, 7, 9, 554, 3, 466, 5, 0]
print in_list
print bubble_sort(in_list)



