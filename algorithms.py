import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score , precision_score , recall_score
from sklearn.feature_selection import RFE

dataset=None

num_feature=None


#method to be called in each algorithm to get the reduced X and y.
#the other way to do this is putting SVR("linear") as the estimator in the method and call the rfe method in the select_algorithm method.
def rfe(X, y, estimator ,num_feature):
  # Feature Extraction with RFE
  selector = RFE(estimator = estimator, n_features_to_select= num_feature)
  X = selector.fit_transform(X, y)
  return X, y


    
  

def SVM(kernel, test_size):
  X = dataset.iloc[:, :-1].values
  y = dataset.iloc[:, -1].values

  #estimator = SVR(kernel="linear") linear becuase rbf does't have coef_ nor feature_importances_
  X, y = rfe(X,y, SVC(kernel = "linear"), num_feature)

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)

  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)

  clf = SVC(kernel = kernel)
  clf = clf.fit(X_train, y_train)

  y_pred = clf.predict(X_test)

  global conf_matrix, accuracy, precision, recall, f1_score

  conf_matrix = confusion_matrix(y_test, y_pred)
  accuracy= accuracy_score(y_test, y_pred)
  precision = precision_score(y_test, y_pred)
  recall = recall_score(y_test, y_pred)
  f1_score = 2 * (precision * recall) / (precision + recall)




def dession_tree(max_depth ,test_size):

  #I generated this code using copilot, haven't tested it yet
  #الكود بتاع الجزء ده تامر باعته نبقي نستخدمه هنا

  X = dataset.iloc[:, :-1].values
  y = dataset.iloc[:, -1].values

  #need to test if the estimator has coef_ or feature_importances_
  X, y = rfe(X,y, DecisionTreeClassifier(max_depth=max_depth), num_feature)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)

  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)

  clf = DecisionTreeClassifier(max_depth=max_depth)
  clf = clf.fit(X_train, y_train)

  y_pred = clf.predict(X_test)

  global conf_matrix, accuracy, precision, recall, f1_score

  conf_matrix = confusion_matrix(y_test, y_pred)
  accuracy= accuracy_score(y_test, y_pred)
  precision = precision_score(y_test, y_pred)
  recall = recall_score(y_test, y_pred)
  f1_score = 2 * (precision * recall) / (precision + recall)
  




def KNN(test_size):
  
  #I generated this code using copilot, haven't tested it yet
  #الكود للجزء ده مش مبعوت فممكن نستخدم ده وخلاص
  #كل ال الباراميترز ليهم ديفولت فمش عارف نباصي انهي

  X = dataset.iloc[:, :-1].values
  y = dataset.iloc[:, -1].values


  #need to test if the estimator has coef_ or feature_importances_
  X, y = rfe(X,y, KNeighborsClassifier(), num_feature)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)

  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)

  clf = KNeighborsClassifier()
  clf = clf.fit(X_train, y_train)

  y_pred = clf.predict(X_test)

  global conf_matrix, accuracy, precision, recall, f1_score

  conf_matrix = confusion_matrix(y_test, y_pred)
  accuracy= accuracy_score(y_test, y_pred)
  precision = precision_score(y_test, y_pred)
  recall = recall_score(y_test, y_pred)
  f1_score = 2 * (precision * recall) / (precision + recall)