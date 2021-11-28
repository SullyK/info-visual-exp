import matplotlib.pyplot as plt # imports
from scipy.signal import savgol_filter

import numpy as np
import random
import sys

for i in range(1,11): # loops 10 times(image 1 -> image 10)
    x1 = np.random.randint(0,10, size=10) # random array, [0-9 range]
    y1 = np.random.randint(0,10, size=10) # random array, [0-9 range]
    x1 = np.sort(x1)
    y1 = np.sort(y1)
    x1 = savgol_filter(x1, 5, 2) #the smoother we want, the higher we make 2nd value(not greater than x tho)
    y1 = savgol_filter(y1, 5, 2) #using the savgol filter to clean line(with rand values)

    plt.plot(x1,y1)
    # plt.title('title name')
    # plt.xlabel('xaxis name')
    # plt.ylabel('yaxis name')
    plt.savefig('line' + str(i) +'.png') # saved as line(number).png
    plt.clf()  # stops from overwriting with additional data


for i in range(1,11): # loops 10 times(image 1 -> image 10)
    x = np.random.randint(10, size=10) # random array, [0-9 range]
    y = np.random.randint(10, size=10) # random array, [0-9 range]
    plt.scatter(x, y) 
    plt.savefig('scatter' + str(i) +'.png') # saved as scatternumber.png
    plt.clf()  # stops from overwriting with additional data



