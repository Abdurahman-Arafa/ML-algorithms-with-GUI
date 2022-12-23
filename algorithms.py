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
import tkinter 

#global variables
dataset = None
num_feature = None


#method to be called in each algorithm to get the reduced X and y.
def rfe(estimator):
  """This function takes the estimator and returns the reduced X and y from the dataset"""
  X = dataset.iloc[:, :-1].values
  y = dataset.iloc[:, -1].values
  selector = RFE(estimator = estimator, n_features_to_select= num_feature)
  X = selector.fit_transform(X, y)
  return X, y




def SVM(kernel, test_size):
  global model, X_test, y_test
  #estimator = SVR(kernel="linear") linear becuase rbf does't support coef_ nor feature_importances_
  X, y = rfe(SVC(kernel = "linear"))

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)

  clf = SVC(kernel = kernel)
  model = clf.fit(X_train, y_train)

  tkinter.messagebox.showinfo("Successful","Model Trained Successfully")
  return


def dession_tree(max_depth ,test_size):
  global model, X_test, y_test

  X, y = rfe(DecisionTreeClassifier(max_depth=max_depth))
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)

  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)

  clf = DecisionTreeClassifier(max_depth=max_depth)
  model = clf.fit(X_train, y_train)

  tkinter.messagebox.showinfo("Successful","Model Trained Successfully")
  return




def KNN(n_neighbors, test_size):
  
  global model, X_test, y_test
  #couldn't use rfe with KNN because it doesn't support coef_ nor feature_importances_, 
  #we can either use LogisticRegression or DecisionTreeClassifier (already imported)
  X, y = rfe(DecisionTreeClassifier(max_depth=2))
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)

  clf = KNeighborsClassifier(n_neighbors)
  model = clf.fit(X_train, y_train)

  tkinter.messagebox.showinfo("Successful","Model Trained Successfully")
  return

def test():
  global conf_matrix, accuracy, precision, recall, f1_score

  y_pred = model.predict(X_test)

  conf_matrix = confusion_matrix(y_test, y_pred)
  accuracy= accuracy_score(y_test, y_pred)
  precision = precision_score(y_test, y_pred)
  recall = recall_score(y_test, y_pred)
  f1_score = 2 * (precision * recall) / (precision + recall)

  tkinter.messagebox.showinfo("Successful","Model Tested Successfully")
  return