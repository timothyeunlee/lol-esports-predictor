from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

# drop nan rows 
# alternative is to replace with 0 float
# for now we can drop nan rows 
def remove_nan(df):
    # is_nan = team_stats.isnull()
    # row_has_nan = is_nan.any(axis=1)
    # rows_with_nan = team_stats[row_has_nan]
    # print(rows_with_nan)
    team_stats = df.dropna()
    return team_stats 

"""
    1. Split the data for training and testing using the sklearn.model_selection (train_test_split) module 
    2. Use the 'SVC' model to train the model 
        - 'fit' is used to train the data 
    3. Predict 
    4. Display Accuracy 
        - use the metric modules
"""
def svm(): 
    drop_cols = ['result', 'Unnamed: 0']
    df = pd.read_csv('../data/teams_ml_data/combined_team_stats.csv')
    team_stats = remove_nan(df)

    X = team_stats.drop(drop_cols, axis = 1) 
    y = team_stats['result']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    svc_classifier = SVC(kernel='linear')
    svc_classifier.fit(X_train, y_train)

    y_pred = svc_classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred)) 
    print(classification_report(y_test, y_pred))



def main(): 
    svm()

if __name__ == "__main__": 
    main() 

"""
FIRST RUN THROUGH
[[487  12]
 [ 15 478]]
              precision    recall  f1-score   support

           0       0.97      0.98      0.97       499
           1       0.98      0.97      0.97       493

    accuracy                           0.97       992
   macro avg       0.97      0.97      0.97       992
weighted avg       0.97      0.97      0.97       992   
"""