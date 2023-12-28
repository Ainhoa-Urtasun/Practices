import matplotlib.pyplot as plt
import numpy
fig = plt.figure(figsize=(10,5),dpi=100)
plt.plot(['December 2023','February 2024'],[0,25],marker='o',color='red',label='Trainees')
plt.plot(['December 2023','February 2024'],[15,30],marker='o',color='blue',label='Control')
plt.plot(['December 2023','February 2024'],[0,0+30-15],marker='o',color='green',ls='-.',label='Counterfactual')
plt.xticks(fontsize=14)
ticks = numpy.arange(0,32)  # 20 ticks
labels = ['' if i % 2 != 0 else str(i) for i in ticks]
plt.yticks(ticks,labels,fontsize=12)
plt.title('Labor Productivity (Q/L)',fontsize=16)
plt.legend(fontsize=14)
plt.grid()
plt.box(False)
plt.show()
