import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def load(name):
    return pd.read_csv(name)

def show_df(data):
    print(data.head())
    print(data.info())

def transform(data):
    categorical_columns = data.select_dtypes(include=['object']).columns
    data=pd.get_dummies(data, columns=categorical_columns, dtype=float)
    print("Data convert object to float")
    export_data(data)
    return data

def export_data(data):
    data.to_excel("data/data_process.xlsx",sheet_name='XG_data')  