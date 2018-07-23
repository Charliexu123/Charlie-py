
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

import random


# In[3]:

position=0


# In[4]:

walk=[position]


# In[5]:

steps=1000


# In[6]:

for i in xrange(steps):
    step=1 if random.randint(0,1) else -1
    position+=step
    walk.append(position)


# In[7]:

nsteps=1000


# In[8]:

draws=np.random.randint(0,2,size=nsteps)


# In[9]:

steps=np.where(draws>0,1,-1)


# In[10]:

walk=steps.cumsum()


# In[11]:

walk.min()


# In[12]:

walk.max()


# In[13]:

(np.abs(walk)>=10).argmax()


# In[14]:

nwalks=5000


# In[15]:

nsteps=1000


# In[16]:

draws=np.random.randint(0,2,size=(nwalks,nsteps))


# In[17]:

steps=np.where(draws>0,1,-1)


# In[18]:

walks=steps.cumsum(1)


# In[19]:

walks


# In[20]:

walks.max()


# In[21]:

walks.min()


# In[23]:

hits30=(np.abs(walks)>=30).any(1)


# In[24]:

hits30


# In[25]:

hits30.sum()


# In[26]:

crossing_times=(np.abs(walks[hits30])>=30).argmax(1)


# In[27]:

crossing_times.mean()


# In[ ]:



