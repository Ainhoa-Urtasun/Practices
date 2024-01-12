import pandas as pd
data = {'Job1(t)':[53,12,3,8,76],
        'Job2(t)':[14,46,6,13,79],
        'Job3(t)':[7,18,35,9,69],
        'Out(t)':[2,5,5,0],
        'Sum':[76,81,49,30,0]}
table = pd.DataFrame(data, index=['Job1(t-1)','Job2(t-2)','Job3(t-1)','Out(t-1)','Sum'])
