import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/AZ/Desktop")
print(os.getcwd())
#check our working directory

covid_data = pd.read_csv("full_data.csv")
print(covid_data.describe())
print(covid_data.iloc[0:10:2,0:5])
print(covid_data.iloc[0:1000:100,2])


my_colummns=[True,True,False,True,False,False]
print(covid_data.iloc[0:3,my_colummns])

print(covid_data.loc[2:4,"date"])
lc=covid_data.loc[:,"location"]
Afghanistan=[]
for i in lc:
    if i=="Afghanistan":
        Afghanistan.append(True)
    else:
        Afghanistan.append(False)
print(covid_data.loc[Afghanistan,"total_cases"])

lc=covid_data.loc[:,"date"]
march31=[]
for i in lc:
    if i=="2020-03-31":
        march31.append(True)
    else:
        march31.append(False)
new_data=covid_data.loc[march31,:]
mean_cases=np.mean(new_data.loc[:,"new_cases"])
print(mean_cases)
mean_deaths=np.mean(new_data.loc[:,"new_deaths"])
print(mean_deaths)
                
plt.boxplot(new_data.loc[:,"new_cases"])
plt.title("new cases of different countries on 31 March 2020")
plt.show()
plt.boxplot(new_data.loc[:,"new_deaths"])
plt.title("new deaths of different countries on 31 March 2020")
plt.show()

world_dates = covid_data.loc[:,"date"]
world_new_cases = covid_data.loc[:,"new_cases"]
world_new_deaths = covid_data.loc[:,"new_deaths"]
plt.plot(world_dates,world_new_cases,"bo")
plt.show()

output=[]
country_over_8000infects=new_data.loc[new_data["total_cases"]>8000,"location"]
for i in country_over_8000infects:
    if i !="World":
        output.append(i)
print("These countries have infections over 8000:",output)
