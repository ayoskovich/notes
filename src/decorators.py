#!/usr/bin/env python
# coding: utf-8

# - `jupyter nbconvert <notebook filename> --to="python" --output-dir='/outDir' --output="simple-nb-convert"`
# 
# - `juptyer nbconvert <notebook filename> --output-dir='/outDir' --output="myoutputfile.html"`

# # using decorators in python

# In[2]:


import functools

def my_decorator(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper

def say_whee():
    print('whee!')

# In[3]:


say_whee = my_decorator(say_whee)
say_whee()

# In[4]:


def another_way(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper

# equivalent to 'say_whee = another_way(say_whee)'
@another_way
def say_whee():
    print('whee!')

# In[5]:


say_whee()

# ## what if my functions have arguments?

# In[6]:


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_twice
def to_upper(string):
    print(string.upper())

# In[7]:


to_upper('anthony')

# ## what if my functions return stuff?

# In[8]:


def deco(func):
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        return rv
    return wrapper

@deco
def foo():
    return 1

# In[9]:


foo()

# ## what if I want the decorator to return some value?

# In[10]:


import time

def timeIt(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time {end - start}')
        
        return rv
    return wrapper

@timeIt
def wait():
    time.sleep(2)
    return 'this comes from wait()'

# In[11]:


wait()

# ## doesn't decorating a function mess with my ability to get help?

# In[12]:


wait

# In[13]:


help(wait)

# In[14]:


wait.__name__

# ## `import functools` to the rescue

# In[15]:


import functools

def timeIt(func):
    @functools.wraps(func)  # !!!
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time {end - start}')
        
        return rv
    return wrapper

@timeIt
def wait():
    time.sleep(2)
    return 'this comes from wait()'

# In[16]:


wait

# In[17]:


help(wait)

# In[18]:


wait.__name__

# ## what if I want to decorate a function that I import from a library?

# In[19]:


def debug(func):
    """ 
    ...I did not write this
    https://realpython.com/primer-on-python-decorators/
    """
    
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

# In[20]:


import math
math.factorial = debug(math.factorial)

def approx_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

# In[21]:


approx_e(5)

# Here I didn't have direct access to that function, but I was able to decorate it using the syntax seen at the beginning of this notebook.

# In[ ]:



