# Machine Learning App

This app allows users to train and test machine learning models on a variety of datasets. The app provides a user-friendly interface for selecting an algorithm, loading a dataset, and configuring the training parameters. The app then trains the model and displays the results of the training and testing.

## Requirements

To use this app, you will need the following:
* `Python 3.6` or higher
* The `customtkinter` library
* The `pandas` library
* The `numpy` library
* The `scikit-learn` library

run `pip install -r requirements.txt` to install the required libraries.

## Usage

To use this app, navigate to the project directory then run the following command:
`python main.py`

### The app will open a window with the following options:

- ## Select Algorithm:
This option allows you to select the machine learning algorithm you want to use. The available algorithms are:

    * SVM
    * Decision Tree
    * KNN
    * Linear Regression

- ## Load Dataset:
This option allows you to load a dataset from a file. The app supports CSV files.

- ## Enter Feature Number:
TThis option allows you to perform feature selection on the dataset using the RFE (Recursive Feature Elmiination) select the top n_features for the selected algorithm.

- Train & Test window:
allows the user to specify the testing size from the dataset and allowing for the training and testing of the model after.

- ## Results window:
This window displays the results of the training and testing of the model. It displays the following:

    * The Accuracy of the model
    * The Precision of the model
    * The Recall of the model
    * The F1 score of the model
    * The option to save the model if the user is satisfied with the results