#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import json
from io import StringIO

import urllib.request
from pandas.io.json import json_normalize

api_key = 'PpgzmsmlP651k7P22v4MZoZuNKckiO6m'
url = 'https://api.nytimes.com/svc/topstories/v2/world.json?'
string = url+'&api-key='+api_key

response = str(urllib.request.urlopen(string).read(), 'utf-8')

#print(response)
df = pd.read_json(StringIO(response))
df.head(100)


# In[ ]:




