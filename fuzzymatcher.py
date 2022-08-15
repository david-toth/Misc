import string
from collections import Counter
import numpy as np
import pandas as pd
from tqdm import tqdm # optional -- if it's a hassle to pip install on Domino, then don't bother

def remove_whitespace(x):
    """Remove whitespace from a string"""
    return x.replace(" ", "")


def lower_case(x):
    """Lowercase representation"""
    x = x.lower()
    return x


def remove_chars(x, chars_to_remove):
    """Remove specific chars from string
    
    Consider this a generalization of remove_whitespace
    function defined above
    
    """
    if chars_to_remove is None:
        return x
    return "".join(i for i in x if i not in chars_to_remove)


def get_ngrams(x, n, return_count=False):
    """Get all ngrams in a string
    
    optionally returns the counts of each ngram, which might be
    useful if the string has duplicated ngrams
    
    """
    x_ngrams = [x[i:i+n] for i in range(len(x) - n + 1)]
    if return_count:
        return Counter(x_ngrams)
    return x_ngrams


def score(a, b):
    """Score the similarity of two strings"""
    if type(a) != set:
        a = set(a)
    if type(b) != set:
        b = set(b)
    ndiff = len(a ^ b)
    ntotal = len(a | b)
    return 1. - ndiff/ntotal


def fuzzy_matcher(table1, 
                  table2, 
                  cols1, 
                  cols2,
                  index1,
                  index2,
                  chars_to_remove=None,
                  ngrams_n=2
                 ):
    """Fuzzy match table 1 with table 2
    
    Args:
        table1          : input table that requires matching
        table2          : source table to match against
        cols1           : columns to use for matching in table1
        cols2           : columns to use for matching in table2
        index1          : record identifier for table1
        index2          : record identifier for table2
        chars_to_remove : list of characters to remove before fuzzy matching. Default is None
        ngrams_n        : number of characters to use when creating ngrams
        
    Returns:
        dataframe of index1, index2 of matching candidates, and match score 
        
    """
    column_order1 = [index1] + cols1
    column_order2 = [index2] + cols2
    df1 = table1[column_order1].copy()
    df2 = table2[column_order2].copy()
    # Fill NA values with blanks
    df1.fillna("", inplace=True)
    df2.fillna("", inplace=True)
    # Concatenate columns to match
    df1["x"] = df1.iloc[:, 1:].sum(axis=1)
    df2["x"] = df2.iloc[:, 1:].sum(axis=1)
    # Create ngrams
    df1["xngram"] = (df1["x"]
                     .apply(remove_chars, chars_to_remove=chars_to_remove)
                     .apply(lower_case)
                     .apply(get_ngrams, n=ngrams_n)
                     .apply(set)
                    )
    df2["xngram"] = (df2["x"]
                     .apply(remove_chars, chars_to_remove=chars_to_remove)
                     .apply(lower_case)
                     .apply(get_ngrams, n=ngrams_n)
                     .apply(set)
                    )
    # Fuzzy match
    results = np.zeros((df1.shape[0], df2.shape[0]))
    for i, x in enumerate(df1.xngram):
        for j, y in enumerate(df2.xngram):
            results[i, j] = score(x, y)
    indices = np.argmax(results, axis=1)
    scores = results.max(axis=1)
    df_results = pd.DataFrame({
        "input_id": df1[index1].values,
        "match_id": df2[index2][indices].values,
        "score": scores
    })
    return df_results