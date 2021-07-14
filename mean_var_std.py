import numpy as np

def calculate(list):
    calculations = {}
    # Raise ValueError if the length of the list is not equal to 9
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:  
        # flattened indicates the 1-D array form of the inputed list to utilize the full mathematical features of numpy
        flattened = np.array(list)
        
        # matrix indicates the 3 x 3 matrix form (2-D array) of the flattened array
        matrix = flattened.reshape(3,3)
        
        calculations['mean'] = [matrix.mean(axis=0).tolist(),matrix.mean(axis=1).tolist(),flattened.mean()]
        calculations['variance'] = [matrix.var(axis=0).tolist(),matrix.var(axis=1).tolist(),flattened.var()]
        calculations['standard deviation'] = [matrix.std(axis=0).tolist(),matrix.std(axis=1).tolist(),flattened.std()]
        calculations['max'] = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(),flattened.max()]
        calculations['min'] = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(),flattened.min()]
        calculations['sum'] = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(),flattened.sum()]

    return calculations
