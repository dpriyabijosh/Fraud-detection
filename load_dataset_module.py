#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Fetching the data from a data set and adding it to 2 dictionaries
# @File : Transaction.txt
# @loadData : Dictionary contains all details of the data based on the user id 
# @transactionData :   Inner dictionary with Transactionid as key 
loadData = {}
transactionData={}
try:
    for line in open('Assignment_dataset/Transaction.txt','r',encoding ="ISO-8859-1"):
        (userId, transactionid, description, amount, x_co, y_co, isFraudulent) = line.split(':')
        loadData.setdefault(userId,{})
        loadData[userId][transactionid] = str(description),float(amount),float(x_co),float(y_co),str(isFraudulent)
        transactionData.setdefault(transactionid,{})
        transactionData[transactionid] = str(description),float(amount),float(x_co),float(y_co),str(isFraudulent)
except FileNotFoundError:
    print("The file is not found!!. Please add a valid file in the given path.")


# In[3]:


#  Function to fetch the details of a transaction id based on the requirement
#     @Para transactionid :the transactionid
#     @Para datafetch : the details of particular transaction

def dataWithTransactionId(transactionid,datafetch=None):
    datalist = []
    try:
        tranData =transactionData[str(transactionid)]
        if datafetch==None:
            datalist= list(tranData)
        elif datafetch.lower()=="description":
            datalist = str(tranData[0])
        elif datafetch.lower()=="transactionamount":
            datalist= float(round(tranData[1],2))
        elif datafetch.lower() =="x_co":
            datalist= float(tranData[2])
        elif datafetch.lower() =="y_co":
            datalist= float(tranData[3])
        elif datafetch.lower() =="isfraud":
            datalist= tranData[4]
        else:
            print("Please add the correct details as description, transactionamount, x_co, y_co and isFraud.\n If you need all details please pass the transactionId")
    except KeyError:
        return datalist
    except NameError:
        return datalist
    return datalist


# In[4]:


#  Function to fetch a list of user's all transaction's corresponding list based on the given option
#     @Para userId :the  corresponding userId
#     @Para datafetch : the given option
def returndictionary(userId,datafetch=None):
    detailsList = []
    try:
        data =loadData[str(userId)]
        for x in data:
            val = list(data[x]) 
            if datafetch=="description":
                detailsList.append(val[0])
            elif datafetch=="transactionamount":
                detailsList.append(round(val[1],2))
            elif datafetch =="x_co":
                detailsList.append(val[2])
            elif datafetch =="y_co":
                detailsList.append(val[3])
            elif datafetch =="isFraud":
                if('true' in val[4]):
                    detailsList.append(x)
            else:
                detailsList.append(val)
    except KeyError:
        return detailsList
    except NameError:
        return detailsList
    return detailsList


# In[5]:


#  Function to print all users
# ENHANCEMENT : To be implemented
def viewAllUsers():
    print('The user ids are..')
    for x in loadData.keys():
        print (x)


# In[6]:


#  Function to print all users
# ENHANCEMENT : To be implemented
def viewAllTransaction():
    print('The transactions are..')
    for x in transactionData.keys():
        print(x)


# In[80]:


#  Function to print all transaction ids of a specific user
# @userId : the user id of the user
def userTransaction(userId):
    listTransaction =[]
    try:
        data = loadData[str(userId)]
        listTransaction = list(data)
    except KeyError:
        return listTransaction
    except NameError:
        return listTransaction
    return listTransaction


# In[7]:


# Function to get a list of fraudulent transaction tags from fraud-description test data.
def getFraudTag():
    textList=[]
    try:
        f = open("Assignment_dataset/fraud-description.txt")
        text = f.readlines()
        for line in text:
            textList.append(line.replace('\n','')) 
        f.close()
    except FileNotFoundError:
        print("The file is not found!!. Please add a valid file in the given path.")
    finally:
        f.close()
        return textList


# In[8]:


# Function to get a list of genuine transaction tags from description test data.
def getGenuineTransactionTag():
    textList=[]
    try:
        f = open("Assignment_dataset/description.txt")
        text = f.readlines()
        for line in text:
            textList.append(line.replace('\n','')) 
        f.close()
    except FileNotFoundError:
        print("The file is not found!!. Please add a valid file in the given path.")
    finally:
        f.close()
        return textList

