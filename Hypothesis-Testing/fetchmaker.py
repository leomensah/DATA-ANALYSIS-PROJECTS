# Import libraries
import numpy as np
import pandas as pd
import codecademylib3
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Import data
dogs = pd.read_csv('dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

print(dogs.head())
whippet_rescue = dogs.is_rescue[(dogs.breed == 'whippet')]
print(whippet_rescue)

num_whippet_rescues = np.sum(whippet_rescue == 1)
print(num_whippet_rescues)

num_whippets = len(dogs[dogs.breed == 'whippet'])
print(num_whippets)

pval = binom_test(x = num_whippet_rescues, n=num_whippets, p = 0.08)
print(pval)

wt_whippets = dogs.weight[(dogs.breed == 'whippet')]
wt_terriers = dogs.weight[(dogs.breed == 'terrier')]
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']


tstats, pval = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print(pval)

"p value is less than threshold frequency hence we reject the hypothesis and conclude that, there is a significance difference of weight between at least a pair of breeds"

tukey_results = pairwise_tukeyhsd(endog = dogs_wtp.weight, groups = dogs_wtp.breed, alpha = 0.05)
print(tukey_results)

# print(dogs_ps)
Xtab = pd.crosstab(dogs_ps.breed, dogs_ps.color)
print(Xtab)

chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)
