import pandas as pd
from io import StringIO

# Format CSV
def csv_format(data: str):
    """
    Input (CSV str):
        '''
        age,height,weight
        25,65,132
        ...
        '''
    Output (dict):
        {
            'age': [25, ...],
            'height': [65, ...],
            'weight': [132, ...]
        }
    """

    # Make CSV all lower case
    data = data.lower()   

    # Convert CSV string to String IO
    csv_string = StringIO(data)

    # Read into dataframe
    df = pd.read_csv(csv_string, sep=",")

    # Return dict with lists
    return df.to_dict('list')

def csv_to_df(data: str):
    """
    Input CSV str
    Output pandas dataframe
    """

    # Make CSV all lower case
    data = data.lower()   

    # Convert CSV string to String IO
    csv_string = StringIO(data)

    # Read into dataframe
    df = pd.read_csv(csv_string, sep=",")

    # Return dataframe
    return df