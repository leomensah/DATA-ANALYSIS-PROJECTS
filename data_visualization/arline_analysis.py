import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
# # print(flight.head())

# ## Task 1
coach_flight = flight.coach_price
print(coach_flight.describe())

'''
Coach ticket has an average price of $376.6 with a minimum and maximum
values as $44.42 and $593.6 respectively. $500 would seem as a good price
since it is above the average and within the 75th quartile range.
'''

sns.set_style('whitegrid')
sns.boxplot(flight.coach_price, palette='Set3')
plt.show()
plt.clf()

# ## Task 2
coach_flight_8_hours = flight.coach_price[flight.hours == 8]
print(coach_flight_8_hours.describe())

'''
Eight hours long coach ticket prices have an average of 431.8 dollars with 
a minimum and maximum value of 170 dollars and 593 dollars respectively. 
'''


sns.boxplot(coach_flight_8_hours)
sns.set_palette('Set1')
sns.set_style('darkgrid')
plt.show()
plt.clf()



# ## Task 3
print(flight['delay'].describe())

'''
The mean fligh delay is 13 minutes with a minimum value of 0.0
and maximum value of 1560 minutes
'''

fig, ax = plt.subplots(figsize=(12, 7))
sns.histplot(data=flight, x='delay')
sns.boxplot(data=flight, x='delay')
plt.show()

'''
The graph for the delay in flight shows a lot of outliers and hence
histogram plot and boxplot are not performing well in visualizing the 
dataset well.
Therefore I will have to subset the data around the mean and visualize the 
dataset. 
'''

flight_delay_less_15 = flight.delay[(flight['delay'] <= 15)]
print(flight_delay_less_15.describe())
sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(12, 7))
sns.boxplot(flight_delay_less_15)
plt.show()

plt.clf()

sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(12, 7))
sns.displot(flight_delay_less_15)
plt.show()

'''
From the graph shown the critical delay times are mostly around
10 minutes
'''

# Task 4
#Visualizing the relationship between coach and first-class prices
columns = [firstclass_price, coach_price]

sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(12, 7))
sns.scatterplot(x = flight['coach_price'], y = flight['firstclass_price'])
plt.show()

'''
From the graph shown from this two variables, it can be observed that, 
there is a positive correlation between these two variable, hence the coach 
price increases with increasing first class price. Therefore, we can conclude 
that flights with higher coach prices also have a higher first-class price.
'''


# ## Task 5
columns = [inflight_meal, inflight_entertainment, inflight_wifi, coach_price]
sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(12, 7))
sns.boxplot(x=flight['inflight_meal'], y=flight['coach_price'], hue=flight['inflight_entertainment'])
plt.show()

sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(12, 7))
sns.boxplot(x=flight['inflight_wifi'], y=flight['coach_price'])
plt.show()
plt.clf()

sns.boxplot(x=flight['inflight_meal'], y=flight['coach_price'])
plt.show()

plt.clf()

sns.boxplot(x=flight['inflight_entertainment'], y=flight['coach_price'])
plt.show()

plt.clf()
sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(12, 7))
sns.violinplot(x=flight['inflight_wifi'], y=flight['coach_price'])
plt.show()
plt.clf()

sns.violinplot(x=flight['inflight_meal'], y=flight['coach_price'])
plt.show()

plt.clf()

sns.violinplot(x=flight['inflight_entertainment'], y=flight['coach_price'])
plt.show()

'''
Using the bar plot to compare the prices of whether there is a wifie in the 
plane or not. it can be observed that coaches with wifi has a higher price
than coaches without the wifi. the width of both plots also shows the price range within the groups are closer together which means that, there is a
similar price range among coaches with prices so as coaches without wifi. 

Conversely, there is not much of a difference between prices of coaches on 
the inflight meal. This means inflight meal does not affect the coaches.

Moreover, there is a relatively huge difference between prices of coaches with
entertainment and coaches without entertainment. This makes entertainment 
have an impact on the prices of coaches.

In conclusion, we can say that coach prices is being affected by both 
the inflight entertainment and the availability of wifi.
'''

# ## Task 6
columns = ['passenger', 'miles']
flight_pass_miles = flight[['passengers', 'miles']]
print(flight_pass_miles.head())

sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(12, 7))
sns.scatterplot(x=flight['passengers'],y = flight['miles'], data=flight_pass_miles)
plt.show()

'''
There are too many counts of data in this dataset to visualize the relationship.
therefore the pearson correlation was used to compare the relationship between the variables. It was found out that, there is no significant relationtionship between the passengers and length of travel.
'''
from scipy.stats import pearsonr
corr = pearsonr(flight['passengers'], flight['miles'])
print(corr)

plt.clf()

print(flight_pass_miles.describe())

sns.histplot(x=flight['passengers'],  data=flight_pass_miles)
plt.show()
plt.clf()

sns.histplot(x=flight['miles'],  data=flight_pass_miles)
plt.show()
plt.clf()

sns.boxplot(x=flight['passengers'],  data=flight_pass_miles)
plt.show()
plt.clf()

sns.boxplot(x=flight['miles'],  data=flight_pass_miles)
plt.show()

plt.clf()

sns.violinplot(x=flight['passengers'],  data=flight_pass_miles)
plt.show()
plt.clf()

sns.violinplot(x=flight['miles'],  data=flight_pass_miles)
plt.show()


sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(12, 7))
sns.histplot(x=flight['passengers'],y = flight['miles'], data=flight_pass_miles)
plt.show()

## Task 7'
columns = ['day_of_week', 'weekend', 'coach_price', 'firstclass_price']
data1 = flight[columns]
# print(data1.head())

# Visualizing the relationship of the coach_price on week day
sns.set_style('whitegrid')
sns.boxplot(x=data1['weekend'],y = data1['coach_price'], data=data1)
plt.show()

plt.clf()
sns.set_style('whitegrid')
sns.boxplot(x=data1['day_of_week'],y = data1['firstclass_price'], data=data1)
plt.show()
plt.clf()

sns.set_style('whitegrid')
sns.boxplot(x=data1['day_of_week'],y = data1['coach_price'], data=data1)
plt.show()

plt.clf()
sns.set_style('whitegrid')
sns.boxplot(x=data1['weekend'],y = data1['firstclass_price'], data=data1)
plt.show()

## Task 8
plt.clf()
sns.set_style('whitegrid')
sns.boxplot(x=flight['day_of_week'],y = flight['coach_price'], hue=flight['redeye'], data=flight)
plt.show()






