#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

df = pd.read_csv('C:/Users/HP/Downloads/uber-raw-data-aug14.csv')
df.head()


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns 


# In[7]:


import numpy as np


# In[21]:


# q1 - on what date we see the most no. of uber pickups 
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
grouped = df.groupby('Date/Time').size().reset_index(name = 'count')
sorted_data = grouped.sort_values(by ='count', ascending = False)
sorted_data.iloc[:1]
#  ans 1 date - 2014-08-12


# In[ ]:


# q2 - how many uber pickups were made on the date with highest no. of pickups 
#  ans 2 - 74 


# In[24]:


#  q3 - how many unique TLC base companies are affiliated with uber pickups in the dataset

count = df['Base'].nunique()
print(count)


# In[28]:


#  Q4 - which tlc base company have the highest no. of pickups 

grouped = df.groupby('Base').size().reset_index(name = 'count')
sorted_data = grouped.sort_values(by = 'count',ascending = False)
sorted_data.iloc[:1]


# In[40]:


#  q5 - how many uber pickups were made at each unique tlc base company 

grouped = df.groupby('Base').size().reset_index(name = 'count')
grouped


# In[41]:


# q6 - determine the busiest time of day for uber pickups based on date/time column
df['Hour'] = df['Date/Time'].dt.hour
hourly_pickup_counts = df.groupby('Hour').size().reset_index(name='Pickup Count')
hour_with_max_pickups = hourly_pickup_counts['Hour'][hourly_pickup_counts['Pickup Count'].idxmax()]
print("Hour with the highest number of pickups:", hour_with_max_pickups)


# In[82]:


# q7 - visualization to represent no. of uber pickups over time 
grouped = df.groupby('Date/Time').size().reset_index(name = 'count')
plt.figure(figsize = (12,5))
plt.plot(grouped['Date/Time'],grouped['count'])
plt.title('pickup counts')
plt.xlabel('Date/Time')
plt.ylabel('count')
plt.legend()
plt.grid(True)
plt.show()


# In[88]:


# q8 - scatter plot to visualize distribution of uber pickups basec on latitude and longitude.

plt.figure(figsize = (12,6))
plt.scatter(df['Lon'],df['Lat'],color='pink',)
plt.title('uber pickups')
plt.xlabel('Lon')
plt.ylabel('Lat')
plt.legend()
plt.grid(True)
plt.show()


# In[91]:


# q9 - bar chart to compare the no. of uber pickups for each tlc base company.
grouped = df.groupby('Base').size().reset_index(name = 'count')
plt.bar(grouped['Base'],grouped['count'],color = 'green')
plt.xlabel('Base')
plt.ylabel('count')
plt.show()


# In[96]:


# q10 - create a pie chart to display the % distribution of pickups for each day of the week.

df['DayOfWeek'] = df['Date/Time'].dt.day_name() 
pickup_counts_by_day = df.groupby('DayOfWeek').size().reset_index(name='Pickup Count')
plt.pie(pickup_counts_by_day['Pickup Count'],labels = pickup_counts_by_day['DayOfWeek'],autopct='%1.1f%%')
plt.title('pickup_counts_by_day')
plt.show()


# In[ ]:




