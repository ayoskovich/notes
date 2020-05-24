#!/usr/bin/env python
# coding: utf-8

# ## Generators
# 
# Generator functions allow for us to define functions that behave like iterators. I can use this thing in a for loop.

# In[1]:


x = !dir

# In[1]:


import time

def timeit(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        rv = func(*args, **kwargs)
        t2 = time.time()
        print('Total time for {}: {}'.format(func.__name__, t2 - t1))
        
        return rv
    return wrapper
    

# In[2]:


@timeit
def firstn(n):
    num = 0
    myList = []
    while num < n:
        myList.append(num)
        num += 1
        
    return myList

@timeit
def gimmen(n):
    num = 0
    while num < n:
        yield num
        num += 1

NREPS = 10000000
x = sum(firstn(NREPS))
y = sum(gimmen(NREPS))

# In[ ]:



