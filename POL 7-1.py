import matplotlib.pyplot as plt
import numpy
fig = plt.figure(figsize=(10,5),dpi=100)
period = ['Pre-Training','Post-Training']
plt.plot(period,[0,7],marker='o',color='red',label='Trainees')
plt.plot(period,[5,10],marker='o',color='blue',label='Control')
plt.plot([period,[0,0+10-5],marker='o',color='green',ls='-.',label='Counterfactual')
plt.xticks(fontsize=14)
ticks = numpy.arange(0,11)  # 20 ticks
labels = ['' if i % 1 != 0 else str(i) for i in ticks]
plt.yticks(ticks,labels,fontsize=12)
plt.title('Labor Productivity (Q/L)',fontsize=16)
plt.legend(fontsize=14)
plt.grid()
plt.box(False)
plt.show()
