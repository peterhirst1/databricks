# Databricks notebook source
import numpy as np

# COMMAND ----------

my1dArray = np.array([1,2,3,])
my2dArray = np.array([[1,2,3], [4,5,6]], dtype = float)
my2dArray = np.array(((1,2,3), (4,5,6)), dtype = np.float32)
                      
charArray1 = np.array([(1,'a', 3.),(4,5,'zzz')], dtype="U21")
                      
print(charArray1)

# COMMAND ----------

rows = 4
cols = 3
arrayls = np.ones((rows, cols))

array5s = 5 * np.ones((rows, cols))

array7s = np.full((rows, cols), 7)

print(array5s)
print(array7s)

# COMMAND ----------

samples = 5
step = 3
start = 10
stop = 25 

np.arange(start, stop, step)

np.linspace(start, stop, samples)

np.eye(3)

np.random.random((2,3))

np.random.randint(0,10, (3,3))

# COMMAND ----------

a = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

a.ndim
a.shape
a.size
a.dtype

a[a < 9]
np.diag(a)

# COMMAND ----------

a = np.array([[1,2], [4,5]])
b = np.array([[9,8], [6,5]])

summ1 = a.sum()
summ2 = np.sum(a)

a + b
np.add(a,b)

a - b

a * b

a/b

np.exp(a)

np.sqrt(a)

np.sin(a)
np.cos(a)
np.log(a)

display(a.dot(b))

             

# COMMAND ----------

from numpy import linalg as la

A = np.array([0,0])
B = np.array([0,3])
C = np.array([1,5,0])
AB = np.sqrt(AB_diffSquared)

AB2 = la.norm(A-B)

AC2 = la.norm(A-C)

BC2 = la.norm(B-C)

print(BC2, BC)

# COMMAND ----------

import numpy as np
# import pyspark as ps

# use spark to read the txt file as csv
dataRaw = spark.read.csv(path = "dbfs:/FileStore/IrisData/iris_head_num.txt")
# collect all the data and store it as a np array
dataRaw = np.array(dataRaw.select("*").collect())

#seperate data from header
header = dataRaw[0:]
#select all rows except the first, all columns expect the 4th
data = dataRaw[1:, :4]
#convert data from string to float32
data = np.vstack(data.astype(np.float32))

#select the labels columns
labels = np.vstack(dataRaw[1:, 4].astype(np.int32))

#make an array of unique labels, and the number of labels total
labelsUn, labelsCounts = np.unique(labels, return_counts = 1)
#this shows we have 3 types of flowers and 50 samples
display(labelsUn, labelsCounts)


# COMMAND ----------

outliers2sd = np.zeros((nclasses,ncols))
for i in labelsUn:
    
    indexes = np.reshape(labels==i,nrows)
    classData = data[indexes,:]

    for j in range(ncols):
        thresholdLow = average[i-1,j]-2*sd[i-1,j]
        thresholdHigh = average[i-1,j]+2*sd[i-1,j]

        remain = [x for x in classData[:,j] if(x > thresholdLow)]
        remain = [x for x in classData[:,j] if(x < thresholdHigh)]

        outliers2sd[i-1,j] = 100 * (labelsCounts[i-1] - len(remain)) / labelsCounts[i-1]
print(header)
print(outliers2sd)

# COMMAND ----------



# COMMAND ----------

#Export to spark.csv file
# some variables for formatting
decimals = 2
fmt = "%.2f"
formatf = ".csv"
import pandas as pd
 
# Our data is in all sorts of shapes now after collecting it
# Well put it together, format it, and export it
species = np.array(['setosa','versicolor','virginica'])
# For each of the flowers in our df
for i in range(len(labelsUn)):
    #Stack the statistics generated
    temp = np.vstack( [average[i,:], mini[i,:], maxi[i,:], sd[i,:], outliers2sd[i,:]] ).T
    
    #Round the decimals to the nearest 2 places
    temp = np.around(temp,decimals)

    #Cast numbers to string and format
    temp_str = np.char.mod(fmt, temp)
    #Take header row and transpose it to be a column
    rows = np.array(header[:-1].astype("U"))[:, np.newaxis]
    
    #Put header column next to data
    rowsf = np.hstack((rows, temp_str))
    #make beauty header row for the csv
    headerf = [species[i],'mean','min','max','std','outliers2sd%']
    #Cast to a pandas dataframe, to then be cast to spark dataFrame
    pdDf = pd.DataFrame(rowsf, columns = [headerf])
    #try to write out 4 csvs
    try:
        sparkDf.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("dbfs:/fileStore/tables/irisTest/" + str(species[i]))
    except:
        # unless fiel already exists
        print("file already exists")
    #read back file to make sure everything works
    display(spark.read.csv("dbfs:/fileStore/tables/irisTest/" + str(species[i])))

# COMMAND ----------


