#Two different way to acheive Fibonacci. Recursive is much slower.
def Fibo_0(x):#Recursive
    if x < 0:
        print 'Error'
        return -1
    if x < 3:
        return 1
    else:
        return Fibo_0(x-2) + Fibo_0(x-1)

def Fibo_1(x):#Classic
    i = 1
    j = 1
    k = 1
    if x < 0:
        print 'Error'
        return -1
    else:
        while (x - 2) > 0:
            k = i + j
            i = j
            j = k
            x = x - 1
        return k
