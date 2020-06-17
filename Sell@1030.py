#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


petro=wb.DataReader('PETR4.SA',data_source='yahoo',start='2015-1-1')
petro.head()


# In[3]:


petro['Log Return'] = np.log(petro['Open']/petro['Close'].shift(1))



petro['Return']=petro[['Log Return']].cumsum(axis=0)

(100+100*petro['Return']).plot(figsize=(15,6),label='Retorno Sell@10:30')
(petro['Adj Close']/petro['Adj Close'].iloc[0]*100).plot(label='Retorno Buy and Hold')
plt.grid(True)
plt.legend()
plt.show()


# In[ ]:




