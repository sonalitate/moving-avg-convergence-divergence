# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 15:55:32 2018

@author: Exam
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from pandas.stats.moments import ewma
os.chdir("C:\\pydata\\")
data=pd.read_csv('TCS.csv')

red=ewma(data.Close,span=26)
red2=ewma(data.Close,span=12)
fred=red-red2
blue=ewma(fred,span=9)
crossover=fred-blue

plt.plot(blue)
plt.plot(fred)
plt.plot(crossover)
plt.show()