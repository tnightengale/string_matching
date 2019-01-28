
# coding: utf-8

# ## Transition to first develop robust method for traversing directories recursively and clustering common file names

# In[1]:


import glob
import os
import pandas as pd
import re
import jellyfish


# In[2]:


for root, dirs, files in os.walk(r'Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018'):
    if root != []: print('root: {}'.format(root))
    if dirs != []:
        print('    dirs:')
        for i in dirs:
            print('        {}'.format(i))
    if files != []:
        print('            files:')
        for j in files:
            print('                {}'.format(j))


# In[3]:


a = os.walk(r'Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018')


# In[4]:


list(a)


# In[5]:


def file_search(dirpath):
    '''
    Recursively walks the dirpath and creates a list of all
    files. Clusters files by similarity and outputs a list
    of the most prevalent cluster.
    '''
    file_paths = []
    for root, dirs, files in os.walk(dirpath):
        for filename in files:
            file_paths.append(os.path.join(root,filename))
    return file_paths


# In[6]:


test = r'Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018'


# In[7]:


a = file_search(test)


# ## Hardcode list of files to play with at home:

# In[8]:


for i in a:
    print(i)


# In[9]:


hardc = r'''Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Contact list Q1 2018.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Survey Tracker.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Q1 2018 Assets.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Q1 2018 RedGr.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\AGF\AGF Q1 2018-Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\AGF\AGF Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\AVISO\AVISO Q1 2018-Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\AVISO\AVISO Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\AVISO\RE Quarterly mutual fund survey - provincial data inquiries.msg
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\BMO\2018_Q1 - BMO Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Bridgehouse\Bridgehouse Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\CI\Q1_2018_All_CI_Brands.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\CIBC\CIBC Template Q1 2018.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\CIBC\Copy of Q1 2018 - CIBC Quarterly Mutual Fund Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\CIBC\Copy of Q1 2018 - Renaissance Quarterly Mutual Fund Survey HC.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Desjardins\Desjardins Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Dynamic\Dynamic Q1 2018-Quarterly Mutual Fund Survey (002).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Fidelity\Fidelity Quarterly_Provincial_MF_Survey (002).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\FTI\FTI Q1 2018-Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\FTI\FTI Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\HSBC\HSBC Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\IG\Investors Group Q1 2018 Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\IG\Investors Group Q1 2018 Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Invesco\Invesco Quarterly Mutual Fund Survey 2018-Q1.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Mackenzie\Mackenzie Q1 2018-Quarterly Mutual Fund Survey Inquiries.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Mackenzie\Mackenzie Q1 2018-Quarterly Mutual Fund Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Manulife\Manulife Q1 2018-Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Manulife\Manulife Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Manulife\Q1 2018-Quarterly Mutual Fund Survey(Revised).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Manulife\RE Quarterly mutual fund survey - provincial data inquiries.msg
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\National Bank\NB Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\PIMCO\PIMCO Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\RBC\RBC Q1 2018 - Qtrly MF Survey - FINAL.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Russell\Russell Q1 2018-Quarterly Mutual Fund Survey (003).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\Scotia\Scotia Q1 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\TD\REVISED 2018 Q1 SERIES DATA.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q1\Received\TD\TD 2018 Q1 Provincial MF Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Q2 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Survey Tracker.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Q2 2018 Assets.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Q2 2018 RedGr.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\AGF\AGF Q2 2018-Quarterly Mutual Fund Survey (008).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\AVISO\AVISO Q2 2018-Quarterly Mutual Fund Survey (002).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\BMO\BMO 2018_Q2 - Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Bridgehouse\Bridgehouse Q2 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Bridgehouse\FW Strategic Insight Quarterly Mutual Funds Survey Q2 2018.msg
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\CI\Investor_Economics_Q2_2018_All_CI_Brands.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\CIBC\CIBC Template Q2 2018.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\CIBC\Copy of Q2 2018 - CIBC Quarterly Mutual Fund Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\CIBC\Copy of Q2 2018 - Renaissance Quarterly Mutual Fund Survey HC.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Desjardins\Desjardins Q2 2018-Quarterly Mutual Fund Survey (005).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Dynamic\Dynamic Q2 2018-Quarterly Mutual Fund Survey (007).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Fidelity\Fidelity Quarterly_Provincial_MF_Survey Q2 2018.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\FTI\Q2 2018-Quarterly Mutual Fund Survey - FT.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\HSBC\HSBC Q2 2018-Quarterly Mutual Fund Survey (009).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\IG\IG Q2 2018 Quarterly Mutual Fund Survey inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\IG\IG Q2 2018 Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Invesco\Invesco Quarterly Mutual Fund Survey 2018-Q2.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Invesco\Invesco Quarterly Mutual Fund Survey 2018-Q2v2.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Mackenzie\Mackenzie Q2 2018-Quarterly Mutual Fund Survey Inquiries.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Mackenzie\Mackenzie Q2 2018-Quarterly Mutual Fund Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Mackenzie\RE Quarterly mutual fund survey inquiries.msg
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Mackenzie\Revisions\Q1 2018-Quarterly Mutual Fund Survey V2.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Mackenzie\Revisions\Q2 2018-Quarterly Mutual Fund Survey V2.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Manulife\Manulife 2018-Q2-Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Manulife\Manulife 2018-Q2-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\National Bank\NB Q2 2018-Quarterly Mutual Fund Survey (004).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\PIMCO\PIMCO Q2 2018-Quarterly Mutual Fund Survey (00A).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\PIMCO\PIMCO Q2 2018-Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\PIMCO\Q2 2018-Quarterly Mutual Fund Survey (Revised).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\PIMCO\RE Quarterly mutual fund survey inquiries.msg
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\RBC\RBC 06 Q2 2018 - Qtrly MF Survey - FINAL.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Russel\Russell Q2 2018-Quarterly Mutual Fund Survey (006).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\Scotia\Scotia Q2 2018-Quarterly Mutual Fund Survey (003).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q2\Received\TD\TD 2018 Q2 Provincial MF Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Q3 2018 Assets.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Q3 2018 RedGr.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\AGF\AGF Q3 2018-Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\AGF\AGF Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\AVISO\AVISO Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\BMO\BMO 2018_Q3 - Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Bridgehouse\Bridgehouse Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\CI\Q3_2018_All_CI_Brands Inquiries.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\CI\Q3_2018_All_CI_Brands.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\CIBC\CIBC Template Q3 2018.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\CIBC\Q3 2018 - CIBC Quarterly Mutual Fund Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\CIBC\Q3 2018 - Renaissance Quarterly Mutual Fund Survey HC.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Desjardins\Desjardins Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Fidelity\Fidelity Quarterly_Provincial_MF_Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\FTI\FTI Q3 2018-Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\FTI\FTI Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\HSBC\HSBC Q3 2018-Quarterly Mutual Fund Survey Inquiries.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\HSBC\HSBC Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\IG\IG Q3 2018 Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Invesco\Invesco Quarterly Mutual Fund Survey 2018-Q3.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Mackenzie\FW Strategic Insight Quarterly Mutual Funds Survey Q3 2018.msg
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Mackenzie\Mackenzie Q3 2018-Quarterly Mutual Fund Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Mackenzie\Q3 2018-Quarterly Mutual Fund Survey (Revised).xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Manulife\Manulife 2018-Q3-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\National Bank\NB Q3 2018-Quarterly Mutual Fund Survey (006).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\PIMCO\PIMCO Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\RBC\RBC 06 Q3 2018 - Qtrly MF Survey - FINAL.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Russel\Russell Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\Scotia\Scotia Q3 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q3\Received\TD\TD 2018 Q3 Provincial MF Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Contact list Q4 2018.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Q4 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\Q3 2018 Assets.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\Q3 2018 RedGr.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\BMO\BMO 2018_Q4 - Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\Bridgehouse\Bridgehouse Q4 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\CI\Investor_Economics_Q4_2018_All_CI_Brands.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\CIBC\Q4 2018 - CIBC Quarterly Mutual Fund Survey.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\CIBC\Q4 2018 - Renaissance Quarterly Mutual Fund Survey HC.XLS
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\Fidelity\Fidelity Quarterly_Provincial_MF_Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\HSBC\HSBC Q4 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\IG\IG Q4 2018 Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\Invesco\Invesco Quarterly Mutual Fund Survey 2018-Q4.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\Mackenzie\Mackenzie Q4 2018-Quarterly Mutual Fund Survey Final.xls
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\Manulife\Manulife 2018-Q4-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\NEI\NEI Q4 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\PIMCO\PIMCO Q4 2018-Quarterly Mutual Fund Survey (002).xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\Russel\Russell Q4 2018-Quarterly Mutual Fund Survey.xlsx
Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018\Q4\Received\TD\TD 2018 Q4 Provincial MF Survey.xls'''.split('\n')


