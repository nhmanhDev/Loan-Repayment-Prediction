import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
import joblib
import time
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

# Print versions of all imported libraries
print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", plt.matplotlib.__version__)
print("Seaborn version:", sns.__version__)
print("XGBoost version:", xgb.__version__)
print("Joblib version:", joblib.__version__)
# print("Scikit-learn version:", sklearn.__version__)
# print("Time version:", time.__version__)
print("RandomForestClassifier version:", RandomForestClassifier.__module__)

import sklearn
print(sklearn.__version__)
print("KNeighborsClassifier version:", KNeighborsClassifier.__module__)
print("LogisticRegression version:", LogisticRegression.__module__)