# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 13:45:33 2021

@author: Akash
"""

import pandas as pd

# Importing the dataset
dataset = pd.read_csv('T6_Luxury_Cars.csv')

#Identifying/Finding missing values if any----
dataset.isnull()
dataset.isnull().sum()

dataset.info()

#Method-1 (Handling Categorical Variables)

pd.get_dummies(dataset["DriveTrain"])
pd.get_dummies(dataset["DriveTrain"],drop_first=True)
DriveTrain_Dummy = pd.get_dummies(dataset["DriveTrain"],drop_first=True)
DriveTrain_Dummy.head(5)


#Now, lets concatenate these dummy var columns in our dataset.
dataset = pd.concat([dataset,DriveTrain_Dummy,],axis=1)
dataset.head(5)
#dropping the columns whose dummy var have been created
dataset.drop(["Make","Model","Type","Origin","DriveTrain",],axis=1,inplace=True)
dataset.head(5)
#------------------------------------------------------------------------------

#Obtaining DV & IV from the dataset
X = dataset.iloc[:,[0,1,2,4,5,6,7,8]].values
y = dataset.iloc[:,3].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Accuracy of the model

#Calculating the r squared value:
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)

#Coefficient
regressor.coef_

# Intercept
regressor.intercept_


#The above score tells that our model is 62.67% accurate with the test dataset.

#Regression eqn:- Mileage = 35.98 + (-1.43*enginesize) + (0.21*Cylinder) + (-0.0064*HP)
   #              + (-0.0041*weight) + ( 0.037*wheelbase) + (0.026*Length) + (2.28*Front) + (0.87*Rear)
         
         
         
#--------------------------Backward Elimination--------------------------------
#Backward elimination is a feature selection technique while building a machine learning model. It is used
#to remove those features that do not have significant effect on dependent variable or prediction of output.

#Step: 1- Preparation of Backward Elimination:

#Importing the library:
import statsmodels.api as sm

#Adding a column in matrix of features:
import numpy as nm
X = nm.append(arr = nm.ones((426,1)).astype(int), values=X, axis=1)

#Applying backward elimination process now
#Firstly we will create a new feature vector x_opt, which will only contain a set of 
#independent features that are significantly affecting the dependent variable.
x_opt=X[:, [ 0,1,2,3,4,5,6,7,8]]

#for fitting the model, we will create a regressor_OLS object of new class OLS of 
#statsmodels library. Then we will fit it by using the fit() method.
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()

#We will use summary() method to get the summary table of all the variables.
regressor_OLS.summary()

#In the above summary table, we can clearly see the p-values of all the variables. 
#Here x1, x2 are dummy variables, x3 is R&D spend, x4 is Administration spend, and x5 is Marketing spend.

#Now since x5 has highest p-value greater than 0.05, hence, will remove the x1 variable
#(dummy variable) from the table and will refit the model.
x_opt=X[:, [ 0,1,2,3,4,5,7,8]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()


x_opt=X[:, [ 0,1,2,3,4,5,7,8]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()



x_opt=X[:, [ 0,1,3,4,5,7,8]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()


x_opt=X[:, [ 0,1,3,4,5,7]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt=X[:, [ 0,3,4,5,7]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()


#Hence,only  DriveTrain,horsepower,weight,wheelbase independent variable is a significant variable for the prediction. 
#So we can now predict efficiently using this variable.

#----------Building Multiple Regression model by only using DriveTrain,horsepower,weight,wheelbase:-----------------
#importing datasets  
data_set= pd.read_csv('T6_Luxury_Cars.csv') 


pd.get_dummies(data_set["DriveTrain"])
pd.get_dummies(data_set["DriveTrain"],drop_first=True)
DriveTrain_Dummy = pd.get_dummies(data_set["DriveTrain"],drop_first=True)
DriveTrain_Dummy.head(5)


data_set = pd.concat([data_set,DriveTrain_Dummy,],axis=1)
data_set.head(5)
#dropping the columns whose dummy var have been created
data_set.drop(["Make","Model","Type","Origin","DriveTrain", "Engine Size (L)", "Rear","Cylinders","Length (IN)"],axis=1,inplace=True)



#Extracting Independent and dependent Variable  
x_BE= data_set.iloc[:,[0,2,3,4]].values
y_BE= data_set.iloc[:,1].values 

# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split
x_BE_train, x_BE_test, y_BE_train, y_BE_test= train_test_split(x_BE, y_BE, test_size= 0.25, random_state=0)

#Fitting the MLR model to the training set:  
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_BE_train, y_BE_train)

#Predicting the Test set result;
y_pred= regressor.predict(x_BE_test)

#Cheking the score  
#Calculating the r squared value:
from sklearn.metrics import r2_score
r2_score(y_BE_test,y_pred)
#The above score tells that our model is now more accurate with the test dataset with
#accuracy equal to 65.82%

#Calculating the coefficients:
print(regressor.coef_)

#Calculating the intercept:
print(regressor.intercept_)


#Regression Eq'n: Mileage= 39.99 + (-0.013*HP -0.005*weight + 0.060*wheelbase + 1.95*Rear)
