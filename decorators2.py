"""
Using decorators that take arguments
"""

import pandas as pd
import functools


def decorator(arg1, arg2):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print(arg1)
            rv = function(*args, **kwargs)
            print(arg2)
            return rv
        return wrapper
    return real_decorator


def setName(name):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            rv = func(*args, **kwargs)
            rv._name = name
            return rv
        return wrapper
    return real_decorator


@decorator("arg1", "arg2")
def print_name(name):
    return name.upper()


@setName('this is its name')
def make_df():
    df = pd.DataFrame({
        'a':[1, 2, 3],
        'b':[4, 5, 6]
    })

    return df
