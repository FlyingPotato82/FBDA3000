#!/usr/bin/env python
# coding: utf-8

# In[1]:


from lxml import html
import requests
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


# In[2]:


def get_title(p):
    with open(p,encoding="utf-8") as file:
        content = file.read()
        tree = html.fromstring(content)
        title = tree.xpath('//title/text()')
        return title


# In[3]:


def get_messages(p):
    with open(p,encoding="utf-8") as file:
        content = file.read()
        tree = html.fromstring(content)
        messages = tree.xpath('//div[@class="_3-94 _2lem"]/text()')
        return messages


# In[ ]:


pathlist = Path("facebook/messages").glob('**/*.html')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    #print(path_in_str)
    get_title(path_in_str)
    get_messages(path_in_str)
    m= get_messages(path_in_str)
    from datetime import datetime
    seconds = list(map(lambda d:datetime.strptime(d, '%b %d, %Y %I:%M%p'),m))
    # data
    df=pd.DataFrame({'x': seconds , 'y': range(len(seconds),0,-1)})
 
    # plot
    plt.plot( 'x', 'y', data=df, linestyle='none', marker='o')
    plt.savefig("fbthings/"+get_title(path_in_str)[0]+"_result.png")
    plt.clf()
        
        


# In[ ]:




