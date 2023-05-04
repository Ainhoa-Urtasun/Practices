import numpy
import matplotlib.pyplot as plt

Pay = {'Employee (SOC)':['Marta (SOC 11-1021)','Martin (SOC 23-1011)','Sarah (SOC 23-1011)'],
       'Pay range':[[78.95,78.95+99],[69.28,69.28+98],[69.28,69.28+98]],
       'Wage and salary':[54.29+5,46.01+5,46.01+2],
       'Paid leave':[7.51+5,6.36+5,6.36+2],
       'Supplementary pay':[0,0,0],
       'Insurance':[5.40+5,5.39+5,5.39],
       'Retirement':[3.57+5,4.98+5,4.98+1],
       'Legally required benefits':[4.98+5,4.53+5,4.53+2]}

fig = plt.figure(figsize=(8,8),dpi=100)

for i in ['Pay range']:
  market = [Pay[i][0][0],Pay[i][1][0],Pay[i][2][0]]
  plt.bar(Pay['Employee (SOC)'],market,0.4,color='white')
  plt.bar(Pay['Employee (SOC)'],[Pay[i][0][1]-market[0],Pay[i][1][1]-market[1],Pay[i][2][1]-market[2]],0.4,bottom=market,color='white',edgecolor='black',linewidth=5,ls='--')

bottom = numpy.zeros(len(Pay['Employee (SOC)']))
for i in list(Pay.keys())[2:]:
  plt.bar(Pay['Employee (SOC)'],[Pay[i][0],Pay[i][1],Pay[i][2]],0.4,bottom=bottom,label=i,alpha=0.5)
  bottom += [Pay[i][0],Pay[i][1],Pay[i][2]]

plt.xlabel('Employees',fontsize=16)
plt.title('Paychecks',fontsize=16)
plt.legend(loc='lower center')
plt.show()
