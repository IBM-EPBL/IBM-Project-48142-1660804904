#!/usr/bin/env python
# coding: utf-8

# # Basic python

# # 1.Split this String

# In[1]:


single="hi there sam!"
print(single)
tokens=single.split()
print(tokens)


# In[2]:


hello="i am studying"
print(hello)
hi=hello.split()
print(hi)


# # 2.Use .format() to print the following string
# 
# output should be:The diameter of earth is 12742

# In[6]:


planet="Earth"
diameter=12742


# In[7]:


print('the diameter of {} is {} kilometers.' . format(planet,diameter));


# # 3.In this nest dictionary grab the world"hello" 

# In[41]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])


# In[31]:


print(d['k1'][3]['tricky'][3]['target'][3])


# In[9]:


import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)


# # 4.1 Create an array of 10 zeros?

# # 4.2 Create an array of 10 fives?

# In[10]:


import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)


# In[12]:


import numpy as np
array=np.ones(10)*5
print("An array of  fives:")
print(array)


# # 5.Create an array of all the even integers from 20 to 35

# In[13]:


import numpy as np
array=np.arange(20,35,2)
print("Array of all the even integers from 20 to 35")
print(array)


# # 6.Create a 3x3 matrix with values ranging from 0 to 8

# In[14]:


import numpy as np
x =  np.arange(0, 9).reshape(3,3)
print(x)


# # 7.Concatenate a and b
# 
#  a=np.array([1,2,3]),b=np.array([4,5,6])

# In[15]:


import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b
print(c)


# # 8.Create a database with 3 rows and 2 columns

# In[1]:


import pandas as pd
data = [['tom',15], ['jerry',20], ['juli',23]]
df = pd.DataFrame(data, columns=['Name','Age'])
print(df)


# In[2]:


import pandas as pd
data = [['yosh',15], ['vicky',21], ['maddy',19]]
df = pd.DataFrame(data, columns=['players','numbers'])
print(df)


# # 9.Generate the series of dates from 1st jan,2023 to 10th feb,2023

# In[26]:


import pandas as pd
pd.date_range("01-01-23","10-02-23")


# # 10. Create 2D list to DataFrame
# lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

# In[3]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[ ]:




