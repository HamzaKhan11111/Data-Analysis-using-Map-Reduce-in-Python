#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import json
import sys
authors = []   #we will create a list of UNIQUE authors
lines = sys.stdin   #input from previous reducer1

for line in lines:
    line = line.strip()   #to remove spaces etc
    if line not in authors:
        authors.append(line)

fil = open ('DBLP_DATA.json')
df = json.load(fil)
for i in df:
    if (str(i)[12:-2]) in authors:
        print(str(i)[12:-2],'\t',1)
