from typing import List

from pydantic import BaseModel
import numpy as np

class DataPoint(BaseModel):
    '''
    Single datapoint
    '''
    datum: np.array

class Data(BaseModel):
    '''
    List of datapoints
    '''
    data: List[DataPoint]
