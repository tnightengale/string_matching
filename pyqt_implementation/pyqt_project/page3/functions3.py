# -*- coding: utf-8 -*-
"""
Created on Wed Feb  20 

@author: TeghanN

Description: the custom functions used by page2.py
"""


from inspect import getouterframes, currentframe
import os

def runrec(src):
    '''
    Modified function from link above
    to yield tuples where the [1] index
    of each tuple is an int representing
    the depth of that dir or file in 
    the system.
    '''
    level = len(getouterframes(currentframe()))
    yield (src, level)
    for x in os.listdir(src):
        srcname = os.path.join(src, x)
        if os.path.isdir(srcname):
            yield from runrec(srcname)
        else:
            yield (srcname,level+1)
            

def groupings(list_of_tuples):
    '''
    Takes in a list_of_tuples, where the 
    [0] index is a path name and the [1]
    index is the depth. Returns a dict
    where the keys are the depths and 
    the paths are a list assigned to the
    keys.
    '''
    groups = {}
    
    for i in list_of_tuples:
        if i[1] in groups.keys():
            groups[i[1]].append(i[0]) # groups = {i[k]:['path1','path2'...], ...}
        else:
            groups[i[1]] = [i[0]]
    
    # filter out non-xls in each list and drop keys with list length 0
    iterable_keys = list(groups.keys())
    for key in iterable_keys:
        groups[key] = list(filter(lambda path: '.xls' in path, groups[key]))
        if len(groups[key]) == 0:
            groups.pop(key)
    
    # sort largest groups first
    ordered_groups = {}
    for i in sorted(groups, key = lambda k: len(groups[k]), reverse = True):
        ordered_groups[i] = groups[i]
    
    return ordered_groups


def largest_group(dict_of_lists):
    '''
    Takes in the above output and
    finds largest group. Outputs
    group as a list.
    '''
    values = list(map(lambda x: len(dict_of_lists[x]), dict_of_lists.keys()))
    index_max = max(range(len(values)), key=values.__getitem__)
    key_with_most_paths = list(dict_of_lists.keys())[index_max]
    return dict_of_lists[key_with_most_paths]


