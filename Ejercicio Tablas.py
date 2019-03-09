
# coding: utf-8

# In[28]:


import pandas as pd


# In[32]:


data = {'equipos': ['Heredia', 'Saprissa', 'LDA', 'Limón', 'Cartago', 'Grecia'],
        'puntos': [30, 31, 28, 10, 21, 30]}
data


# In[33]:


frame = pd.DataFrame(data)
frame


# In[35]:


tabla = pd.DataFrame(data)
tabla.index.name = 'posicion'
tabla


# In[38]:


tabla = tabla.sort_values('puntos', ascending=False).reset_index(drop=True)


# In[39]:


tabla


# In[44]:


tabla.head(3)


# In[47]:


tabla.tail(1)


# In[49]:


tabla.loc[:2]


# In[66]:


tabla.loc[len(tabla)-1:]

