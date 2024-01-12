import pandas as pd
data = {'Job$_{1(t)}$': [1, 2, 3],
        'Column2': [4, 5, 6],
        'Column3': [7, 8, 9]}
df = pd.DataFrame(data, index=['Row1', 'Row2', 'Row3'])

# Display the DataFrame
print(df)
