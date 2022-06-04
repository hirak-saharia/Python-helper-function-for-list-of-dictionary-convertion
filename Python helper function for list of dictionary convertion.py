#!/usr/bin/env python
# coding: utf-8

# In[1]:


movies = '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fic"}]'


# In[2]:


movies


# #We can see that it is list of dictionary format and we need to convert into a
# ['Action', 'Adventure', 'Fantasy', 'Science Fic'] format
# 
# To do so, we will use helper() funtion and  ast module using ast.literal_eval() function

# In[4]:


def convert(obj):
    L = []
    for i in obj:
        L.append(i['name'])
    return L


# In[11]:


import ast 
ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fic"}]')


# In[12]:


def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


# In[22]:


convert(movies)


# In[ ]:




