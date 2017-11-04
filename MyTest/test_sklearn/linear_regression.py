
# coding: utf-8

# In[10]:


# _*_ coding:utf-8 _*_
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[5]:


X = [[6],[8],[10],[14],[18]]
Y = [[7],[9],[13],[17.5],[18]]
plt.figure()
plt.title("Pizza price plotted against diameter")
plt.xlabel("Diameter in inches")
plt.ylabel("Price in dollars")
plt.plot(X, Y, "k.")
plt.axis([0,25,0,25])
plt.grid(True)
plt.show()


# In[10]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,Y)
print("pizza should cost:$%.2f"%model.predict([12]))


# In[16]:


print("Residual sum of squares: %.2f"%np.mean((model.predict(X)-Y)**2))


# In[33]:


from __future__ import division
xbar = (6+8+10+14+18)/5
variance = ((6-xbar)**2 + (8-xbar)**2 + (10-xbar)**2 + (14-xbar)**2  + (18-xbar)**2 ) / 4
print("variance = {0}".format(variance))
variance2 = np.var([6,8,10,14,18],ddof=1) #23.2
print(" variance_with_var = {0} ".format(variance2))

xbar = (6+8+10+14+18)/5
ybar = (7+9+13+17.5+18)/5
cov = ((6-xbar)*(7-ybar) + (8-xbar)*(9-ybar) + (10-xbar)*(13-ybar) + (14-xbar)*(17.5-ybar) + (18-xbar)*(18-ybar)) / 4
print(cov)
cov2 = np.cov([6,8,10,14,18],[7,9,13,17.5,18])[0][1] #22.65
print(cov2)

beta = cov2 / variance2 
print(beta) #0.976


# In[34]:


X = [[6],[8],[10],[14],[18]]
Y = [[7],[9],[13],[17.5],[18]]
X_test = [[7],[9],[11],[16],[12]]
Y_test = [[11],[8.5],[15],[18],[11]]
model = LinearRegression()
model.fit(X,Y)
print("R-squared:%.4f"%model.score(X_test,Y_test))


# In[40]:


from numpy.linalg import inv
from numpy import dot, transpose
X = [[1,6,2],[1,8,1],[1,10,0],[1,14,2],[1,18,0]]
Y = [[7],[9],[13],[17.5],[18]]
print(dot(inv(dot(transpose(X),X)),dot(transpose(X),Y)))


# In[44]:


from numpy.linalg import lstsq
X = [[1,6,2],[1,8,1],[1,10,0],[1,14,2],[1,18,0]]
Y = [[7],[9],[13],[17.5],[18]]
print(lstsq(X,Y)[0])


# In[ ]:


from sklearn.linear_model import LinearRegression
X = [[6,2],[8,1],[10,0],[14,2],[18,0]]
Y = [[7],[9],[13],[17.5],[18]]
model = LinearRegression()
model.fit(X,Y)

X_test = [[8,2],[9,0],[11,2],[16,2],[12,0]]
Y_test = [[11],[8.5],[15],[18],[11]]

predictions = model.predict(X_test)
for i,prediction in enumerate(predictions):
    print("Predictes:%s,Target:%s"%(prediction,Y_test[i]))
print("R-squared:%.2f"%model.score(X_test,Y_test))

