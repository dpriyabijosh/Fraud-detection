#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Function that returns the minimum and maximum of user's transaction based on their transaction locations.
# @userId : user id of the user
from load_dataset_module import returndictionary
def maximumMinimumTransaction(userId):
    minValue,maxValue =0,0
    try:
        rslt = returndictionary(str(userId),"transactionamount")
        asceSortedlist = sorted(rslt)
        minValue=asceSortedlist[0]
        maxValue = asceSortedlist[-1]
    except ValueError:
        print( "You have not entered an integer" )
    except:
         print( "Unexpected Error occured" )
    finally:
        return minValue,maxValue


# In[4]:


#Function that returns the location centroid of any user based on their transaction locations.
# @userId : user id of the user
from load_dataset_module import returndictionary
def getCentroid(userId):
    centroid=0
    try:
        latitude = returndictionary(str(userId),"x_co")
        longitude = returndictionary(str(userId),"y_co")
        centroid =(round(sum(latitude)/len(latitude),2)),round((sum(longitude)/len(longitude)),2)
    except ZeroDivisionError :
        print( "Division  by zero is not allowed" )
    except ValueError:
        print( "You have not entered an integer" )
    except:
         print( "Unexpected Error occured" )
    finally:
        return centroid


# In[5]:


#  Function that computes the standard deviation of transactions of any user.
# @userId : user id of the user
from load_dataset_module import returndictionary
def getStandardDeviation(userId):
    stddev=0
    try:
        data = returndictionary(str(userId),"transactionamount")
        mean = round((sum(data)/len(data)),2)
        deviations = [(x - mean) ** 2 for x in data]
        variance = sum(deviations) / len(data) # variance = Sum of deviation/length
        stddev =variance**0.5 # standard deviation is sq.root of variance
    except ZeroDivisionError :
        print( "Division  by zero is not allowed" )
    except ValueError:
        print( "You have not entered an integer" )
    except:
         print( "Unexpected Error occured" )
    return round(stddev,2)


# In[6]:


#  A function that computes the variance of any given user’s transactions.
# @userId : user id of the user
from load_dataset_module import returndictionary
def getVariance(userId):
    variance =0.0
    try:
        data = returndictionary(str(userId),"transactionamount")
        mean = round((sum(data)/len(data)),2)
        deviations = [(x - mean) ** 2 for x in data]
        variance = sum(deviations) / len(data)
    except ZeroDivisionError :
        print( "Division  by zero is not allowed" )
    except ValueError:
        print( "You have not entered an integer" )
    except:
         print( "Unexpected Error occured" )
    return round(variance,2)


# In[7]:


# A function to check the given transaction is fraudulent or not.
# @transactionid : transaction id of the user
from load_dataset_module import * 
def isFraud(transactionid):
    data = dataWithTransactionId(str(transactionid),'isFraud')
    description = dataWithTransactionId(str(transactionid),'description')
    if 'true' in str(data) and description in getFraudTag() : 
        print('The transaction id {} is fraudulent.\n'.format(transactionid))
        print('The details of the transaction are given below;')
        print('Transaction amount : ',dataWithTransactionId(str(transactionid),'transactionamount'))
        print('Location(x,y) : ',dataWithTransactionId(str(transactionid),'x_co'),',',dataWithTransactionId(str(transactionid),'y_co'))
        print('Transaction Description : ', dataWithTransactionId(str(transactionid),'description'))
    elif 'false' in str(data) and description in getGenuineTransactionTag() : 
        print('The transaction id {} is not fraudulent.'.format(transactionid))
        print('The transaction Description is ', dataWithTransactionId(str(transactionid),'description'))
    else:
        print('Wrong user id entered!! Please enter a valid user id')      


# In[8]:


# A function to show the fraudulent transaction of a user.
# @userId : user id of the user
from load_dataset_module import *
def listFraudTransaction(userId):
    data=returndictionary(userId,"isFraud")
    return data


# In[9]:


# A function to find distance from the centroid of the user.
# @userId : user id of the user
#@transactionId : transaction id which we need to find the distance
from load_dataset_module import dataWithTransactionId
def distanceTransactionFromCentroid(userId,transactionId):
    centroid_x,centroid_y = getCentroid(str(userId))
    x, y = (dataWithTransactionId(transactionId,"x_co")),(dataWithTransactionId(transactionId,"y_co"))
    distance =(((centroid_x-x)**2) + ((centroid_y-y)**2)**0.5)#Equation to find distance between locations
    return round(distance,2)


