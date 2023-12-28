import matplotlib.pyplot as plt
import numpy
fig = plt.figure(figsize=(10,10),dpi=100)
plt.plot(['Before the training','After the training'],[45,87],color='red',label='Trainees')
plt.plot(['Before the training','After the training'],[75,90],color='blue',label='Control')
plt.plot(['Before the training','After the training'],[45,45+90-75],color='blue',ls='-.',label='Counterfactual')
plt.title('Training Evaluation')
plt.xlabel('Time')
plt.ylabel('Labor productivity')
plt.grid()

ticks = numpy.arange(1,101)  # 100 ticks
labels = ['' if i % 5 != 0 else str(i) for i in ticks]
plt.yticks(ticks,labels,fontsize=12)

plt.grid(axis='y')

plt.box(False)

plt.legend()
plt.show()
