# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:03:59 2023

@author: Ananya
"""
import pandas as pd
import numpy as np
import json

#method 1 to read json data
json_file=open('loan_data_json.json')
data=json.load(json_file)

#method 2 to read Json data
with open('loan_data_json.json') as json_file:
    data=json.load(json_file)

#transforming the json data to dataframe
loandata= pd.DataFrame(data)

# finding unique values for purpose column
loandata['purpose'].unique()

#describe the dataframe
loandata.describe()

#creating a new columns by conditionl statement using loc
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate_type']='High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate_type']='Low'

try:
    loandata.loc[(loandata['fico'] >=300) & (loandata['fico']<400), 'fico.category']='Very Poor'
    loandata.loc[(loandata['fico'] >=400) & (loandata['fico']<600), 'fico.category']='Poor'
    loandata.loc[(loandata['fico'] >=601) & (loandata['fico']<660), 'fico.category']='Fair'
    loandata.loc[(loandata['fico'] >=660) & (loandata['fico']<700), 'fico.category']='Good'
    loandata.loc[loandata['fico'] >=700 , 'fico.category']='Excellent'
except:
    loandata['fico']='unknown'
#using exp() to get the annual income
loandata['annual_income']=np.exp(loandata['log.annual.inc'])

#writing the data into a csv file and adding an index to the file
loandata.to_csv('loan_cleaned.csv',index=True)
