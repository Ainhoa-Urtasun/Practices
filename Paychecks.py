import numpy
import matplotlib.pyplot as plt

def Paychecks(Pay):

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
  plt.legend(ncols=2,loc='upper center')
  plt.show()
