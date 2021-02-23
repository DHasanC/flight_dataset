# Python Notebook - Clone of Python Tutorial - Lessons 7 & 8

data = datasets[0]

import pandas as pd
import numpy as np

data = data.fillna(np.nan)

data.head()

data['delayed'] = data['arr_delay'].apply(lambda x: x > 0) 



