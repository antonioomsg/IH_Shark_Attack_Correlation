#These are my functions:

def drop_null(table,subset):
    table.dropna(subset=[f"{subset}"],inplace=True)

def standardize_data(df,column,old,new):
    df[column] = df[column].replace(old, new)

def c_data(column):
     print(df[f"{column}"].value_counts())