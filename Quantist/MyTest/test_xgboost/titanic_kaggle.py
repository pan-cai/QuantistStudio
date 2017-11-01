# _*_ coding:utf-8 _*_
import pandas as pd

import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.cross_validation import KFold
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import accuracy_score

#read data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")