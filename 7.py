import pandas as pd
data = {'Job1(t)': [1, 2, 3],
        'Job2(t)': [4, 5, 6],
        'Job3(t)': [7, 8, 9]}
df = pd.DataFrame(data, index=['Job1(t-1)','Job2(t-2)','Job3(t-1)'])
