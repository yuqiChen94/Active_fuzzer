#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from datetime import datetime

df=pd.read_csv("log/0712LIT301.Pv.csv")
out=[datetime.strptime(x,' %d/%m/%Y %I:%M:%S %p') for x in df[" Timestamp"].tolist()]
flag=0
for i in range(len(out)):
    if(out[i]==datetime(2019,7,12,9,52,40)):
        flag = i
        break
df_out=df.iloc[flag:, 2:4]
df_out.to_csv("log/0712LIT301.csv")
