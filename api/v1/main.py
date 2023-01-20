import pandas as pd
import logging
import os
import pathlib
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
from flaml import AutoML
from sklearn.metrics import classification_report

def test_func(path_string):

    try:
        #!pip install openpyxl
        train = pd.read_excel(path_string)
        #train.head()
        print("train.head():", train.head())
        print("")
        print("train.info():", train.info())
        print("")

        train.drop_duplicates(keep=False, inplace=True)
        print("train.shape:", train.shape)
        print("")

        print("train.Class.value_counts():", train.Class.value_counts())

        [train, test] = train_test_split( train, test_size=0.2, random_state=42,shuffle=True, stratify=train.Class)

        print("train.shape:", train.shape)
        print("")
        print("test.shape:", test.shape)
        print("")

        print("train.isnull().sum().sort_values(ascending=False):", train.isnull().sum().sort_values(ascending=False))
        print("")

        pd.options.display.max_columns = None
        print("train[train.isna().any(axis=1)]:", train[train.isna().any(axis=1)])
        print("")

        print("test[test.isna().any(axis=1)]:", test[test.isna().any(axis=1)])
        print("")

        automl = AutoML()
        y = train.pop('Class')
        X = train

        [X_train, X_test, y_train, y_test] = train_test_split( X, y, test_size=0.2, random_state=42,shuffle=True, stratify=y)

        automl.fit(X_train, y_train, task="classification",metric='log_loss',time_budget=300)

        print('Best ML leaner:', automl.best_estimator)
        print('Best hyperparmeter config:', automl.best_config)
        print('Best log_loss on validation data: {0:.4g}'.format(automl.best_loss))
        print('Training duration of best run: {0:.4g} s'.format(automl.best_config_train_time))

        print("classification_report_train:", classification_report(y_train, automl.predict(X_train)))
        print("")

        print("classification_report_test:", classification_report(y_test, automl.predict(X_test)))
        print("")

        test_=test.drop('Class',axis=1)
        print("test_.head():", test_.head())
        print("")

        y_pred = automl.predict(test_)
        print("y_pred[:5]:", y_pred[:5])
        print("")

        df = pd.DataFrame(y_pred,columns=['Class'])
        print("df.head():", df.head())
        print("")

        print("print(classification_report(test.Class, df.Class)):", print(classification_report(test.Class, df.Class)))
        print("")

    except Exception as err:
        logging.error(err)
    return 