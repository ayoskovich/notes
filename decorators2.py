"""
Using decorators that take arguments.
"""

import pandas as pd
import functools


def setName(name):
    def real_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            rv = func(*args, **kwargs)
            rv._name = name
            return rv
        return wrapper
    return real_decorator


def printMessage(mess):
    def real_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            rv = func(*args, **kwargs)
            print(mess)
            return rv
        return wrapper
    return real_decorator


class Wrangle:
    """
    Houses data wrangling methods
    """

    @staticmethod
    @printMessage('Printing df1')
    @setName('this is its name')
    def make_df():
        df = pd.DataFrame({
            'a':[1, 2, 3],
            'b':[4, 5, 6]
        })

        return df

    @staticmethod
    @printMessage('Printing df2')
    @setName('filtered version')
    def filter_df():
        df = Wrangle.make_df().query('a == 2')

        return df


if __name__ == "__main__":
    x = Wrangle.filter_df()
    y = Wrangle.make_df()
