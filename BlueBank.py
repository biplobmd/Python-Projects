# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:02:15 2024

@author: biplo
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing Json File
json_file=open('loan_data_json.json')
data = json.load(json_file)

# Transform to Dataframe
loandata = pd.DataFrame(data)


# Using EXP() to get the annual income from 'log.annual.inc'
income = np.exp(loandata['log.annual.inc'])
loandata['AnnualIncome'] = income

# Applying for loops to create a category list based on Fico number
length = len(loandata)
FicoCategory = []
for x in range (0,length):
   fico = loandata['fico'][x]
   if fico >= 300 and fico < 400: 
       category ='Very Poor'
   elif fico >= 401 and fico < 600: 
       category = 'Poor'
   elif fico >= 601 and fico < 660: 
       category = 'Fair'
   elif fico >= 660 and fico < 700: 
       category = 'Good'
   elif fico >= 700:
       category = 'Excellent'
   else:
        category = 'Excellent'
        
   FicoCategory.append(category)

# Converting FicoCategory into a series
FicoCategory = pd.Series(FicoCategory)

# Adding FicoCategory column into the dataset
loandata['fico.category'] = FicoCategory

# Using df.loc as a conditional statement to create a new column for Interest Rate 

loandata.loc[loandata['int.rate'] > 0.12, ['int.rate.type']] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, ['int.rate.type']] = 'Low'

# number of loans/rows by category and graph to visualize the data
CategoryPlot = loandata.groupby('fico.category').size()
CategoryPlot.plot.bar(color = 'Green')
plt.show()

PurposeCount = loandata.groupby('purpose').size()
PurposeCount.plot.bar(color = 'Red')
plt.show()


# Scatter Plot
xpoint = loandata['dti']
ypoint = loandata['AnnualIncome']
plt.scatter(xpoint,ypoint, color = '#4caf50')
plt.show()

# Export to CXV
loandata.to_csv('loanData.csv', index = True)













