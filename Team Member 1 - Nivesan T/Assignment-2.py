#!/usr/bin/env python
# coding: utf-8

# In[1]:


#IMPORTING THE libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


# In[2]:


#importing the dataset
df=pd.read_csv(r"E:\assignment2\Churn_Modelling.csv")


# In[3]:


#PERFORM VISUALIZATION
#univariate analysis
df.nunique()


# In[4]:


#univariate analysis
df.head()


# In[5]:


#Bi-variate analysis
sns.FacetGrid(df,hue="IsActiveMember",size=5)
plt.show()


# In[6]:


#multi-variate analysis
sns.pairplot(df, hue="IsActiveMember", height=2)


# In[12]:


#DESCRIPTION STATICS ON THE DATASET
df.describe()


# In[8]:


#HANDLE THE MISSING VALUES
df.isnull().sum


# In[9]:


#HANDLE THE MISSING VALUES
df.isnull().sum().sum()


# In[10]:


#CHECKS FOR THE CATEGORICAL COLUMNS AND PERFORM ENCODING
df.columns


# In[13]:


#SPLIT THE DATA INTO DEPENDENT AND INDEPENDENT VARIABLES
x = df.iloc[:,6:8].values
print(x)


# In[14]:


#Extracting the Dataset to Get the Dependent variable
y = df.iloc[:,3].values
print(y)


# In[15]:


#SCALE THE INDEPENDENT VARIABLES
# Initialise the Scaler
scaler = StandardScaler()


# In[16]:


#SPLIT THE DATA INTO TRAINING AND TESTING
from sklearn.model_selection import train_test_split
df = pd.read_csv(r"E:\assignment2\Churn_Modelling.csv")
x= df.iloc[:,6:8].values
y=df.iloc[:,3].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.05, random_state=0)


# In[18]:


print (x_train)


# In[19]:


print(y_train)


# In[20]:


print(x_test)


# In[21]:


print(y_test)

