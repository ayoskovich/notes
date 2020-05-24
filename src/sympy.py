#!/usr/bin/env python
# coding: utf-8

# ## Notes on `sympy`
# 
# - Source [here](https://github.com/sympy/sympy)
# - Tutorial [here](https://docs.sympy.org/latest/tutorial/index.html)

# In[1]:


import sympy

# In[2]:


help(sympy)

# In[3]:


sympy.__version__

# In[7]:


sympy.sqrt(8)

# In[8]:


from sympy import symbols

# In[34]:


x, y = symbols('x y')

# In[17]:


expr = x + y
expr

# ### Factoring and expanding expressions

# In[2]:


from sympy import *

# In[3]:


from sympy import expand, factor
expanded_expr = expand(x*expr)
expanded_expr

# In[25]:


factored_expr = factor(expanded_expr)
factored_expr

# ### Integration and differentiation

# In[90]:


diff(sin(x)*exp(x), x)  # Take the first derivative
diff(sin(x)*exp(x), x, 2)  # Take the second derivative

# In[30]:


integrate(exp(x)*sin(x) + exp(x)*cos(x), x)

# In[35]:


limit(sin(x)/x, x, 0)

# In[36]:


solve(x**2 - 2, x)

# ### Get answer as LaTeX

# In[40]:


latex(integrate(exp(x), x))

# ### Gotchas
# 
# https://docs.sympy.org/latest/gotchas.html#gotchas

# In[45]:


a, b = symbols('b a')  # a is b and b is a
crazy = symbols('unrelated')  # symbols could be anything

# In[55]:


x + 1 == x + 1  # Double equal sign tests for "exact structural equality testing"

# ### Using Eq

# In[64]:


Eq(x + 1, x + 1)

# In[65]:


Eq(x + 1, 6)

# In[4]:


solve(Eq(x + 1, 8), x)

# In[60]:


(x + 1)**2 == x**2 + 2*x + 1

# In[69]:


a = cos(x)**2 - sin(x)**2
b = cos(2*x)

a.equals(b)  # Another way to test for equality

# ### Using rational numbers

# In[70]:


x + 1/3

# In[71]:


x + Rational(1, 3)

# ### Substitution

# In[74]:


z = symbols('z')

# In[76]:


expr = cos(z) + 1

# In[78]:


expr.subs(z, 4)

# In[79]:


expr.subs(z, x)

# In[81]:


expr = x**2 + z**3
expr.subs([(x, 2), (z, 4)])

# ### Converting strings to sympy expressions

# In[5]:


str_expr = "x**2 + 5"
expr = sympify(str_expr)

# In[6]:


expr

# ### Evaluate an equation to floating point

# In[7]:


sqrt(8).evalf()

# In[9]:


import inspect

# In[10]:


help(inspect)

# In[ ]:



