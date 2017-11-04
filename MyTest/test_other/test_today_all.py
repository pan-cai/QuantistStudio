
# coding: utf-8

# In[2]:


#! _*_ coding:utf-8 _*_
import pandas as pd
import tushare as ts
import pymysql
from sqlalchemy import create_engine


# In[3]:


#connect mysql
engine = create_engine('mysql+pymysql://root:caicai520@127.0.0.1/QuantistStudio?charset=utf8')


# In[6]:


today_all = pd.read_sql_table('today_all',engine)
today_all


# In[7]:


today_all.info()


# In[8]:


today_all.describe()


# In[10]:


today_all.groupby('code')['change'].sum().describe()


# In[ ]:


#先建立一个Dataframe
sale_area=pd.DataFrame(sale.groupby("地区名称")["利润"].sum()).reset_index()
#设置bins,和分组名称
bins=[-10,7091,10952,17656,37556]
groups=["较差","中等","较好","非常好"]
#使用cut分组
#sale_area["分组"]=pd.cut(sale_area["利润"],bins,labels=groups)


# In[13]:


today_all.loc[today_all['change']<1.09,'lable']='bad'
today_all.loc[today_all['change']>=1.09,'lable']='good'
today_all

