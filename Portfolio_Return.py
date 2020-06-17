#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


tickers=['FESA4.SA','AGRO3.SA']
new_data=pd.DataFrame()
for t in tickers:
    new_data[t]=wb.DataReader(t,data_source='yahoo',start='2019-10-1')['Adj Close']
new_data


# In[3]:


(new_data/new_data.iloc[0]*100).plot(figsize=(15,6))
plt.legend()
plt.grid()
plt.show()


# In[4]:


retorno=(new_data/new_data.shift(1))-1
peso=np.array([0.5,0.5])
array_port=np.dot(retorno,peso)
array_port


# In[9]:


df_port=pd.DataFrame(array_port)
df_port=np.log(1+df_port)
df_port=df_port.cumsum()
df_port=(df_port+1)*100
df_grafico=(new_data/new_data.iloc[0]*100)
df_grafico.insert(loc=2,column='Retorno da Carteira',value=df_port[0].to_list())

df_grafico.plot(figsize=(15,6),color=['yellow','yellow','green'])
plt.legend()
plt.grid(True)
plt.show()

