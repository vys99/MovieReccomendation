#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df=pd.read_csv('C:/Users/vysak/Downloads/Hydra-Movie-Scrape.csv')
df


# In[3]:


df = df[['Title','Genres','Director','Writers','Cast']]
df


# In[4]:


df.duplicated().sum()


# In[5]:


df.isnull().sum()


# In[6]:


features=['Title','Genres','Director','Writers','Cast']
for i in features:
    df[i]=df[i].fillna(' ')


# In[7]:


df.isnull().sum()


# In[8]:


df2=df.copy()


# In[9]:


le=LabelEncoder()
for i in features:
    df2[i]=le.fit_transform(df2[i].astype(str))
df2


# In[10]:


wcss=[]
for i in range(1,15):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=True)
    kmeans.fit(df2)
    wcss.append(kmeans.inertia_)


# In[11]:


plt.plot(range(1,15),wcss,'r',marker='D')
plt.title('Elbow Method')
plt.ylabel('WCSS')
plt.xlabel('No of Clusters')
plt.show()


# In[12]:


kmeans=KMeans(n_clusters=10,init='k-means++',random_state=True)
ykmeans=kmeans.fit_predict(df2)


# In[13]:


labels=pd.Series(ykmeans)
labels


# In[14]:


df2['clust']=labels
df['clust']=labels


# In[15]:


df2


# In[16]:


df2.groupby(df2['clust']).mean()


# In[17]:


import tkinter as tk


# In[18]:


root=tk.Tk()


# In[19]:


root.configure(bg='chartreuse')


# In[20]:


root.title('Movie Recommendation ')


# In[21]:


label1=tk.Label(root,text='Enter the movie name ',bg='yellow',font=("Arial", 20))
label1.pack(pady=10)


# In[22]:


entry=tk.Entry(root)
entry.pack(pady=10)


# In[23]:


import random


# In[24]:


def button_fun():
    with open('reccom.txt','w') as file:
        movie_nm=entry.get()
        recco=[]
        new_rand=[]
        clust=df[df['Title']==movie_nm]['clust'].iloc[0]
        for i,j in zip(df['Title'],df['clust']):
            if j==int(clust):
                recco.append(i)
        for l in range(10):
            if l not in new_rand:
                new_rand.append(random.choice(recco))
        for g in new_rand:
            file.write(str(g) +'\n')
            
    with open('reccom.txt','r') as f:
        label2.config(text=f.read())


# In[25]:


def cancel_fun():
    label2.configure(text=' ')


# In[26]:


button=tk.Button(root,text='Find',font=("Arial", 12),bg='light green', fg='black',command=button_fun)
button.pack(pady=10)


# In[27]:


button=tk.Button(root,text='Cancel',font=("Arial", 12),bg='light green', fg='black',command=cancel_fun)
button.pack(pady=10)


# In[28]:


label3=tk.Label(root,text='--------  Movie Recommendations  --------',bg='yellow',font=("Arial", 20))
label3.pack(pady=10)


# In[29]:


label4=tk.Label(root,text=' ',font=("Arial", 20),bg='chartreuse')
label4.pack(pady=10)


# In[30]:


label2=tk.Label(root,text=' ',font=("Arial",16),bg='chartreuse')
label2.pack(pady=10)


# In[31]:


root.mainloop()

