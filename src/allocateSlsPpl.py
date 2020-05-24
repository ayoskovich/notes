#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np
import allocate

import importlib
importlib.reload(allocate); 

SAM_CAP = 20

df = pd.DataFrame(columns=['group', 'acct', 'amt'],
    data = [
    ('a', 'x1', 1),
    ('a', 'x2', 3),
    ('a', 'x3', 6),
    ('a', 'x4', 7),
    ('a', 'x5', 1),
    ('a', 'x6', 5),
    ('a', 'x7', 8),
    ('a', 'x8', 17),
    ('a', 'x9', 3)
    ])

df.sort_values(by=['group', 'amt'], 
               ascending=[True, False],
               inplace=True)

# In[37]:


def iterOne(df):
    df['running'] = df.pipe(allocate.calcRun, 'amt')

    new, inds = allocate.getAssignments(df, 20)

    # save 'new'
    nowWorkWith = df.pipe(allocate.dropDone, inds)
    
    return new, nowWorkWith


allAssignments = []
for i, x in enumerate(range(10)):
    df['running'] = df.pipe(allocate.calcRun, 'amt')

    assignment, inds = allocate.getAssignments(df, 20)
    
    assignment['tag'] = i
    
    allAssignments.append(assignment)
    
    # Overwrite df and drop the assignment we just chose
    df = df.pipe(allocate.dropDone, inds)

# In[38]:


# Print all assignments

for frame in allAssignments:
    if frame.empty:
        break
    else:
        print(frame)

# #### Stack all the assignments

# In[39]:


pd.concat(allAssignments)

# In[ ]:



