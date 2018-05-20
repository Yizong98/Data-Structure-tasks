
###########   Part 1 ################

# answers should go to hw7.txt file 


###########   Part 2  ###############

def workaround(x):
  """this function exists to let okpy accept submissions.
  >>> workaround(5)
  10
  """
  return x*2

import numpy as np
import pandas as pd
from datetime import *

#YOUR CODE GOES HERE#
data_1 = pd.read_csv('data1.csv')
data_2 = pd.read_csv('data2.csv')

def Month_num_converter(Month):
    """ Returns numerical value given a full name Month
    >>> Month_num_converter('January')
    1
    >>> Month_num_converter('July')
    7
    >>> Month_num_converter('Jan')
    Month input is not valid
    """
    try:
        return{
            'January' : 1,
            'February' : 2,
            'March' : 3,
            'April' : 4,
            'May' : 5,
            'June' : 6,
            'July' : 7,
            'August' : 8,
            'September' : 9, 
            'October' : 10,
            'November' : 11,
            'December' : 12
        }[Month] 
    except:
        return "Month input is not valid"