import pandas as pd
data = {'job_{1(t)}':[53,12,3,8],
        'job 2(t)':[14,46,6,13],
        'job 3(t)':[7,18,35,9],
        'Out(t)':[2,5,5,0]}
Table = pd.DataFrame(data, index=['Job1(t-1)','Job2(t-2)','Job3(t-1)','Out(t-1)'])
Table['Sum'] = Table.sum(axis=1)
Table.loc['Sum'] = Table.sum(axis=0)

