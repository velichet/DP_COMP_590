import numpy as np
import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from io import StringIO
import json

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

def label_data(col):
    """ 
    Label encoder for target column values
    
    1) col : Target/user specified column

    """
    
    LE = LabelEncoder()    
    interger_label = LE.fit_transform(col)
    
    return interger_label


        
def convert_epsilon(epsilon):
    """ 
    Function to convert epsilon to prob p and q
    
    1) epsilon : epsilon
    
    """
    
    const = math.pow(math.e, float(epsilon)/2)
    p = const / (const + 1)
    q = 1-p
    
    return p ,q 
    


def encode(input_data,d):
    
    """ 
    Function to encode data into the vector
    
    1) input_data : raw data from the user
    
    2) d : domain size of the column mentioned by user
    
    """
    
    ue_data = np.zeros(d)
    
    if input_data != None:
        ue_data[input_data] = 1
        
    return ue_data



            
def __perturb(ue_data, p ,q, d):    
    
    """ 
    Function to peturb the vector
    
    1) ue_data : encoded data 
    
    2) d : domain size of the column mentioned by user 
    
    3) p : probability p used to flip the bits in the array 
    
    4) q : probability q used to flip the bits in the array 
    
    """
    
    peturb_vec = np.zeros(d)

    for index in range(d):
        
        if ue_data[index] == 0:
            
            rnd = np.random.random()
            if rnd <= q:
                peturb_vec[index] = 1
        else:
            
            rnd = np.random.random()
            if rnd <= p:
                peturb_vec[index] = 1
                
    return peturb_vec

      

def local_dp(epsilon, col, data):
    
    """ 
    Function to peturb the vector
    
    1) epsilon : epsilon value 
    
    2) col : Target/user specified column
    
    3) data : The data should be a Dataframe  
    
    """

    # Convert data to a dataframe
    data = csv_to_df(data)
    
    domain = np.unique(data[col])
    size = domain.size
    
    p , q = convert_epsilon(epsilon)
    peturb_vect = []
    
    for instance in label_data(data[col]):
        
     ue_data_vec = encode(instance,size)
     peturb_vec =  __perturb(ue_data_vec,p,q,size)
        
     peturb_vect.append(peturb_vec)
   

    estimate_values =  np.array((sum(peturb_vect) - q * len(peturb_vect)) / (p-q)).clip(0)
     
    results = {}
    i = 0
    for d in domain:
        results[d] = int(estimate_values[i])
        i+=1
    
    return json.dumps(results)

    