import matplotlib.pyplot as plt # imports
import numpy as np
import random
import sys



for i in range(1,11): # loops 10 times(image 1 -> image 10)
    randarr = np.random.randint(10, size=10) # random array, [0-9 range]
    x = randarr # set x
    randarr = np.random.randint(10, size=10) # random array, [0-9 range]
    y = randarr #  set y
    plt.scatter(x, y) 
    plt.savefig('scatter' + str(i) +'.png') # saved as scatternumber.png
    plt.clf()  # stops from overwriting with additional data

