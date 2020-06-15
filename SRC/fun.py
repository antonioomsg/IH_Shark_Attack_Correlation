#These are my functions:

def drop_null(table,subset):
    table.dropna(subset=[f"{subset}"],inplace=True)

def standardize_data(df,column,old,new):
    Valid_colums[column] = Valid_colums[column].replace(old, new)

def c_data(column):
     print(Valid_colums[f"{column}"].value_counts())