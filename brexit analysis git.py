
# coding: utf-8

# In[1]:

import pandas as pd
import scipy as sp
from pandas import DataFrame as df
import json
import requests
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


# In[2]:

r = requests.get('https://petition.parliament.uk/petitions/131215.json')


# In[3]:

json_pd=(pd.read_json(r.content))


# In[4]:

df2=json_pd["data"][0]["signatures_by_country"]


# In[5]:

df_list=df(df2)[['name','signature_count']]


# In[6]:

df_list.to_csv(r'C:\Users\Mike\Documents\brexit.csv', sep=',')


# In[7]:

df_list.sort('signature_count', ascending=False).head(20)

