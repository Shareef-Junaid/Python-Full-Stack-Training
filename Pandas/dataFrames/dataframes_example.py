import pandas as pd
data = []
df = pd.DataFrame(data)

data = [1, 2, 3, 4, 5, 6, 7, 8]
df = pd.DataFrame(data)
print(df)

data = [['A', 1], ['B', 2], ['C', 3]]
df = pd.DataFrame(data)
print(df)


data = {'Name': ['A', 'B', 'C', 'D'],
        'Age': [10, 10, 40, 50]
        }
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)


df['num'] = [1, 2, 3, 4]
print(df)
df = pd.read_csv('artwork_data.csv')

import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
periods=10), columns=list('ABCD'))
df.plot()



