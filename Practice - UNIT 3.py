import pandas as pd
data = {'job1(t)':[53,12,3,8],
        'job2(t)':[14,46,6,13],
        'job3(t)':[7,18,35,9],
        'Out(t)':[2,5,5,0]}
Table = pd.DataFrame(data, index=['job1(t-1)','job2(t-2)','job3(t-1)','Out(t-1)'])

