import matplotlib.pyplot as plt
import numpy

# Generate sample data
# Generate sample data
L = [0,1,2,3,4,5,6,7,8,9,10]
QA = [0,11,27,47.5,66,(5/4)*66,98,111,122,131,138]
QB = [0,10,30,60,100,(5/4)*100,135,140,144,147,149]
MOLA = numpy.diff(QA).tolist()
MOLA = [numpy.nan] + MOLA
VMOLA = [3*x for x in MOLA]
MOLB = numpy.diff(QB).tolist()
MOLB = [numpy.nan] + MOLB
VMOLB = [3*x for x in MOLB]
w = [50 for _ in range(11)]

# Create subplots
fig, ax = plt.subplots(1,1,figsize=(12,12))

# Scatter plot
ax.plot(L,VMOLA,'o-',color='blue',label='$VMOL$ of Firm A')
ax.plot(L,VMOLB,'o-',color='orange',label='$VMOL$ of Firm B')
ax.plot(L,w,'o-',color='green',label='Wage') 
ax.legend()
ax.set_xlabel('Number of employees')

# Setting the grid
ax.minorticks_on() # Enable minor ticks if needed
ax.grid(which='major', color='grey', linestyle='-', linewidth=0.5)
ax.grid(which='minor', color='lightgrey', linestyle='--', linewidth=0.5, alpha=0.5)

# Customize ticks to ensure they fall at every unit
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(-1, 2, 1.0))

# Show the plots
plt.show()
