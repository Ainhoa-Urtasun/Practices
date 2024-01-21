import matplotlib.pyplot as plt
import numpy

# Generate sample data
# Generate sample data
L = [0,1,2,3,4,5,6,7,8,9,10]
QA = [0,11,27,47.5,66,(5/4)*66,98,111,122,131,138]
QB = [0,10,30,60,100,(5/4)*100,135,140,144,147,149]
MOLA = numpy.diff(QA).tolist()
MOLA = [numpy.nan] + MOLA
MOLB = numpy.diff(QB).tolist()
MOLB = [numpy.nan] + MOLB

# Create subplots
fig, axs = plt.subplots(1,2,figsize=(10,5))

# Scatter plot on the left
axs[0].plot(L,QA,'o-',color='blue')
axs[0].plot(L,QB,'o-',color='orange')
axs[0].set_title('Total product')
axs[0].set_xlabel('Number of employees')
axs[0].grid(True)  # Show grid

# Scatter plot on the right
axs[1].plot(L,MOLA,'o-',color='blue',label='Firm A')
axs[1].plot(L,MOLB,'o-',color='orange',label='Firm B')
axs[1].legend()
axs[1].set_title('Marginal output of labor ($MO_L$)')
axs[1].set_xlabel('Number of employees')
axs[1].grid(True)  # Show grid

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()
