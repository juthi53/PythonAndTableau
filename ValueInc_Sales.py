# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

#reading the CSV file
data=pd.read_csv('transaction2.csv',sep=';')#read a file

data.info()#show all the table structure

#creating new columns after applying some calculatons
data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']
data['SellingPricePerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']

data['ProfitPerTransaction']=data['SellingPricePerTransaction']-data['CostPerTransaction']
data['Markup']=(data['SellingPricePerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']
data['Markup']=round(data['Markup'],2)

data.info()

#populating a date type column joining year, month and day columns
data['Date']=data['Year'].astype(str)+'/'+data['Month']+'/'+data['Day'].astype(str)
print(data['Date'].dtype)

print(data.iloc[0:3])#show first 3 rows
data.iloc[:-5]#last 5 rows
data.head(5)#show first 5 rows by default 5 rows
data.iloc[0:5,4]#show 5 rows of 4th column

#replacing '[',']' into '' from ClientKeywords column
data['ClientKeywords']=data['ClientKeywords'].str.replace('[','')
data['ClientKeywords']=data['ClientKeywords'].str.replace(']','')

#spliting the ClientKeywords column after every ',' and loading data into dataframe
split_str=data['ClientKeywords'].str.split(',' ,expand=True)

#creating new columns for the split columns in ClientKeywords
data['ClientAge']=split_str[0]
data['ClientType']=split_str[1]
data['LengthofContract']=split_str[2]

#using the lower function
data['ItemDescription']=data['ItemDescription'].str.lower()

#merging two files joining by Month column
seasons=pd.read_csv('value_inc_seasons.csv',sep=';')
data=pd.merge(data,seasons,on='Month')

#dropping unwanted columns
data=data.drop('Day',axis=1)
data=data.drop(['Year','Month','ClientKeywords'],axis=1)

#writing the data into csv file
data.to_csv('ValueINC_Cleaned.csv',index=False)