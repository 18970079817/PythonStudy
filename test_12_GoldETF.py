# LinearRegression is a machine learning library for linear regression
from sklearn.linear_model import LinearRegression
# pandas and numpy are used for data manipulation
import pandas as pd
import numpy as np
# matplotlib and seaborn are used for plotting graphs
import matplotlib.pyplot as plt
import seaborn
# fix_yahoo_finance is used to fetch data
import fix_yahoo_finance as yf

# Read data
Df = yf.download('GLD','2008-01-01','2019-03-10')
# Only keep close columns
Df=Df[['Close']]
# Drop rows with missing values
Df= Df.dropna()
# Plot the closing price of GLD
Df.Close.plot(figsize=(10,5))
plt.ylabel("Gold ETF Prices")
plt.show()

Df['S_2'] = Df['Close'].shift(1).rolling(window=2).mean()
Df['S_9'] = Df['Close'].shift(1).rolling(window=9).mean()
Df= Df.dropna()
X = Df[['S_2','S_9']]
X.head()

y = Df['Close']
y.head()

t=.91
t = int(t*len(Df))
# Train dataset
X_train = X[:t]
y_train = y[:t] 
# Test dataset
X_test = X[t:]
y_test = y[t:]

linear = LinearRegression().fit(X_train,y_train)
print "Gold ETF Price =", round(linear.coef_[0],3), "* 2 Days Moving Average", round(linear.coef_[1],3), "* 9 Days Moving Average +", round(linear.intercept_,3)

predicted_price = linear.predict(X_test)
print type(y_test.index)
print y_test.index
predicted_price = pd.DataFrame(predicted_price,index=y_test.index,columns = ['price'])
predicted_price.plot(figsize=(10,5))
y_test.plot()
plt.legend(['predicted_price','actual_price'])
plt.ylabel("Gold ETF Price")
plt.show()

r2_score = linear.score(X[t:],y[t:])*100
print float("{0:.2f}".format(r2_score))