# ## Implement similarity metrics to cluster file names

# In[10]:


import numpy as np


# Approach: build a pairwise comparison matrix for j>i (else null). After algorithm is built, attempt to apply the similarity metric to the pairs as they are being constructed. Result is an upper triangular matrix with (hopefully) some linear boundary x.

# Itertools has a function for pairwise combinations:

# In[11]:


import itertools


# In[12]:


list(itertools.combinations(['a','b','c'], 2))


# This function creates a pairwise list, rather than a matrix.

# In[13]:


combinations = list(itertools.combinations(hardc,2))


# Apply the similarity metrics to each tuple in the pairwise combinations:

# In[14]:


ld = [jellyfish.levenshtein_distance(i[0],i[1]) for i in combinations]


# ### Visualize distribution of measures 

# In[15]:


import seaborn as sns
sns.set()


# In[16]:


sns.distplot(ld)


# It looks like the levenshtein distance metric produces a fairly continuous distribution that would not be easy to segment linearly. 
# 
# One potential continuation of this approach would be to examine some clustering methods, and perhaps create more features by applying other similarity metrics to the pairwise combinations. These higher dimensional datapoints may be easier to classify.

# ### Continuation with k-means on raw strings (no feature engineering)

# In[17]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score


# In[18]:


hardc[:4]


