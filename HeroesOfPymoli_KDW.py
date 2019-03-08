
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = 'purchase_data.csv'

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[2]:


#find unique players 
playerCount = len(purchase_data['SN'].unique())
#count players ensure no duplicates
totalPlayers = pd.DataFrame({'Total PLayers':[playerCount]})
totalPlayers


# In[2]:





# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


#identify unique items
itemCount = len(purchase_data['Item ID'].unique())
#caluculate avg price and round 
averagePrice = round(purchase_data['Price'].mean()/1,2)
#count purchase from the main data set 
purchaseCount = len(purchase_data['Purchase ID'].value_counts())
#calculate total Revenue
revenueTotal = purchase_data['Price'].sum()

#build data set and clean up data with , and $ with formating
purchaseAnalysis = pd.DataFrame({'Number of Unique Items':[itemCount],'Average Price':f'${averagePrice}',
                                 'Number of Purchases':[purchaseCount], 'Total Revenue':[revenueTotal]})
purchaseAnalysis['Total Revenue'] = purchaseAnalysis['Total Revenue'].astype(float).map('${:,.2f}'.format)
purchaseAnalysis


# In[3]:





# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[4]:


# group up data on Gender and Screen name to enusre no duplicates are counted
grpBy = purchase_data.groupby(['Gender'])[['SN']].nunique().rename(columns={'SN':'Total Count'})
#calculate average of players by gender
genderPer = (grpBy/grpBy.sum()*100).round(2).rename(columns={'Total Count':'Percentage of Players'})
# join the data with a concat
genTotal = pd.concat([grpBy,genderPer],axis =1)
#sort the data from larger count to smaller
genTotal.sort_values(by=['Total Count'],ascending=False)


# In[4]:





# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[5]:


# get the purchase count from data set
purchGender = purchase_data.groupby(['Gender'])[['Price']].count().rename(columns={'Price': 'Purchase Count'})
#calculate the average price by gender with means name column
avgPurchPrce = purchase_data.groupby(['Gender'])[['Price']].mean().rename(columns={'Price': 'Average Purchase Price'})
#calculate total purchace price 
totPurchPrce = purchase_data.groupby(['Gender'])[['Price']].sum().rename(columns={'Price': 'Total Purchase Value'})
#set the index
grpBy.index = totPurchPrce.index
#calculate the data on the index with divison set column value
totPurPers = totPurchPrce.div(grpBy['Total Count'], axis='index').rename(columns={'Total Purchase Value': 'Avg Total Purchase per Person'})
#combing the data sets and format the rows
purchTotal = pd.concat([purchGender,avgPurchPrce,totPurchPrce,totPurPers], axis=1)
purchTotal['Average Purchase Price'] = purchTotal['Average Purchase Price'].astype(float).map('${:,.2f}'.format)
purchTotal['Avg Total Purchase per Person'] = purchTotal['Avg Total Purchase per Person'].astype(float).map('${:,.2f}'.format)
purchTotal['Total Purchase Value'] = purchTotal['Total Purchase Value'].astype(float).map('${:,.2f}'.format)
purchTotal.sort_values(by=['Purchase Count'],ascending=False)


# In[5]:





# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[6]:


#identify the max age to ensure bins are correct.
ageMax = purchase_data['Age'].max()
# print(ageMax)

# create Bins for ages and lables
bins = [0, 9, 14, 19, 24, 29, 34, 39, 46]
ageLabel = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
purchase_data['Summary'] = pd.cut(purchase_data['Age'], bins, labels=ageLabel)
# create a bin for each age group
binVal1 = purchase_data.groupby(['Summary']).get_group(('<10'))
plyCT1 = len(binVal1['SN'].unique())
perAge1 = (plyCT1/playerCount)*100

binVal2 = purchase_data.groupby(['Summary']).get_group(('10-14'))
plyCT2 = len(binVal2['SN'].unique())
perAge2 = (plyCT2/playerCount)*100

binVal3 = purchase_data.groupby(['Summary']).get_group(('15-19'))
plyCT3 = len(binVal3['SN'].unique())
perAge3 = (plyCT3/playerCount)*100

binVal4 = purchase_data.groupby(['Summary']).get_group(('20-24'))
plyCT4 = len(binVal4['SN'].unique())
perAge4 = (plyCT4/playerCount)*100

binVal5 = purchase_data.groupby(['Summary']).get_group(('25-29'))
plyCT5 = len(binVal5['SN'].unique())
perAge5 = (plyCT5/playerCount)*100

binVal6 = purchase_data.groupby(['Summary']).get_group(('30-34'))
plyCT6 = len(binVal6['SN'].unique())
perAge6 = (plyCT6/playerCount)*100

binVal7 = purchase_data.groupby(['Summary']).get_group(('35-39'))
plyCT7 = len(binVal7['SN'].unique())
perAge7 = (plyCT7/playerCount)*100

binVal8 = purchase_data.groupby(['Summary']).get_group(('40+'))
plyCT8 = len(binVal8['SN'].unique())
perAge8 = (plyCT8/playerCount)*100
# create bin data for table creation
binTotals = [plyCT1,plyCT2,plyCT3,plyCT4,plyCT5,plyCT6,plyCT7,plyCT8]
perValues = [perAge1,perAge2,perAge3,perAge4,perAge5,perAge6,perAge7,perAge8]
perValues = [round(pr,2) for pr in perValues]
#populate data frame and display table
playDemo = {'Summary':ageLabel, 'Total Count':binTotals, 'Percentage of Players':perValues}

