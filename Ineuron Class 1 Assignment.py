#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


x= pd.Series([10,13,18,22,27,32,38,40,45,51,56,57,88,90,94,99])


# In[16]:


plt.hist(x, bins= 5)
plt.grid()
plt.show()


# In[ ]:




