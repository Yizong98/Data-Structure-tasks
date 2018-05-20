
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
def Month_num_converter(Month):
    """ Returns numerical value given a full name Month
    >>> Month_num_converter('January')
    1
    >>> Month_num_converter('July')
    7
    >>> Month_num_converter('Jan')
    'Month input is not valid'
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
def date_converter(df):
    """ Convert date in the table to the day-month-year form.
    >>> data_1.apply(date_converter,axis=1)
    0    02-Jun-13
    1    23-Jul-13
    2    30-Sep-17
    3    12-Dec-17
    dtype: object
    >>> data_2.apply(date_converter,axis=1)
    0    02-Jan-15
    1    21-Mar-16
    2    30-May-17
    3    15-Jul-18
    dtype: object
    >>> date_converter(1)
    'invalid input'
    """
    try:
        return df['Date'].strftime("%d-%b-%y")
    except:
        return "invalid input"
def data_formatter(df):
    ''' 
    Format the Month, Year, Day in the table to datatime form.
    >>> data_2 = pd.read_csv('data2.csv')
    >>> data_2['Month'] = data_2['Month'].apply(Month_num_converter)
    >>> data_2.apply(data_formatter,axis=1)
    0   2015-01-02
    1   2016-03-21
    2   2017-05-30
    3   2018-07-15
    dtype: datetime64[ns]
    >>> data_1 = pd.read_csv('data1.csv')
    >>> data_1.apply(data_formatter,axis=1)
    0   2013-06-02
    1   2013-07-23
    2   2017-09-30
    3   2017-12-12
    dtype: datetime64[ns]
    >>> date_converter(1)
    'invalid input'
    '''
    try:
        return datetime(df['Year'],df['Month'],df['Day'])
    except:
        return "invalid input"
data_1 = pd.read_csv('data1.csv')
data_2 = pd.read_csv('data2.csv')
data_2['Month'] = data_2['Month'].apply(Month_num_converter)
data_2['Date'] = data_2.apply(data_formatter,axis=1)
data_1['Date']= data_1.apply(data_formatter,axis=1)
combine_csv = data_1[['Date','Tweet']].merge(data_2[['Date','Tweet']], on=['Tweet','Date'],how='outer')
combine_csv['Date']=pd.to_datetime(combine_csv.Date)
combine_csv = combine_csv.sort_values('Date',ascending=False)
combine_csv['Date']=combine_csv.apply(date_converter,axis=1)
combine_csv.to_csv('combined.csv', index=False)


