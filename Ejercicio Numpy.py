
# coding: utf-8

# In[37]:


import numpy as np


# In[38]:


ar1 = ([100,200,10,11])


# In[45]:


arr = np.array(ar1)


# In[40]:


ar2 = ([200,100,20,20])


# In[46]:


arr2 = np.array(ar2)


# In[49]:


arr2 > arr


# In[51]:


arr > arr2


# In[58]:


resultado = arr < arr2


# In[59]:


lista = list(resultado)


# In[60]:


lista


# In[62]:


lista.index(False)