# In[ ]:


vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(hardc)

true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)


# In[ ]:


print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])


# The above categorization seems very unpromising. The strings are very similar for a large portion of the beginning and the end of the string.

# In[ ]:


for i in range(len(hardc)):
    print('[{}]        '.format(str(model.labels_[i])) + hardc[i][50:])


# We can see above that the k-means clustering on the strings does not do a good job of differentiating out the files we want.

# ## Alternative approach 

# A case specific set of rules could be hard coded to pick out file names of interest using regex:

# ## A further approach

# One realization is that the files we want can be identified in the context of their position within the file tree. The idea is that files on the save level of a tree are probably similar. Thus attempting to work with a flat list of all file names actually reduces important contextual information.

# In[ ]:


## NO LONGER USED
def dir_to_lists(path):
    '''
    Some baller recursion in a 
    list comprehension to return
    a list of lists representation
    of a particular directory.
    '''
    dirs = os.listdir(path)
    return [dir_to_lists(path + r'\{}'.format(item)) if os.path.isdir(path + r'\{}'.format(item)) else item for item in dirs]
      
            


# In[ ]:


## NO LONGER USED
def dir_to_dicts(path):
    '''
    Some baller recursion in a 
    list comprehension with dict
    key to directory name to return
    a dict of dict and list
    representation
    of a particular directory.
    '''
    dirs = os.listdir(path)
    return {path:[dir_to_dicts(path + r'\{}'.format(item)) if os.path.isdir(path + r'\{}'.format(item)) else item for item in dirs]}
            


# Found some really great code that more easily solves the problem. Link here: https://stackoverflow.com/questions/40641615/what-is-the-difference-between-a-frame-and-object-and-when-should-i-modify-one

# In[ ]:


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


# In[ ]:


a = list(runrec(r"Z:\Data\Surveys\Quarterly Mutual Fund Survey\2018") )
a


# In[ ]:


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
        
    return groups


# In[ ]:


d = groupings(a)


# In[ ]:


d[33]


# In[ ]:


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


# Right now this function naively finds the largest grouping of files at a given depth in the file tree. A ui version would suggest groupings of files to the user, by descending group size. 

# In[ ]:


for i in largest_group(d):
    print('\n{}'.format(i))


# In[ ]:


list_of_files = largest_group(d)


# ## Scanning and Scraping Columns from the file list 

