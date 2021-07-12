#!/usr/bin/env python
# coding: utf-8

# # Welcome to Covid19 Data Analysis Notebook
# ------------------------------------------

# ### Let's Import the modules 

# In[3]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ## Task 2 

# ### Task 2.1: importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 
# 

# In[5]:


corona_dataset_csv=pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head(10)


# #### Let's check the shape of the dataframe

# In[6]:


corona_dataset_csv.shape


# ### Task 2.2: Delete the useless columns

# In[7]:


corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)


# In[8]:


corona_dataset_csv.head(10)


# ### Task 2.3: Aggregating the rows by the country

# In[9]:


corona_dataset_aggregated=corona_dataset_csv.groupby("Country/Region").sum()


# In[10]:


corona_dataset_aggregated.head()


# In[11]:


corona_dataset_aggregated.shape


# ### Task 2.4: Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

# In[12]:


corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()


# ### Task3: Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# In[13]:


corona_dataset_aggregated.loc['China'].plot()


# In[14]:


corona_dataset_aggregated.loc['China'][:3].plot()


# ### task 3.1: caculating the first derivative of the curve

# In[15]:


corona_dataset_aggregated.loc["China"].diff().plot()


# ### task 3.2: find maxmimum infection rate for China

# In[19]:


corona_dataset_aggregated.loc["China"].diff().max()


# In[20]:


corona_dataset_aggregated.loc["Italy"].diff().max()


# In[21]:


corona_dataset_aggregated.loc["Spain"].diff().max()


# ### Task 3.3: find maximum infection rate for all of the countries. 

# In[47]:


countries =list(corona_dataset_aggregated.index)
max_infection_rates=[]
for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_infection_rate"]=max_infection_rates


# In[51]:


corona_dataset_aggregated.head()


# ### Task 3.4: create a new dataframe with only needed column 

# In[49]:


corona_data=pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])


# In[50]:


corona_data.head()


# ### Task4: 
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# ### Task 4.1 : importing the dataset

# In[53]:


hapiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")


# In[55]:


hapiness_report_csv.head()


# ### Task 4.2: let's drop the useless columns 

# In[58]:


useless_cols=["Overall rank","Score","Generosity","Perceptions of corruption"]


# In[59]:


hapiness_report_csv.drop(useless_cols, axis=1,inplace=True)
hapiness_report_csv.head()


# ### Task 4.3: changing the indices of the dataframe

# In[63]:


hapiness_report_csv.set_index("Country or region", inplace=True)


# ### Task4.4: now let's join two dataset we have prepared  

# #### Corona Dataset :

# In[67]:


corona_data.head()
corona_data.shape


# #### wolrd happiness report Dataset :

# In[68]:


hapiness_report_csv.head()
hapiness_report_csv.shape


# In[70]:


data = corona_data.join(hapiness_report_csv, how="inner")
data.head()


# ### Task 4.5: correlation matrix 

# In[71]:


data.corr()


# ### Task 5: Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[72]:


data.head()


# ### Task 5.1: Plotting GDP vs maximum Infection rate

# In[74]:


x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))


# In[75]:


sns.regplot(x,np.log(y))


# ### Task 5.2: Plotting Social support vs maximum Infection rate

# In[ ]:





# In[ ]:





# ### Task 5.3: Plotting Healthy life expectancy vs maximum Infection rate

# In[ ]:





# In[ ]:





# ### Task 5.4: Plotting Freedom to make life choices vs maximum Infection rate

# In[ ]:





# In[ ]:




