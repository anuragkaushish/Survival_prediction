# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:02:01 2020

@author: Anurag
"""

import numpy as np
import matplotlib.pyplot as plt

x= np.arange(1,50)
y= np.arange(1,50)

plt.scatter(x,y,c= 'b')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Graph in 2D')
