#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np
import sys


# In[44]:


support_total = 500
totalsize = 302
chunksize = 215
support_chunk = support_total * chunksize/totalsize


# In[45]:

count=0
dic = {}
lines = sys.stdin 
for author in lines:
    author = author.strip()      									# findind authors with their occurance in each chunksize
    if author[11:-1] != 'null' and author[11:-1] not in dic and author[0:3] != '},{':           #making a unique dic of authors
        dic[author[11:-1]] = 1
    elif author[11:-1] != 'null' and author[11:-1] in dic and author[0:3] != '},{':          # if already present, just increase count
        dic[author[11:-1]] += 1
    else:                                                   # else just pass
        pass       
                                                 
for i in list(dic.keys()):                                  # remove those with support < support threshold for 1 chunk
    if dic[i] < support_chunk:
        del dic[i]

for i in list(dic.keys()):                                  #print all the candidate set (may contain duplicates at this stage)
    print(i)
