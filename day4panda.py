# Databricks notebook source
list = [1,2,3,4,5]

print(list[1])


# COMMAND ----------

import pandas as pd

# COMMAND ----------

dict1 = {key : "value", "word1" : "definition", "value1" : 12}
df = pd.DataFrame({})

print(dict1["key"]) 

# COMMAND ----------

df = pd.DataFrame({
    "a" : [1,2,3],
    "b" : [4,5,6],
    "C" : [7,8,9],
}, index = [1,2,3])

df2 = pd.DataFrame(
    [[1,2,3],[4,5,6],[7,8,9]],
    index=[1,2,3],
    columns = ["a", "b", "c"])

print(df)
print("break")
print(df2)

# COMMAND ----------

df.loc[#row,#colum]
df.iloc[#row,#colum]

df.loc[#row,[column,#column]] # get that colum to that column on that row

df.loc [:"a"]
df.iloc[:,0]
    
pd.conccat([df,df], axis=1)
pd.concat([df,df])
    


# COMMAND ----------

df.sort_values("a", ascending=False)

df.sort_values(1, axis=1, ascending=False)


df.drop(columns="c")
df.drop([1,3])

print(df.t) #slips column and  row


# COMMAND ----------

tipsData = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

print(tipsData.describe())

print(tipsData.insull().sum())



# COMMAND ----------

tipsData.groupby(["day"]).count()

# COMMAND ----------

tipsData.groupby(["day"]).sum()

# COMMAND ----------

totalTips = tipsData.groupby(["day"]).sum()["tip"]
totalBill = tipsData.groupby(["day"]).sum()["total_bill"]

tipDayPercentage = (100 * totalTips / totalBill)

tipDayPercentage = tipDayPercentage.to_frame('tip(%)').reset_index()

print(tipDayPercentage)

# COMMAND ----------

name = input('name')
print('hi', name)


