import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

corona_dataset_csv=pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head(10)
corona_dataset_csv.shape
corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)
corona_dataset_csv.head(10)
# Aggregating the rows by the country
corona_dataset_aggregated=corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.head()
corona_dataset_aggregated.shape
corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()
corona_dataset_aggregated.loc['China'][:3].plot()
# caculating the first derivative of the curve
corona_dataset_aggregated.loc["China"].diff().plot()
# find maxmimum infection rate for China
corona_dataset_aggregated.loc["China"].diff().max()
corona_dataset_aggregated.loc["Italy"].diff().max()
corona_dataset_aggregated.loc["Spain"].diff().max()
# find maximum infection rate for all of the countries. 
countries =list(corona_dataset_aggregated.index)
max_infection_rates=[]
for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_infection_rate"]=max_infection_rates
corona_dataset_aggregated.head()
corona_data=pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])
corona_data.head()
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis
hapiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")
hapiness_report_csv.head()
useless_cols=["Overall rank","Score","Generosity","Perceptions of corruption"]
hapiness_report_csv.drop(useless_cols, axis=1,inplace=True)
hapiness_report_csv.head()
# changing the indices of the dataframe
hapiness_report_csv.set_index("Country or region", inplace=True)


corona_data.head()
corona_data.shape
hapiness_report_csv.head()
hapiness_report_csv.shape

data = corona_data.join(hapiness_report_csv, how="inner")
data.head()
data.corr()
data.head()
# ### Task 5.1: Plotting GDP vs maximum Infection rate
x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))


# Plotting Social support vs maximum Infection rate

# Plotting Healthy life expectancy vs maximum Infection rate

# Plotting Freedom to make life choices vs maximum Infection rate