# In[10]:


# A function to find distance from the centroid of the user.
# @userId : user id of the user
#@transactionId : transaction id which we need to find the distance
from load_dataset_module import *
def verifyTransactionOfSameUser(userid,transaction):
    try:
        transactionCheck=[]
        transactionCheck =loadData[str(userid)][str(transaction)]
    except KeyError:
        print('The transactionId {} does not belong to the user with userId {}'.format(transaction, userid))
    if transactionCheck!=[]:
        return True
    else:
        return False


# In[11]:


# A function to return the data set by entering
# @transactionId : user id of the user
#@datafetch : type of data needed
from load_dataset_module import transactionData
def dataWithTransactionId(transactionId,datafetch='all'):
    d =transactionData[str(transactionId)]
    if datafetch=="all":
        lst= list(d)
    elif datafetch=="description":
        lst = str(d[0])
    elif datafetch=="transactionamount":
        lst= float(round(d[1],2))
    elif datafetch =="x_co":
        lst= float(d[2]) 
    elif datafetch =="y_co":
        lst= float(d[3])
    elif datafetch =="isFraud":
        lst= str(d[4])
    else:
        print("Incorrect operation")
    return lst


# In[12]:


# A function to verify the transactions is of the given user 
# @userId : user id of the user
#@transaction : given transaction id
from load_dataset_module import *
def verifyTransactionOfSameUser(userid,transaction):
    try:
        transactionCheck=[]
        transactionCheck =loadData[userid][transaction]
    except KeyError:
        print('The transactionId {} does not belong to the user with userId {}'.format(transaction, userid))
    if transactionCheck!=[]:
        return True
    else:
        return False


# In[13]:


# A function to verify the distance between two transactions
# @transactionId1 : user id of the user
#@transactionId2 : given transaction id
from load_dataset_module import transactionData
def distanceBtnTwoTransactions(transactionId1,transactionId2):
    distance = 0.0
    try:
        x1 = (dataWithTransactionId(str(transactionId1),"x_co"))
        y1 = (dataWithTransactionId(str(transactionId1),"y_co"))
        x2 = (dataWithTransactionId(str(transactionId2),"x_co"))
        y2 = (dataWithTransactionId(str(transactionId2),"y_co"))
        distance =(((x2-x1)**2) + ((y2-y1)**2)**0.5)#Equation to find distance between locations
    except TypeError:
        print('Please check the transaction id. Whole numbers are only allowed')
    return round(distance,2)  


# In[14]:


# A function to verify the distance between two transactions of same user
#@userId : user id of the user
# @transactionId1 : 1st transaction id of the user
#@transactionId2 : 2nd transaction id of the user
def distanceBtnTwoTransactionsOfAUser(userId, transactionId1,transactionId2):
    distance =0;
    try:
        if(verifyTransactionOfSameUser(userId,transactionId1)):
            if(verifyTransactionOfSameUser(userId,transactionId2)):
                distance = (distanceTransactionFromCentroid(userId,transactionId1)-distanceTransactionFromCentroid(userId,transactionId2))
            else:
                print('The transaction id {} does not belongs to user {}'.format(transactionId2,userId))
        else:
            print('The transaction id {} does not belongs to user {}'.format(transactionId1,userId))
    except:
        print('Unexpected error')
    finally:
        round(distance,2)


# In[15]:


# A function to verify the distance of a transaction from the centroid
#@userId : user id of the user
# @transactionId : 1st transaction id of the user
from load_dataset_module import dataWithTransactionId
def distanceTransactionFromCentroid(userId,transactionId):
    if(verifyTransactionOfSameUser(userId,transactionId)):
        centroid_x,centroid_y = getCentroid(userId)
        x, y = (dataWithTransactionId(transactionId,"x_co")),(dataWithTransactionId(transactionId,"y_co"))
        distanceFromCentroid =(((centroid_x-x)**2) + ((centroid_y-y)**2)**0.5)
    return round(distanceFromCentroid,2)

