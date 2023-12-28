import matplotlib.pyplot as plt
import numpy
fig = plt.figure(figsize=(4,4),dpi=100)
plt.plot(['Before the training','After the training'],[45,87],color='red',label='Trainees')
plt.plot(['Before the training','After the training'],[175,210],color='blue',label='Control')
plt.plot(['Before the training','After the training'],[45,45+210-175],color='blue',ls='-.',label='Counterfactual')
plt.title('Labor productivity')
plt.legend()
plt.show()