a = []
with open ('GLD.txt', 'r') as f:
    a = f.readlines()

def prediction(n):
    pass
    if n == len(a):
        return float(a[-1])
    elif n < len(a):
        return float(a[n])
    else:
#        return get_moving_average(2) * 1.093 - get_moving_average(9) * 0.096 + 0.36
        return (((prediction(n-1) + prediction(n-2) / 2) * 1.093) - ((prediction(n-2) + prediction(n-3) + prediction(n-4) + prediction(n-5) + prediction(n-6) + prediction(n-7) + prediction(n-8) + prediction(n-9) + prediction(n-1) / 9) * 0.096) + 0.36)
#        c = (get_moving_average(2) * 1.093) - (get_moving_average(9) * 0.096) + 0.36

def get_moving_average(x):
    pass
    b = a[-x:]
    c = 0
    for i in range(len(b)):
        c = c + float(b[i])
    return c / x

#print get_moving_average(2811)
print prediction(0)