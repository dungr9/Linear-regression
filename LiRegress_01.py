import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv('data.csv').values

x = data[:, 0].reshape(-1, 1)
y = data[:,1].reshape(-1,1)




