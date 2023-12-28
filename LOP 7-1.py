import matplotlib.pyplot as plt
import numpy
fig = plt.figure(figsize=(10,10),dpi=100)
plt.plot(['Before the training','After the training'],[45,87],color='red',label='Trainees')
plt.plot(['Before the training','After the training'],[175,210],color='blue',label='Control')
plt.plot(['Before the training','After the training'],[45,45+210-175],color='blue',ls='-.',label='Counterfactual')
plt.title('Training Evaluation')
plt.xlabel('Time')
plt.ylabel('Labor productivity')
plt.grid()
plt.legend()
plt.show()
