#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
authors = []   #we will create a list of UNIQUE authors
lines = sys.stdin   #input from previous mapper


# In[2]:


for line in lines:
    line = line.strip()   #to remove spaces etc
    if line not in authors:
        authors.append(line)
    else:
        pass

for author in authors:
    print(author)

