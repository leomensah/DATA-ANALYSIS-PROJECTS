import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import codecademylib3_seaborn

files_list = glob.glob('states*.csv')
states_list = []
for files in files_list:
  data = pd.read_csv(files)
  states_list.append(data)

us_census = pd.concat(states_list)
#print(us_census)

# print(us_census.columns.values)
print(us_census.dtypes)
# print(us_census.head())

us_census['Income'] = us_census.Income.replace({"[\$]":""}, regex=True)
split_gender = us_census.GenderPop.str.split('_')
us_census['Men'] = split_gender.str.get(0)
us_census['Women'] = split_gender.str.get(1)

us_census['Men'] = us_census.Men.str.extract('(\d+)', expand=True)
us_census['Women'] = us_census.Women.str.extract('(\d+)', expand=True)

print(us_census.head())
plt.scatter(us_census.Women, us_census.Men)
plt.show()

# print(us_census['Women'])
print(us_census['Women'].isnull().sum())
us_census_new = us_census
print(us_census_new.dtypes)
print(us_census_new.head())
us_census_new[['Men', 'Women']] = us_census_new[['Men', 'Women']].apply(pd.to_numeric)
print(us_census_new.dtypes)
us_census_new['Women'].fillna((us_census_new['TotalPop'] - us_census_new['Men']), inplace=True)

us_census_new['Women'] = pd.to_numeric(us_census_new['Women'])
print(us_census_new['Women'].isnull().sum())
print(us_census_new.dtypes)
# print(us_census.duplicated())

# print(us_census.shape)
us_census_new.drop_duplicates(inplace=True)
# print(us_census.shape)

plt.scatter(us_census_new.Women, us_census_new.Men)
plt.xlabel('Women')
plt.ylabel('Men')
plt.title('Plot of Men and Women')
plt.show()

print(us_census_new.isna().any())

# us_census_new['White'] = us_census_new['White'].str.strip('%')
us_census_new['Hispanic'] = us_census_new.Hispanic.str.replace('%', ' ').astype(float)
us_census_new['White'] = us_census_new.White.str.replace('%', ' ').astype(float)
us_census_new['Black'] = us_census_new.Black.str.replace('%', ' ').astype(float)
us_census_new['Native'] = us_census_new.Native.str.replace('%', ' ').astype(float)
us_census_new['Asian'] = us_census_new.Asian.str.replace('%', ' ').astype(float)
us_census_new['Pacific'] = us_census_new.Pacific.str.replace('%', ' ').astype(float)
print(us_census_new.head())

plt.hist(us_census_new.Hispanic)
plt.title('A histogram of the Hispanic race')
plt.show()

plt.hist(us_census_new.White)
plt.title('A histogram of the White race')
plt.show()

plt.hist(us_census_new.Black)
plt.title('A histogram of the Black race')
plt.show()

plt.hist(us_census_new.Native)
plt.title('A histogram of the Native race')
plt.show()

plt.hist(us_census_new.Asian)
plt.title('A histogram of the Asian race')
plt.show()

plt.hist(us_census_new.Pacific)
plt.title('A histogram of the Pacific race')
plt.show()

