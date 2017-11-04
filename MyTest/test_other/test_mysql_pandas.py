
# coding: utf-8

# In[1]:


#! _*_ coding:utf-8 _*_
import pandas as pd
import tushare as ts
import pymysql
from sqlalchemy import create_engine


# In[2]:


#connect mysql
engine = create_engine('mysql+pymysql://root:caicai520@127.0.0.1/QuantistStudio?charset=utf8')


# In[4]:


df = pd.DataFrame({'A':[1,2,3],'B':['a','b','c']})
df.to_sql('test_dataframe',engine,index=False)
pd.read_sql_table('test_dataframe',engine)


# In[6]:


pd.read_sql_query('select * from test_dataframe',engine)


# In[8]:


pd.read_sql_table('indexs',engine,index_col='code')


# In[9]:


pd.read_sql_table('indexs',engine,columns=['open','close'])


# In[10]:


for chunk in pd.read_sql_query('select * from indexs', engine,chunksize=5):
    print(chunk)


# In[13]:


from pandas.io import sql
sql.execute('insert into test_dataframe values (?,?)',engine,params=[(1,'c')])
sql.execute('select * from test_dataframe',engine)

