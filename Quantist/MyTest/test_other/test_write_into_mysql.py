
# coding: utf-8

# In[1]:


#! _*_ coding:utf-8 _*_
import tushare as ts
import pymysql
from sqlalchemy import create_engine


# In[16]:


#connect mysql
engine = create_engine('mysql+pymysql://root:caicai520@127.0.0.1/QuantistStudio?charset=utf8')


# In[24]:


today_all = ts.get_today_all()
# print("success getting today_all")
sh = ts.get_hist_data("sh")
sz = ts.get_hist_data("sz")
hs300 = ts.get_hist_data("hs300")
sz50 = ts.get_hist_data("sz50")
zxb = ts.get_hist_data("zxb")
cyb = ts.get_hist_data("cyb")
indexs = ts.get_index()
print("over")


# In[25]:


basic_list = ["today_all","sh","sz","hs300","sz50","zxb","cyb","indexs"]
for basic in basic_list:
    index.to_sql(basic,engine,if_exists='append')
    print(basic + " over")


# In[ ]:


ts.get_tick_data("603618",date="2017-01-09")#history tick


# In[ ]:


realtime = ts.get_realtime_quotes("603618")
realtime2 = ts.get_realtime_quotes(["sh","zs","hs300","sz50","zxb","cyb"])


# In[ ]:





# In[ ]:


# basic information
cash_flow = ts.get_cashflow_data(2017,1)
debtpaying = ts.get_debtpaying_data(2017,1)
growth = ts.get_growth_data(2017,1)
operation = ts.get_operation_data(2017,1)
profit = ts.get_profit_data(2017,1)
report = ts.get_report_data(2017,2)

