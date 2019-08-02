import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib.pylab import rcParams
##normalizing data
from sklearn.preprocessing import MinMaxScaler

rcParams['figure.figsize'] = 20, 10
scale = MinMaxScaler(feature_range=(0,1))

##reading file
file = pd.read_csv('NSE-TATAGLOBAL11.csv')

print(file.head())