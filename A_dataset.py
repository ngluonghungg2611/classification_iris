import pandas as pd 
import numpy as np     
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data[: , :2] # Lay all ahng va 2 cot
y = iris.target # Lay tat ca cac labels thuc te
