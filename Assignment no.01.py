# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:42:34 2021

@author: Akash
"""
#-------------Logistic Regression------------------------------
#Import Libraries
import pandas as pd
import seaborn as sns

#Import data 
HR_data = pd.read_csv("HR_Data.csv")
HR_data.head(5)
HR_data.tail(5)

print("No. of left in original dataset:" +str(len(HR_data.index)))

#Analyzing Data
sns.countplot(x="left",data=HR_data)

sns.countplot(x="left",hue="exp_in_company",data=HR_data)

sns.countplot(x="left",hue="number_project",data=HR_data)

sns.countplot(x="left",hue="promotion_last_5years",data=HR_data)

sns.countplot(x="left",hue="salary",data=HR_data)

sns.countplot(x="left",hue="role",data=HR_data)

#CHECKING DATA TYPE OF A VARIABLE AND CONVERTING IT INTO ANOTHER TYPE-----
HR_data.info()


#Identifying/Finding missing values if any----
HR_data.isnull()
HR_data.isnull().sum()



#creating dummies of object values (catogirical values)

pd.get_dummies(HR_data["role"])
role_Dummy = pd.get_dummies(HR_data["role"],drop_first=True)
role_Dummy.head(5)

pd.get_dummies(HR_data["salary"])
salary_Dummy = pd.get_dummies(HR_data["salary"],drop_first=True)
salary_Dummy.head(5)

#Now, lets concatenate these dummy var columns in our dataset.
HR_data = pd.concat([HR_data,role_Dummy,salary_Dummy],axis=1)
HR_data.head(5)

#dropping the columns whose dummy var have been created
HR_data.drop(["role","salary",],axis=1,inplace=True)
HR_data.head(5)

#Splitting the dataset into Train & Test dataset
x=HR_data.drop("left",axis=1)
y=HR_data["left"]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,predictions)

#Accuracy = (2656+333)/(2656+225+536+333) = 79%


#Calculating the coefficients:
print(logmodel.coef_)

#Calculating the intercept:
print(logmodel.intercept_)

#----To Improve the accuracy of the model, lets go with Backward ELimination Method &
# rebuild the logisitc model again with few independent variables--------
HR_data_1 = HR_data
HR_data_1.head(5)

#--------------------------Backward Elimination--------------------------------
#Backward elimination is a feature selection technique while building a machine learning model. It is used
#to remove those features that do not have significant effect on dependent variable or prediction of output.

#Step: 1- Preation of Backward Elimination:
#Importing the library:
import statsmodels.api as sm

#Adding a column in matrix of features:
x1=HR_data_1.drop("left",axis=1)
y1=HR_data_1["left"]
import numpy as nm
x1 = nm.append(arr = nm.ones((14999,1)).astype(int), values=x1, axis=1)

#Applying backward elimination process now
#Firstly we will create a new feature vector x_opt, which will only contain a set of 
#independent features that are significantly affecting the dependent variable.
x_opt= x1[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]

#for fitting the model, we will create a regressor_OLS object of new class OLS of statsmodels library. 
#Then we will fit it by using the fit() method.
regressor_OLS=sm.OLS(endog = y1, exog=x_opt).fit()

#We will use summary() method to get the summary table of all the variables.
regressor_OLS.summary()

#In the above summary table, we can clearly see the p-values of all the variables. 
#And remove the ind var with p-value greater than 0.05
x_opt= x1[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt= x1[:, [0,1,2,3,4,5,6,7,8,9,10,11,14,15,16,17,18]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt= x1[:, [0,1,2,3,4,5,6,7,8,10,11,14,15,16,17,18]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()


x_opt= x1[:, [0,1,2,3,4,5,6,7,8,10,11,15,16,17,18]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()


x_opt= x1[:, [0,1,2,3,4,5,6,7,8,10,11,16,17,18]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt= x1[:, [0,1,2,3,4,5,6,7,8,10,11,17,18]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt= x1[:, [0,1,2,3,4,5,6,7,8,11,17,18]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split
x_BE_train, x_BE_test, y_BE_train, y_BE_test= train_test_split(x_opt, y1, test_size= 0.25, random_state=0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(x_BE_train, y_BE_train)

predictions = logmodel.predict(x_BE_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_BE_test,predictions)

#Accuracy = (2649+367)/(2649+232+502+367) = 80%

#Calculating the coefficients:
print(logmodel.coef_)

#Calculating the intercept:
print(logmodel.intercept_)

#So, ur final Predicitve Modelling Equation becomes:
 #LEFT =
#   [ Exp (- 0.37 - 0.35* Satiscn Level - 4.31 * Last Evalntn + 0.28 * No.Of Project
#     - 0.34 * Avg Month Hrs + 0.005 * Exp In Compn + 0.28 * Work Accndt - 1.55 
#    * Promotn - 0.73 * R&D - 0.60 * Hr + 1.57 * Technical + 1.008 * Low ) ]
#      / [Exp (- 0.37 - 0.35* Satiscn Level - 4.31 * Last Evalntn + 0.28 * No.Of Project
 #      - 0.34 * Avg Month Hrs + 0.005 * Exp In Compn + 0.28 * Work Accndt - 1.55 
 #      *Promotn - 0.73 * R&D - 0.60 * Hr + 1.57 * Technical + 1.008 * Low )] + 1
