import pandas as pd
import numpy as np


def calcRun(my_df, col):
    """ Calculate running total of a column. 
    
    my_df (pd.DataFrame): Original dataframe
    col (string): Column name to calculate running total on 
    """
    return my_df.groupby(['group'], as_index=False)[col].cumsum()


def getAssignments(my_df, cutoff):
    """ Return part of df for 1 person. 
    
    my_df (pd.DataFrame): Original dataframe
    cutoff (int): Max account size for an individual person
    """
    
    rv = my_df.query('running < {}'.format(cutoff))[['group', 'acct', 'amt']]
    indices = rv.index
    
    return rv, indices


def dropDone(my_df, indices):
    """ Drop records from the dataframe that have been solved. 
    
    my_df (pd.DataFrame): Original dataframe
    indices (pandas.core.indexes.numeric.Int64Index): Indexes of popped dataframe
    """
    return my_df.drop(indices).drop(labels=['running'], axis=1)
