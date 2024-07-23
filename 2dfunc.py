import matplotlib.pyplot as plt
import csv
from math import cos, sin, pi, e
import numpy as np
import random

def fx(x,k): # define x parametric equation
    # return k*cos(x)
    return k*x**2
def fy(y,k): # define y parametric equation
    # return k*sin(y) 
    return 2*k*y

#parametric kernel
params = np.arange(-2*pi,2*pi,0.01).tolist()
xvals = []
yvals = []
for i in params:
    xvals.append(fx(i+random.random(),6))
    yvals.append(fy(i+random.random(),3))

# plotter
plt.plot(xvals, yvals)
plt.show()

#saving the values
f = open("data2d.csv","w",newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(['input','outputx','outputy'])
for i,j,k in zip(params,xvals,yvals):
    csv_writer.writerow([i,j,k])
f.close()