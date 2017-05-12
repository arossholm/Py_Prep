in_string = ' are not iterating through the 1 23 3535 words in the string, you are iterating through the characters in the string. To iterate through the words, you would first need to split the string into words , using str.split() , and then iterate through that . Example -'
i = 0
for c in in_string:
    #print c, i
    i += 1
i = 0
w_old = 'a'
for w in in_string.split(" "):
    #print w, i
    i += 1
    if w_old < w:
        w_old = w
    print w_old


print('test stuff')

Adict = {"first":1,"second":2}
print(Adict.keys())

Atuple = ('1',2,'sdfhsfdghf')
print(Atuple[2])

Alist = [2,2,2,2,2]

Aset = set([1,3,4,32,5,3221,1])
print Aset

print(Alist[3])


a_dict = {}
a_dict = {"first": 1}
print a_dict
a_dict["second"] = [2]
print a_dict
a_dict.update({'third':3})
print a_dict
a_dict["second"].append(222)
print a_dict
print a_dict["second"]
print a_dict.keys()
print a_dict.values()
print a_dict.items()