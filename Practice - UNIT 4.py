import matplotlib.pyplot as plt
import numpy

# Generate sample data
# Generate sample data
L = [0,1,2,3,4,5,6,7,8,9,10]
QA = [0,11,27,47.5,66,(5/4)*66,98,111,122,131,138]
QB = [0,10,30,60,100,(5/4)*100,135,140,144,147,149]
MOLA = numpy.diff(QA).tolist()
MOLA = [numpy.nan] + MOLA
VMOLA = [10*x for x in MOLA]
MOLB = numpy.diff(QB).tolist()
MOLB = [numpy.nan] + MOLB
VMOLB = [10*x for x in MOLB]
w = [50 for _ in range(11)]

# Create subplots
fig, axs = plt.subplots(1,1,figsize=(10,5))

# Scatter plot
axs[0].plot(L,VMOLA,'o-',color='blue',label='Firm A')
axs[0].plot(L,VMOLB,'o-',color='orange',label='Firm B')
axs[0].plot(L,w,'o-',color='green',label='Wage')
axs[0].legend()
axs[0].set_title('Value of marginal output of labor ($VMOL$)')
axs[0].set_xlabel('Number of employees')
axs[0].grid(True)  # Show grid

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()