playOutput = pd.DataFrame(playDemo)
playOutput = playOutput.set_index('Summary')
playOutput


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[191]:


purchase_data['Summary'] = pd.cut(purchase_data['Purchase ID'], bins, labels=ageLabel)
avgPurchPrce = purchase_data.groupby(['Summary'])[['Price']].mean().rename(columns={'Price': 'Average Purchase Price'})
totPurchPrce = purchase_data.groupby(['Summary'])[['Price']].sum().rename(columns={'Price': 'Total Purchase Value'})


plyCT1 = len(binVal1['SN'])
plyCT2 = len(binVal2['SN'])
plyCT3 = len(binVal3['SN'])
plyCT4 = len(binVal4['SN'])
plyCT5 = len(binVal5['SN'])
plyCT6 = len(binVal6['SN'])
plyCT7 = len(binVal7['SN'])
plyCT8 = len(binVal8['SN'])

binTotals = [plyCT1,plyCT2,plyCT3,plyCT4,plyCT5,plyCT6,plyCT7,plyCT8]
perValues = [perAge1,perAge2,perAge3,perAge4,perAge5,perAge6,perAge7,perAge8]

purchTotal = pd.concat([avgPurchPrce,totPurchPrce], axis=1)

playDemo = {'Labels':ageLabel, 'Purchase Count':binTotals}

playOutput = pd.DataFrame(playDemo)
playOutput = playOutput.set_index('Labels')
outPut = pd.concat([playOutput, purchTotal], axis=1)
outPut['Average Purchase Price'] = outPut['Average Purchase Price'].astype(float).map('${:,.2f}'.format)
outPut['Total Purchase Value'] = outPut['Total Purchase Value'].astype(float).map('${:,.2f}'.format)
# purchTotal['Total Purchase Value'] = purchTotal['Total Purchase Value'].astype(float).map('${:,.2f}'.format)
outPut


# In[7]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[7]:


#grab the data from the original Data Frame
screenName = purchase_data.groupby(purchase_data['SN'])
#gather all the unique screen names
scnName = screenName['SN'].unique()
#gather all the screenames
scnCount = screenName['Age'].count()
# get the average purchase for each sn name
scnAvgPur = (screenName['Price'].mean())
# populate the total purchase value
scnTotPur = screenName['Price'].sum()
#create empty Data table to add values to
bigSpdr = {'SN':scnName, 'Purchase Count':scnCount, 'Average Purchase Price':scnAvgPur, 'Total Purchase Value':scnTotPur}
#create Data Frane and Print Data
bigSpender = pd.DataFrame(bigSpdr)
bigSpender['SN'] = bigSpender['SN'].str[0]
bigSpender = bigSpender.set_index('SN')
bigSpender = bigSpender.sort_values('Total Purchase Value', ascending=False)
bigSpender = bigSpender[['Purchase Count', 'Average Purchase Price', 'Total Purchase Value']]
bigSpender['Average Purchase Price'] = bigSpender['Average Purchase Price'].astype(float).map('${:,.2f}'.format)
bigSpender['Total Purchase Value'] = bigSpender['Total Purchase Value'].astype(float).map('${:,.2f}'.format)
bigSpender.iloc[:5]


# In[8]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[27]:


#grab the data from the original Data Frame
popItem = purchase_data.groupby(purchase_data['Item ID'])
itemIds = popItem['Item ID'].unique()
# grab all the unique names
nameIds = popItem['Item Name'].unique()
#sort the data 
purCount = popItem['Age'].count()
# locate the unique values
purPrice = popItem['Price'].unique()
# populate the total purchase value
popTotPur = popItem['Price'].sum()
#create empty Data table to add values to
mostPop = {'Item ID':itemIds, 'Item Name':nameIds, 'Purchase Count':purCount, 'Item Price':purPrice, 'Total Purchase Value':popTotPur}
#create Data Frane and Print Data
mostPoplr = pd.DataFrame(mostPop)
mostPoplr['Item ID'] = mostPoplr['Item ID'].str[0]
mostPoplr['Item Name'] = mostPoplr['Item Name'].str[0]
mostPoplr = mostPoplr.set_index('Item ID')
mostPoplr = mostPoplr.sort_values('Purchase Count', ascending=False)
mostPoplr = mostPoplr[['Item Name', 'Purchase Count', 'Item Price', 'Total Purchase Value']]
mostPoplr['Item Price'] = mostPoplr['Item Price'].astype(float).map('${:,.2f}'.format)
mostPoplr['Total Purchase Value'] = mostPoplr['Total Purchase Value'].astype(float).map('${:,.2f}'.format)
mostPoplr.iloc[:5]


# In[9]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[37]:


#use existing data and sort Total Purchase Value Descending 
mostPoplr = mostPoplr.sort_values('Total Purchase Value', ascending=False)
mostPoplr = mostPoplr[['Item Name', 'Purchase Count', 'Item Price', 'Total Purchase Value']]
mostPoplr.iloc[:5]


# In[39]:




