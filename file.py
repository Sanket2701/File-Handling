#!/usr/bin/env python
# coding: utf-8

# In[5]:


f=open("file.txt",'r')
f.read()


# In[22]:


f=open("file.txt",'w')
f.write("World with")
f.close()


# In[23]:


f=open("file.txt","a")
f.write(" Corona Virus")
f.close()


# In[21]:


f=open("file.txt","r+")
f.read()
f.write("hi buddy")
f.read()
f.close()


# In[24]:


with open("file.txt") as file:   
    data = file.read()
    print(data)


# In[25]:


with open("file.txt", "w") as f:  
    f.write("Hello World!!!")


# In[29]:


with open("file.txt", "r") as file: 
    data = file.readlines() 
    for line in data: 
        word = line.split() 
        print('word')


# In[ ]:




