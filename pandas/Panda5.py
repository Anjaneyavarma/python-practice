#Panda5.py
# How to get the items of series A not present in series B
import numpy as np
import pandas as pd
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution
print(ser1[~ser1.isin(ser2)])
