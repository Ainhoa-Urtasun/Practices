import matplotlib.pyplot as plt
import numpy
fig = plt.figure(figsize=(10,7),dpi=100)
plt.plot(['December 2023','February 2024'],[45,87],color='red',label='Trainees')
plt.plot(['December 2023','February 2024'],[75,90],color='blue',label='Control')
plt.plot(['December 2023','February 2024'],[45,45+90-75],color='blue',ls='-.',label='Counterfactual')
plt.title('Training Evaluation',fontsize=16)
plt.xlabel('Time (training takes place\nduring January 2024)',fontsize=14)
plt.ylabel('Labor productivity',fontsize=14)
plt.text(0.5,50,'Training takes place during January 2024')
ticks = numpy.arange(40,101)  # 100 ticks
labels = ['' if i % 5 != 0 else str(i) for i in ticks]
plt.yticks(ticks,labels,fontsize=12)
plt.xticks(fontsize=14)
plt.grid()
plt.box(False)
plt.legend(fontsize=14)
plt.show()
