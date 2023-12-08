# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 05:58:23 2023

@author: Ananya
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data=pd.read_excel("articles.xlsx")

data.describe() #summary of the table

data.info() #summary of the coloumns

#counting the number of articles by source id
data.groupby(["source_id"])["article_id"].count()

#number of reaction by publisher
data.groupby(["source_id"])["engagement_reaction_count"].sum()

#dropping the unwanted column
data=data.drop("engagement_comment_plugin_count", axis=1)

#defining a function to create a list of flags
#based on a certain keyword is present in the title or not
def keywordFlag(keyword):
    keyword_flag=[]
    for i in range(len(data)):
        try:
            if keyword.lower() in data['title'][i].lower():
                flag=1
            else:
                flag=0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

#calling the function and creating a series/column in the dataframe
data['Keyword_Flag']=pd.Series(keywordFlag("Murder"))

#creating a object of SentimentIntensityAnalyzer class
sent_list=SentimentIntensityAnalyzer()
#sent=sent_list.polarity_scores(data['title'][15])
title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]

#loading the sentimental data into lists
for i in range(len(data)):
    try:
        sent=sent_list.polarity_scores(data['title'][i])
        neg=sent['neg']
        pos=sent['pos']
        neu=sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

#creating a series on sentimental data
data['title_neg_sentiment']=pd.Series(title_neg_sentiment)
data['title_pos_sentiment']=pd.Series(title_pos_sentiment)
data['title_neu_sentiment']=pd.Series(title_neu_sentiment)

#writing the tdataframe into a excel file
data.to_excel('blogme.clean.xlsx',sheet_name='blogmedata',index=False)
    
