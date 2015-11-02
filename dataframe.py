#Data Analysis with Python and Pandas
#Creating and Navigating a Dataframe
#Milktea Oct 27, 2015 22:46

import pandas as pd

starting = {'Col_1':[1,6,4,7],
	    'Col_2': [5,7,8,3],
	    'Col_2': [6,3,7,4]}

df = pd.DataFrame(starting)
print(df)
print(df.dtypes)
print(df['Col_1'][0])
print(df.Col_1)
