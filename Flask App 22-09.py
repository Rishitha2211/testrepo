#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install flask


# In[8]:


from flask import Flask


# In[9]:


app=Flask(__name__)


# In[10]:


@app.route('/')
def test():
    return "Test code working!!!!!!!"
@app.route('/next')
def next():
    return "Showing the next page"


# In[ ]:


if __name__=='__main__':
    app.run()


# In[ ]:




