import matplotlib.pyplot as plt
import numpy

# Data for the stacked horizontal bar chart
tasks = ['Serve as a link between\nmanagement and employees','Advise managers on\norganizational policy matters']

skills = 78*3
skill1 = (78/skills)*numpy.array([95,92])
skill2 = (78/skills)*numpy.array([95,92])
skill3 = (78/skills)*numpy.array([95,92])

colors = ['red','green','blue']  # Colors for each skill

# Create the stacked horizontal bar chart
plt.figure(figsize=(15,2))  # Set figure size
plt.barh(tasks,skill1.astype(int),color=colors[0])
plt.barh(tasks,skill2.astype(int),left=skill1.astype(int), color=colors[1])
plt.barh(tasks,skill3.astype(int),left=[skill1[i].astype(int) + skill2[i].astype(int) for i in range(len(skill1))], color=colors[2])
plt.yticks(tasks,fontsize=12)
# Create a legend for the colors
plt.legend(['Active listening','Management of Personnel Resources','Speaking'],fontsize=12,loc='upper left',bbox_to_anchor=(1.02,1.0))

ticks = numpy.arange(1,101)  # 100 ticks
labels = ['' if i % 5 != 0 else str(i) for i in ticks]
plt.xticks(ticks,labels,fontsize=12)
plt.xlabel('Minutes of daily work')
plt.grid(axis='x')
plt.title('11-3121 Human Resource Manager',fontsize=16)
plt.box(False)
plt.show()
