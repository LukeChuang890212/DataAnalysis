from scipy import stats 
import numpy as np

import statsmodels.api as sm
from statsmodels.formula.api import ols

import pandas as pd 

old_width = pd.get_option('display.max_colwidth')
pd.set_option('display.max_colwidth', -1)

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) 

def t_test(group1, group2):
    mean1 = np.mean(group1)
    mean2 = np.mean(group2)
    std1 = np.std(group1)
    std2 = np.std(group2)
    nobs1 = len(group1)
    nobs2 = len(group2)
    
    modified_std1 = np.sqrt(np.float32(nobs1)/
                    np.float32(nobs1-1)) * std1
    modified_std2 = np.sqrt(np.float32(nobs2)/
                    np.float32(nobs2-1)) * std2

    (statistic, pvalue) = stats.ttest_ind_from_stats( 
               mean1=mean1, std1=modified_std1, nobs1=nobs1,   
               mean2=mean2, std2=modified_std2, nobs2=nobs2 )
    return mean1, mean2, modified_std1, modified_std2, statistic, pvalue
def anova(aov_data, variable):
    model = ols(variable,data = aov_data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print(anova_table)
    return anova_table
