import collections
a = [1,2,3,1,2,3,4,1,2,5,4,6,7,7,8,9,6,2,23,4,2,1,5,6,7,8,2]
b = collections.Counter(a)
for c in b:
       print  c,b[c]