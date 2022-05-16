#### IMPORTING THE MODULES THAT YOU'LL BE USING IN THIS PROJECT ###
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

### LOADING OF CSV FILES ###
df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')
# print(df_goals.sample(20))
# print(df.head())
# print(df.dtypes)
# print(df.shape)
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
# print(df.head())
# print(df.tail())
sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(df['Year'], df['Total Goals'])
sns.set_context('poster', font_scale=0.8)
plt.xticks(rotation=45)
ax.set_title('Graph of Total Goals Scored in a Year')

plt.show()

sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12, 7))
sns.boxplot(x='year', y='goals', data=df_goals, palette='Spectral')
ax2.set_title('Box plot showing goals scored in a year')
plt.xticks(rotation=45)
plt.show()






