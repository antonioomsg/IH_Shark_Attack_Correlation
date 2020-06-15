#These are my functions:

def drop_null(table,subset):
    table.dropna(subset=[f"{subset}"],inplace=True)