import matplotlib.pyplot as plt
import numpy as np
x=[1,2,6,18]
y=[3,10,12,20]
a=np.array(x)
b=np.array(y)
plt.plot(a,b,marker='o',linestyle=':',color='red',mec='green',mfc='green')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Plotted Graph")
plt.show()

