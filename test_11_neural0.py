import pandas as pd
import neuralpy as ne
import random

random.seed(2016)
sample_size=50
sample = pd.Series(random.sample(range(-10000,10000),sample_size))
x=sample/10000
y=x**2

count = 0
dataSet = [([x.ix[count]],[y.ix[count]])]
count = 1
while (count < sample_size):
#    print "Working on data item: ", count
    dataSet = (dataSet+[([x.ix[count,0]], [y.ix[count]])])
    count += 1

fit = ne.Network(1, 6, 12, 1)
epochs = 5000
learing_rate = 1
print "Fitting model right now"
fit.train(dataSet, epochs, learing_rate)

count = 0
pred = []
while(count < sample_size):
    out = fit.forward(x[count])
    print 'Obs:' + str((count+1)) + '\t' + 'y=' + str(round(y[count],4)) + '\t' + 'prediction=' + str(round(pd.Series(out),4))
    pred.append(out)
    count += 1