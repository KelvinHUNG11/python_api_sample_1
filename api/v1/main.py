import pandas as pd
import logging
import os
import pathlib
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
from flaml import AutoML
from sklearn.metrics import classification_report
import pickle

def train_model(path_string):

    try:
        #!pip install openpyxl
        train = pd.read_excel(path_string)

        ## ** Method 1 - to replace invalid input with mean value ** ##
        ##Check the number of invalid input
        print("train.isnull().sum():", train.isnull().sum())

        ##To indicate row(s) of invalid input
        print("train[train.isnull().any(axis=1)]:", train[train.isnull().any(axis=1)])

        ## Optional, to replace missing or invalid with an averaged value
        ## Assume column "ECCENTRICITY" is found invalid in the file
        ## train.ECCENTRICITY = train.ECCENTRICITY.fillna(train.ECCENTRICITY.mean())

        ## ** End of Method 1 ** ##

        ## ** Method 2 - to drop all rows with invalid input ** ##

        ##Drop invalid row(s)
        train.dropna(axis=0, how='any')

        ## ** End of Method 2 ** ##

        ##Drop duplicated row(s), optional
        train.drop_duplicates(keep=False, inplace=True)

        ##Default value, 20% dataset for validation; 80% dataset for training purpose
        [train, test] = train_test_split( train, test_size=0.2, random_state=42, shuffle=True, stratify=train.Class)

        pd.options.display.max_columns = None
        print("train[train.isna().any(axis=1)]:", train[train.isna().any(axis=1)])
        print("")

        print("test[test.isna().any(axis=1)]:", test[test.isna().any(axis=1)])
        print("")

        automl = AutoML()
        y = train.pop('Class')
        X = train

        [X_train, X_test, y_train, y_test] = train_test_split( X, y, test_size=0.2, random_state=42,shuffle=True, stratify=y)

        automl.fit(X_train, y_train, task="classification",metric='log_loss',time_budget=5)

        ##Save the best model ever trained
        with open('automl.pkl', 'wb') as f:
            pickle.dump(automl, f, pickle.HIGHEST_PROTOCOL)

        print('Best ML leaner:', automl.best_estimator)
        print('Best hyperparmeter config:', automl.best_config)
        print('Best log_loss on validation data: {0:.4g}'.format(automl.best_loss))
        print('Training duration of best run: {0:.4g} s'.format(automl.best_config_train_time))

        print("classification_report_train:", classification_report(y_train, automl.predict(X_train)))
        print("")

        with open('classification_report_train.csv', 'w') as f:
            f.write(str(classification_report(y_train, automl.predict(X_train))))

        print("classification_report_test:", classification_report(y_test, automl.predict(X_test)))
        print("")

        with open('classification_report_test.csv', 'w') as f:
            f.write(str(classification_report(y_test, automl.predict(X_test))))

        test_=test.drop('Class',axis=1)
        ##print("test_.head():", test_.head())
        print("")

        y_pred = automl.predict(test_)
        ##print("y_pred[:5]:", y_pred[:5])
        print("")

        df = pd.DataFrame(y_pred,columns=['Class'])
        ##print("df.head():", df.head())
        print("")

    except Exception as err:
        logging.error(err)
    return 

def test_model(path_string):

    try:
        #!pip install openpyxl
        test = pd.read_csv(path_string)

        ##Drop invalid row(s)
        test.dropna()

        ##To load the trained model called "automl.pkl"
        automl = pickle.load(open('automl.pkl', 'rb'))
        logging.info("Model called successfully")
        y_pred = automl.predict(test)

        ##Update predicted results to the file
        for i in range(len(y_pred)):
            # updating the column value/data
            test.loc[i, 'Class'] = y_pred[i]
  
        # writing into the file
        test.to_csv(path_string, index=False)

    except Exception as err:
        logging.error(err)
    return 

def check_uploaded_files(path_string_file_train, path_string_file_test):

    try:
        #!pip install openpyxl
        train_file = pd.read_excel(path_string_file_train)

        temp_train_column = []
        temp_test_column = []

        for col in train_file.columns:
            temp_train_column.append(col)

        test_file = pd.read_csv(path_string_file_test)

        for col in test_file.columns:
            temp_test_column.append(col)

        for col in range(len(temp_train_column) - 1):

            if (temp_train_column[col] != temp_test_column[col]):

                result = "matched"

                return result

    except Exception as err:

        logging.error(err)

    return 