# -*- coding: utf-8 -*-
"""data preprocessing.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/github/IBM-EPBL/IBM-Project-3276-1658510974/blob/main/Final%20Deliverables/Data%20Pre-Processing/data%20preprocessing.ipynb
# Importing Libraries
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix,accuracy_score

ds=pd.read_csv(r"dataset_website.csv")
ds.head()

"""# Importing Data Set"""

ds.info()
ds.isnull().any()

x=ds.iloc[:,1:31].values
y=ds.iloc[:,-1].values
print(x,y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

"""# Model
"""

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)

y_pred1=lr.predict(x_test)
from sklearn.metrics import accuracy_score
log_reg=accuracy_score(y_test,y_pred1)
log_reg

import pickle
pickle.dump(lr,open('Phishing_Website.pkl','wb'))

"""# Handling null values"""

ds.shape

ds.columns

ds.info()

ds.describe()

ds['HTTPS_token'].unique()

ds.isnull().any()

"""# Splitting the Data"""

y = ds['Result']
X = ds.drop('Result',axis=1)
X.shape, y.shape

print(X)

print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=0)

X_train.shape

y_test.shape

X_test.shape