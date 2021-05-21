#!/usr/bin/env python
# coding: utf-8

# #                                   Exploratory Data Analysis-Retail
# 
# ##                                              The Spark Foundation 
# 
# ##                                     Data science &Business Analytics Intern
# 

# ## Task#3:

# ### Author:Harish patel

# ###### Exploratory Data Analysis on SampleSuperstore.csv
#        #AS a Business manager,try to find out the weak areas where you can work to make more profit.

# In[1]:


#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#let's the data read by using pandas libraries


# In[3]:


df=pd.read_csv("Downloads/SampleSuperstore.csv")


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info


# In[7]:


df.isnull().sum()


# In[8]:


df.duplicated().sum()


# In[9]:


df.drop_duplicates(subset=None,keep="first",inplace=True)
df


# In[10]:


df.nunique()


# In[11]:


col=["Postal Code"]
df=df.drop(columns=col,axis=1)


# In[12]:


corr=df.corr()
corr


# In[13]:


plt.figure(figsize=(6,4))
with sns.color_palette("muted"):
    sns.countplot(x='Ship Mode',data=df)


# In[14]:


df.hist(bins=50,figsize=(20,15))


# In[15]:


plt.figure(figsize=(6,4))
with sns.color_palette("muted"):
    sns.countplot(x="Region",data=df)


# In[ ]:





# In[16]:


plt.figure(figsize=(9,7))
with sns.color_palette("muted"):
    sns.countplot(x="State",data=df)
    plt.xticks(rotation=90)


# In[17]:


plt.figure(figsize=(6,4))
with sns.color_palette("muted"):
    sns.countplot(x="Segment",data=df)


# In[18]:


newdata=pd.DataFrame(df.groupby('State').sum())['Profit'].sort_values(ascending=True)


# In[19]:


print(newdata)


# In[20]:


state=df.groupby('State')[['Sales','Profit']].sum().sort_values(by="Sales",ascending=False)
plt.figure(figsize=(60,70))
state[:30].plot(kind="bar",color=['blue',"red"])
plt.title("Profit or loss and sales of the top 30 States")
plt.xlabel("States")
plt.ylabel("total profit/ loss and sales")
state[30:].plot(kind="bar",color=["blue","red"])
plt.title("Profit or loss and sales of least economic States")
plt.xlabel("States")
plt.ylabel("total profit/ loss and sales")


# In[21]:


data=pd.DataFrame(df.groupby("State").sum())["Discount"].sort_values(ascending=True)
data


# In[22]:


plt.figure(figsize=(10,5))
sns.lineplot("Discount","Profit",data=df,color="blue",label="Discount")
plt.legend()


# In[23]:


#The above the analysis showing if we reduce the discount the profit we will increase.


# In[ ]:




