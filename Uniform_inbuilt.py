import math
import numpy as np
from random import seed
from random import random
import matplotlib.pyplot as plt
import time

N = 1000;
a = np.zeros((2,N))
for i in range(N):
    a[1,i] = random()

a = np.sort(a)
