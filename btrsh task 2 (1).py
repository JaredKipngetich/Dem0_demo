#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# Here we are exploring the data to understand it better and to establish the statistical properties of the data.

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("C:\\Users\\User\\OneDrive\\Desktop\\Data//customer_booking.csv", encoding ="ISO-8859-1")
df.head()


# In[4]:


df.info()


# In[5]:


df["flight_day"].unique()


# In[6]:


mapping = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7,
}
df["flight_day"] = df["flight_day"].map(mapping)


# In[7]:


df["flight_day"].unique()


# In[8]:


df.describe()


# # Make a new feature

# We want to establish customer behaviour in order to have a trip on holiday(weekend), so we are goinng to make a feature called
# is_weekend. If the flight day is Saturday or Sunday we give is_weekend value=1, for another value, it is given a value of 0.

# In[9]:


is_weekend = []
for  i in range(len(df)):
    if df['flight_day'][i]==6 or df['flight_day'][i]==7:
        is_weekend.append(1)
    else:
        is_weekend.append(0)
df['is_weekend'] = is_weekend
df.head()


# # Analyze data

# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns

weekend = df.groupby('is_weekend')['num_passengers'].sum().reset_index()
ax = sns.barplot(data = weekend, x = 'is_weekend',y = 'num_passengers')
ax.bar_label(ax.containers[0])
plt.show()


# What is the average number of passengers per day

# In[12]:


dayperday = df.groupby('flight_day')['num_passengers'].mean().reset_index()

ax = sns.barplot(data = dayperday, x = 'flight_day', y= 'num_passengers')
for bar in ax.patches:
    bar.set_facecolor('#888888')
    
ax.bar_label(ax.containers[0])
plt.ylim(0,2)
ax.patches[5].set_facecolor('#aa3333')
ax.patches[6].set_facecolor('#aa3333')
plt.show()


# From the chart, it is evident that the number of passenger on weekends is less than the number of flights on weekdays. If you consider the average, the weekends have a higher value. 
# Let us establish which routes have schedules on weekends with the most passengers.

# In[13]:


route = df[df['is_weekend'] == 1].groupby('route').agg({'num_passengers' : 'sum'}).reset_index().sort_values(by='num_passengers', ascending=False)


# In[14]:


route[:5]


# The routes above have the most passengers, we need to increase the number of flights to these 5 routes on weekends.

# In[ ]:





# # Making a machine learning model

# Dropping columns with many redundant features

# In[15]:


df['route'].value_counts()


# It is clear route has 799 unique values, this is too large a figue and hence we delete route column

# In[16]:


df.drop('route',axis = 1, inplace = True)


# In[17]:


df['booking_origin'].value_counts()


# Let us change the value of booking origin from name of country to name of continent.

# In[18]:


conda update jupyter


# In[19]:


get_ipython().system('pip install -U jupyter')


# In[13]:


get_ipython().system('pip install pycountry_convert')


# In[20]:


get_ipython().system('pip install pycountry')


# In[21]:


import pycountry_convert as pc

continent = []
index = []

df['booking_origin'] =  df['booking_origin'].replace('Myanmar (Burma)', 'Myanmar')

for i in range(len(df)):
    country = df['booking_origin'][i]
    #print(country)
    try :
        country_code = pc.country_name_to_country_alpha2(country, cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        continent.append(continent_name)
    except:
        continent.append('Others')

df['booking_continent'] = continent




# In[22]:


df['booking_continent'].value_counts()


# Now we have less unique values to represent booking origin.

# In[23]:


df.drop('booking_origin', axis = 1, inplace=True)


# # Data Cleaning

# In[24]:


df.sample()


# In[25]:


num = ['num_passengers', 'purchase_lead', 'length_of_stay', 'flight_hour', 'flight_duration']
plt.figure(figsize=(12,8))

for i, column in enumerate (df[num].columns, 1):
    plt.subplot(4,4,i)
    sns.boxplot(data=df[num], x=df[column])
    plt.tight_layout()


# from the charts above, it is evident that length_of_stay & purchase_lead have outlier values. We shall eliminate these outliers.

# In[26]:


from scipy import stats
import numpy as np

print(f'Total rows before delete outlier : {len(df)}')

filtered_entries = np.array([True] * len(df))

for col in num:
    zscore = abs(stats.zscore(df[col]))
    filtered_entries = (zscore < 3) & filtered_entries
    df = df[filtered_entries]
    
print(f'Total rows after delete outlier : {len(df)}')


# In[27]:


plt.figure(figsize=(12,8))

for i, column in enumerate (df[num].columns, 1):
    plt.subplot(4,4,i)
    sns.kdeplot(data=df[num], x=df[column])
    plt.tight_layout()


# In[29]:


from sklearn.preprocessing import Normalizer
num_max = df[num].max()
num_min = df[num].min()

num_features = (df[num]-num_min)/(num_max-num_min)
num_features.head()

df[num] = num_features

plt.figure(figsize = (12,8))


for i, column in enumerate (df[num].columns,1):
    plt.subplot(4,4,i)
    sns.kdeplot(data = df, x=df[column])
    plt.tight_layout()


# # Feature encoding

# In[30]:


from sklearn import preprocessing

label_encode = ['sales_channel']
one_hot = ['booking_continent']
                
mapping_trip_type = {
    'RoundTrip'  : 0,
    'OneWay'     : 1,
    'CircleTrip' : 2
}               

df['trip_type'] = df['trip_type'].map(mapping_trip_type)

df['sales_channel'] = preprocessing.LabelEncoder().fit_transform(df['sales_channel'])

onehots = pd.get_dummies(df['booking_continent'], prefix='booking_continent')
df = df.join(onehots)

df.drop('booking_continent', axis = 1, inplace=True)


# In[31]:


df.head(5)


# In[32]:


from sklearn.model_selection import train_test_split

x = df.drop(columns = ['booking_complete'], axis = 1)
y = df['booking_complete']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# In[33]:


y_train.value_counts(normalize = True)


# As seen above, the data is unbalanced and so we need to balance it by sampling

# # Sampling Data
# 

# In[ ]:


get_ipython().system('pip uninstall scikit-learn')


# In[ ]:


get_ipython().system('pip uninstall imblearn')


# In[ ]:


get_ipython().system('pip install scikit-learn==1.2.2')


# In[ ]:


get_ipython().system('pip install imblearn')


# In[12]:


import imblearn
from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state = 2)

x_over, y_over = sm.fit_resample(x_train, y_train.ravel())


# In[ ]:


get_ipython().system('pip show scikit-learn  # to see which version and where scikit-learn is installed')
get_ipython().system('pip freeze  # to see all packages installed in the active virtualenv')
"import sklearn; sklearn.show_versions()"

