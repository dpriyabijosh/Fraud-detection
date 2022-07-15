#!/usr/bin/env python
# coding: utf-8

# In[10]:


#The function is to go back to main menu
def goBackToMainMenu():
    main()


# In[11]:


#The function is to exit from the system
def exitFn():
    print('Thank you for your time!!\nHave a good Day!!!\nBye')


# In[12]:


#The Function is to perform the action by transaction id
from user_statistics_module import *#To import the statistics function for the interface
def selectByID(transactionid):
    try:
        chooseOption= str(input('Please choose an option\n1. Check fraudulency \n2. Check distance from another transaction\n3. Go Back to Previous menu\n4. Exit\n'))  
        if chooseOption == str(1):
            isFraud(transactionid)#Checking fraudulency for the given transaction id
            print('\n\n')
            selectByID(str(transactionid))# Go to previous options
            
        elif chooseOption == str(2):
            secondTransactionId = str(input('Please enter your next transaction id to find the distance between both transactions\n'))
            checkingTransactionId = dataWithTransactionId(secondTransactionId)#Checking the distance with another transaction id
            if checkingTransactionId == []:
                print("Please check the second transaction id entered")
                selectByID(str(transactionid))# Go to previous options
            else:
                distanceBetween = distanceBtnTwoTransactions(transactionid,secondTransactionId)
                if distanceBetween == None:
                    print("Please check the transaction id")
                    selectByID(str(transactionid))#Go to previous options
                else:
                    print('The distance between the transaction id {} and transactionid {} is'.format(transactionid,secondTransactionId),distanceBetween)
                    selectByID(str(transactionid))#Go to previous options
        elif chooseOption == str(3):
                goBackToMainMenu()#Go to previous options
        elif chooseOption == str(4):
                exitFn()#Go to previous options
        else:
            print('Please enter a valid option\n')
            selectByID(str(transactionid))
    except ValueError:
        print("Please add valid options. Whole numbers are only allowed. Add the options as per the given instruction\n")


# In[13]:


#The Function is to perform the action by user id
from user_statistics_module import *#To import the statistics function for the interface
from load_dataset_module import returndictionary#To import the load_data_set functions for the interface
def selectByUser(userId):
    try:
        chooseOption= int(input('What do yo like to do?\n1. Find the minumum and maximum transaction amount\n2. Find the centroid\n3. Find the distance of a transaction from centroid\n4. Find the standard deviation\n5. Find the variance \n6. List of Fraudulent \n7. Go Back to Previous menu\n8. Exit \n'))
        if chooseOption == 1:
            minimum, maximum = maximumMinimumTransaction(userId)#Minimum and maximum  of transactions
            print('The minimum amount of transaction of the user ',userId, 'is', minimum)
            print('The maximum amount of transaction of the user',userId, 'is', maximum)
            selectByUser(userId)#Go to previous options
        elif chooseOption == 2:
            centroidResult = getCentroid(userId)#Find the centroid of the transactions of the user
            print('The centroid of the user based on the transaction location is ',centroidResult)
            selectByUser(userId)#Go to previous options
        elif chooseOption == 3:
            transactionid=str(input('Please enter the transaction id\n'))
            checkingTransactionId = dataWithTransactionId(transactionid)
            if checkingTransactionId == []:
                print("Wrong transaction id entered\n")
                selectByUser(userId)#Go to previous options
            else:
                if verifyTransactionOfSameUser(userId,transactionid)==True:
                    distanceFromCentroid = distanceTransactionFromCentroid(userId,transactionid)#Find the distance from centroid
                    print('The distace of a transaction from centroid is ',distanceFromCentroid)
                    selectByUser(userId)#Go to previous options
                else:
                    print("Wrong transaction id entered\n")
                    selectByUser(userId)#Go to previous options
        elif chooseOption == 4:
            standardDeviation = getStandardDeviation(userId)#Find the standard deviation of the user's transactions
            print('The standard deviation of the transactions of the user is  ',standardDeviation)
            selectByUser(userId)#Go to previous options
        elif chooseOption == 5:
            variance = getVariance(userId)#Find the variance of the user's transactions
            print('The variance of the transactions of the user is ',variance)
            selectByUser(userId)#Go to previous options        
        elif chooseOption == 6:
            fraudListStatus = listFraudTransaction(userId)#Show the fraudulent transactions of a specific user
            print('The fraudulent transactions of the specific user is; ')
            for p in fraudListStatus: print (p)
            selectByUser(userId)#Go to previous options
        elif chooseOption == 7:
            goBackToMainMenu()#Go to previous options
        elif chooseOption == 8:
            exitFn()# To exit the system
        else:
            print('Please choose a correct option.')
            selectByUser(userId)#Go to previous options
                
    except ValueError:
        print("Please add valid options. Whole numbers are only allowed. Add the options as per the given instruction")
        selectByUser(userId)#Go to previous options


# In[14]:


from user_statistics_module import *#To import the statistics function for the interface
from load_dataset_module import *#To import the load_dataset function for the interface
#The Function is to show main options to the user
def main():
    userOption = str(input('Please choose an option 1 to 3\n1. Search by Transaction\n2. Search by User\n3. Exit\n'))
    if userOption ==str(1) :
        transactionid=str(input('Please enter the transaction id\n'))
        checkingTransactionId = dataWithTransactionId(transactionid,None)
        if checkingTransactionId == []:
            print("Please check the transaction id entered")
            main()
        else:
            selectByID(str(transactionid))
    elif userOption ==str(2) :
        userId=str(input('Please enter the user id\n'))
        checkingUserId = returndictionary(str(userId))
        if checkingUserId == []:
            print("Please check the user id entered")
            main()
        else:
            print('User id found!!')
            selectByUser(userId)
            
    elif userOption ==str(3) :  
        exitFn()
    else:
        print("Please choose a correct option")
        main()

