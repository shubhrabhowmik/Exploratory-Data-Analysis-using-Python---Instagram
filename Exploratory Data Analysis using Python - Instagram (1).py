#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis using Python

# Dataset: https://statso.io/instagram-reach-analysis-case-study/

# In[2]:


import pandas as pd
import numpy as snp
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
pio.templates.default = "plotly_white"


# In[3]:


data = pd.read_csv("C:\\Users\\BHS7BAN\\Desktop\\Python\\Instagram_analysis\\Instagram data.csv", encoding='latin-1')


# In[4]:


data.head(3)


# Next, we look at the descriptive statistics of the data:

# In[5]:


data.describe()


# In[6]:


data.columns


# Now let’s have a look at the column info:

# In[7]:


data.info()


# Let's have a look if your data contains any missing values or not:

# In[8]:


data.isnull().sum()


# When you start exploring your data, always start by exploring the main feature of your data. For example, as we are working on a dataset based on Instagram Reach, we should start by exploring the feature that contains data about reach. In our data, the Impressions column contains the data about the reach of an Instagram post. So let’s have a look at the distribution of the Impressions:

# In[9]:


fig = px.histogram(data, x='Impressions', nbins=10, title='Distribution of Impressions')
fig.show()


# Now let’s have a look at the number of impressions on each post over time:

# In[10]:


fig = px.line(data, x= data.index, 
              y='Impressions', 
              title='Impressions Over Time')
fig.show()


# In[11]:


fig = go.Figure()

fig.add_trace(go.Scatter(x=data.index, y=data['Likes'], name='Likes'))
fig.add_trace(go.Scatter(x=data.index, y=data['Saves'], name='Saves'))
fig.add_trace(go.Scatter(x=data.index, y=data['Follows'], name='Follows'))

fig.update_layout(title='Metrics Over Time',
                  xaxis_title='Date',
                  yaxis_title='Count')

fig.show()


# Now let’s have a look at the distribution of reach from different sources:

# In[12]:


reach_source = ['From Home','From Hashtags','From Explore','From Other']
reach_count = [data[source].sum() for source in reach_source]

fig = px.pie(data_frame = data,
       names = reach_source,
       values = reach_count,
       title = 'Reach from Different Sources')

fig.show()


# Now let’s have a look at the distribution of engagement sources:

# In[13]:


engagement_sources = ['Saves','Comments','Shares','Likes']
engagement_count = [data[source].sum() for source in engagement_sources]

fig = px.pie(data_frame=data,
            names=engagement_sources,
            values=engagement_count,
            title='Engagement Sources')

fig.show()


# Now let’s have a look at the relationship between the number of profile visits and follows:

# In[14]:


fig = px.scatter(data, x="Profile Visits", y="Follows",
                title = 'Profile Visits vs. Follows',
                trendline="ols")
fig.show()

