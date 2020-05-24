#!/usr/bin/env python
# coding: utf-8

# # Working in jupyter notebooks
# 
# Helpful links
# 
# - [28 tips](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
# - [features](http://arogozhnikov.github.io/2016/09/10/jupyter-features.html)

# ### Store data between notebooks

# In[3]:


# Notebook 1
x = 'This is a stored variable'
%store x

# In[4]:


# Notebook 2
%store -r x
x

# ### See namespace

# In[8]:


foo = 'Anthony'
num = 43

# In[12]:


%who

# In[9]:


%who str

# In[10]:


%who int

# In[11]:


%who float

# ### Running terminal commands from the notebook

# In[16]:


!dir /A:D

# In[19]:


!cd

# ### You can also save terminal output into python

# In[3]:


output = !dir

# ### Keyboard shortcuts for jupyter lab

# ```
# {
#   "shortcuts": [
#     {
#       "command": "notebook:hide-cell-outputs",
#       "keys": [
#         "Shift O"
#       ],
#       "selector": ".jp-Notebook:focus"
#     },  
#       
#     {
#       "command": "notebook:show-cell-outputs",
#       "keys": [
#         "O"
#       ],
#       "selector": ".jp-Notebook:focus"
#     }
#   ]
# }
# ```

# ### Visual themes

# In[5]:


!pip install jupyterthemes

# In[6]:


!jt -l

# In[7]:


!jt -t onedork

# In[ ]:



