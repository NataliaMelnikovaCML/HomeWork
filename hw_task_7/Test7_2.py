# задание 2
import numpy
from sklearn import svm
# from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

data = open('titanic_no_name.csv').read()
# print(data)
data_2 = data.replace('"','')
data_new = float(data_2)
