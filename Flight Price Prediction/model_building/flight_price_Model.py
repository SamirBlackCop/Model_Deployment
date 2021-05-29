# ================================  IMPORT LIBRARIES =========================================>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.model_selection import RandomizedSearchCV
import pickle

# =================================== Dataset ==================================================>

pd.set_option('display.max_columns', None)
train_data = pd.read_excel("flight_price_data.xlsx")
train_data.dropna(inplace = True)

# ======================================= EDA =====================================================>

train_data["Journey_day"] = pd.to_datetime(train_data.Date_of_Journey, format="%d/%m/%Y").dt.day
train_data["Journey_month"] = pd.to_datetime(train_data["Date_of_Journey"], format = "%d/%m/%Y").dt.month