# The problem is that surveys often are not formatted identically. One option is to hardcode a set of rules that fail if the survey deviates. A better solution might be to loop through the files, locate a target sheet, and locate target columns. In a ui, the user might supply the target sheet and target columns. The loop could ask for clarigying input when it finds targets too disimilar to the supplied objective.

# ### Road map:
# 1. **Sheet Process**
#     - User input sheet name objective OR group similar targets and suggest
#     - generate list_of_sheets from list_of_files
#     - check list_of_sheets for targets that match objective, and request clarification if there are gaps
# <br>
# <br>
# 2. **Column Process**
#     - User input columns objective
#     - check target sheet for columns objective and if found, organize and append data to master table

# ### 1. Sheet Process 

# Let's explore if we can group sheet names:

# In[ ]:


# find longest common substring in list to use differentiating remaining substring
# to create dict keys. End result is {'remaining string1':{'sheet1':pd.df1,'sheet2':pd.df2, ...}, ...}
list(map(lambda s: s.split(os.path.commonprefix(list_of_files))[1],list_of_files))


# In[ ]:


def list_of_sheets(list_of_files):
    '''
    '''
    dict_of_sheets = {}
    
    common_substring = os.path.commonprefix(list_of_files)
    
    for file in list_of_files:
        try:
            dict_of_sheets[file.split(common_substring)[1]] = list(pd.read_excel(file, sheet_name = None).keys())
        except:
            print('The following file could not be read as an excel: {}'.format(file))
    
    return dict_of_sheets


# In[ ]:


SHEET_DICT = list_of_sheets(list_of_files)


# In[ ]:


SHEET_DICT


# Upon reflection, a better process might be to generate a flat list of sheet names, recommend one of the top ones and use that as the sheet objective.

# In[ ]:


from collections import Counter


# In[ ]:


def sheet_name_freq(list_of_files):
    '''
    '''
    sheet_freq = []
    
    for file in list_of_files:
        try:
            sheets = list(pd.read_excel(file, sheet_name = None).keys())
        except:
            print('\nThe following file could not be read as an excel: {}'.format(file))
        
        sheet_freq += sheets
    
    return Counter(sheet_freq)
    


# In[ ]:


sheet_name_freq(list_of_files)


# Choose one the most frequent sheet names, eg. Load Survey, and then check which files have a sheet which can be loosely matched to this objective.

# In[ ]:


sheet_objective = 'Load Survey'


# In[ ]:


def sheet_name_freq_list(list_of_files):
    '''
    '''
    sheet_freq = []
    
    for file in list_of_files:
        try:
            sheets = list(pd.read_excel(file, sheet_name = None).keys())
            sheet_freq.append(sheets)
        except:
            print('\nThe following file could not be read as an excel: {}'.format(file))
    
    return sheet_freq


# In[ ]:


sheet_name_freq_list(list_of_files)


# In[ ]:


def matching_sheet_objective(objective, list_of_files):
    '''
    '''
    dict_of_df = {}
    
    common_substring = os.path.commonprefix(list_of_files)
    
    for file in list_of_files:
        
        try:
            curr_df = pd.read_excel(file, sheet_name = None)
        except:
            print('\nThe following file could not be read as an excel: {}'.format(file))
    
        curr_sheets = list(curr_df.keys())
        
        if objective in curr_sheets:
            dict_of_df[file.split(common_substring)[1]] = curr_df[objective]
        
        else:
            print('Objective sheet: "{}" is not in list of sheet targets: {}.'.format(objective, curr_sheets))
            
            print('Target options:')
            
            for i in range(len(curr_sheets)):
                print('{}. {}'.format(i,curr_sheets[i]))
            
            u_input = input('Enter the number of the correct above target. Enter nothing to skip: ')
            
            
            try: 
                if int(u_input) in range(len(curr_sheets)):

                    dict_of_df[file.split(common_substring)[1]] = curr_df[curr_sheets[u_input]]

                    print('{} was imported.'.format(curr_sheets[u_input]))
            except:
                print('\n"{}" is not a valid input. No sheets from the following file were imported: {}'.format(u_input,file))
            
    return dict_of_df


# In[ ]:


matching_sheet_objective(sheet_objective, list_of_files)


# In[ ]:


x = input()


# In[ ]:


x


# In[ ]:


int(x) in


# In[ ]:


list_of_files

