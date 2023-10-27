#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import sys
authors = {}   #we will create a list of UNIQUE authors
lines = sys.stdin   #input from previous reducer1

for line in lines:
    line = line.strip()
    print(line)
    word,count=line.split('\t')
    count=int(count)
    
    if word not in authors:
        authors[word]=count
        
    else:
        authors[word]=authors[word]+1
       
lis1=[]
lis2=[]
for i in authors:
    if authors[i] >= 500:
        lis1.append(i)
        lis1.append(authors[i])
        lis2.append(lis1)
        lis1=[]
        
df = pd.DataFrame(lis2,columns=['Author(s)','frequency'])
df.to_csv('Result.csv')
