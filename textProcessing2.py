in_string = '315098750 #/&()))) ..,,;;::--____  are not iterating through the 1 23 3535 words in the string, you are iterating'
i = 0
for c in in_string:
    if ord(c) > 65 and ord(c) < 123:
        print i, c, ord(c)
    i += 1
i = 0
w_old = 'a'
for w in in_string.split(" "):
    #print w, i
    i += 1
    if w_old < w:
        w_old = w
    print w_old


