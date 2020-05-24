#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from skits.preprocessing import DifferenceTransformer

y = np.random.random(10)
# scikit-learn expects 2D design matrices,
# so we duplicate the time series.
X = y[:, np.newaxis] 

dt = DifferenceTransformer(period=2)

Xt = dt.fit_transform(X,y)
X_inv = dt.inverse_transform(Xt)

assert np.allclose(X, X_inv)
