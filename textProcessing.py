in_string = 'ou are not iterating through the 1 23 3535 words in the string, you are iterating through the characters in the string. To iterate through the words, you would first need to split the string into words , using str.split() , and then iterate through that . Example -'
i = 0
for c in in_string:
    #print c, i
    i += 1
i = 0
w_old = 'old'
for w in in_string.split(" "):
    #print w, i
    i += 1
    if w_old > w:
        print w_old
    else:
        w_old = w
