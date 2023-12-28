import matplotlib.pyplot as plt
import numpy

# Data for the stacked horizontal bar chart
tasks = ['Serve as a link between\nmanagement and employees',
         'Advise managers on\norganizational policy matters',
         'Analyze and modify compensation\nand benefits policies',
         'Perform difficult staffing duties\nincluding firing employees',
         'Represent organization at personnel-related events']

colors = ['red','green','blue','yellow','grey']  # Colors for each skill

# Create the stacked horizontal bar chart
plt.figure(figsize=(15,7))  # Set figure size
plt.barh(tasks,[3,3,1,1,1],color=colors[0])
plt.barh(tasks,[3,3,3,3,3],left=[3,3,1,1,1], color=colors[1])
plt.barh(tasks,[3,3,1,2,3],left=numpy.array([3,3,1,1,1])+numpy.array([3,3,3,3,3]),color=colors[2])
plt.barh(tasks,[1,3,3,3,1],left=numpy.array([3,3,1,1,1])+numpy.array([3,3,3,3,3])+numpy.array([3,3,1,2,3]),color=colors[3])
plt.barh(tasks,[1,1,3,1,1],left=numpy.array([3,3,1,1,1])+numpy.array([3,3,3,3,3])+numpy.array([3,3,1,2,3])+numpy.array([1,3,3,3,1]),color=colors[4])
plt.yticks(tasks,fontsize=12)
# Create a legend for the colors
plt.legend(['Active listening','Management of Personnel Resources','Speaking','Judgement and Decision Making','Reading Comprehension'],
           fontsize=12,loc='upper left',bbox_to_anchor=(1.02,1.0))

ticks = numpy.arange(1,15)  # 15 ticks
labels = ['' if i % 1 != 0 else str(i) for i in ticks]
plt.xticks(ticks,labels,fontsize=12)
plt.xlabel('Weekly Working Hours')
plt.grid(axis='x')
plt.title('11-3121 Human Resource Managers',fontsize=16)
plt.box(False)
plt.show()
