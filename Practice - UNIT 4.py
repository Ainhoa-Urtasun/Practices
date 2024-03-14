import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
L = [0,1,2,3,4,5,6,7,8,9,10]
QA = [0,11,27,47.5,66,(5/4)*66,98,111,122,131,138]
QB = [0,10,30,60,100,(5/4)*100,135,140,144,147,149]
MOLA = np.diff(QA).tolist()
MOLA = [np.nan] + MOLA
VMOLA = [3*x for x in MOLA]
MOLB = np.diff(QB).tolist()
MOLB = [np.nan] + MOLB
VMOLB = [3*x for x in MOLB]
w = [50 for _ in range(11)]

# Set figure size here
plt.figure(figsize=(10,6))  # Increase the size of the figure

# Scatter plot
plt.plot(L, VMOLA, 'o-', color='blue', label='$VMOL$ of Firm A')
plt.plot(L, VMOLB, 'o-', color='orange', label='$VMOL$ of Firm B')
plt.plot(L, w, 'o-', color='green', label='Wage')
plt.legend()
plt.xlabel('Number of employees')
plt.ylabel('Euros')  # Assuming you might want a label for the y-axis as well

# Setting the grid
#plt.minorticks_on() # Enable minor ticks if needed
plt.grid(which='major', color='grey', linestyle='-', linewidth=0.5)
#plt.grid(which='minor', color='lightgrey', linestyle='--', linewidth=0.5, alpha=0.5)

# Filter out np.nan values before finding min and max for y-axis ticks
VMOLA_filtered = [x for x in VMOLA if not np.isnan(x)]
VMOLB_filtered = [x for x in VMOLB if not np.isnan(x)]
max_value = max(max(VMOLA_filtered), max(VMOLB_filtered), max(w))

# Customize ticks to ensure they fall at every unit
plt.xticks(np.arange(0, max(L)+1, 1.0))
plt.yticks(np.arange(0, max_value+5, 5.0))

# Show the plots
plt.show()
