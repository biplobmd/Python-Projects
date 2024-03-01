# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 00:05:55 2023

@author: biplo
"""

import pandas as pd

# file_name=pd.read_csv('file.csv') <---- format of read_csv

data=pd.read_csv('transaction.csv')

data=pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

# Working with calculations


CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction= CostPerItem * NumberOfItemsPurchased

# Adding a new column to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

# Sales Per Transaction

data['SalesPerTransaction']= data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = Sales - Cost
data ['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup Calcultion = (Sales - Cost) / Cost
data['Markup'] =round(data ['ProfitPerTransaction'] / data['CostPerTransaction'],2)

#Combining Data Fields and Converting Integer to String
data['Date'] = data['Day'].astype(str)+"-"+data['Month']+"-"+data['Year'].astype(str)

# Using Split to split the Client_Keywords field

split_col=data["ClientKeywords"].str.split("," , expand=True)

# Creating New Columns based of the splitted columns from Client_Keyword field
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

# Using the Replace Function to remove Square Bracets from new columns

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#Using the Lower function to change value to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

# Bringinging in a new dataset
seasons=pd.read_csv('value_inc_seasons.csv' , sep=";")

# Merging two datasets
data = pd.merge(data, seasons, on='Month')

# Dropping unnessecary columns
data = data.drop(['ClientKeywords','Year','Month','Day'], axis= 1)


# Export into CSV
data.to_csv('ValueInc_cleaned.csv', index= False)

