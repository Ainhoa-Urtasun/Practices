import numpy as numpy
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
L = numpy.linspace(1,28,100)
Q = L**0.25
plt.plot(L,Q)
x0 = 16
y0 = 16**0.25
m = 0.25*16**(-0.75)
plt.plot(x0,y0,color='red',marker='o')
plt.plot([x0,x0],[1,y0],linestyle='--',color='red')
plt.plot([-1,x0],[y0,y0],linestyle='--',color='red')
x = numpy.linspace(0,28,100)
plt.plot(x,m*x-x0*m+y0,color='green')
plt.axhline(1,color='black',linewidth=0.5)
plt.axvline(0,color='black',linewidth=0.5)
plt.xlabel('Labor (L)')
plt.title('Q (K = 1)')
plt.box(False)
plt.xticks(range(0,28,2))
plt.yticks(numpy.arange(1,2.5,0.25))
plt.grid(True)
plt.show()
