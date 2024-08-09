import matplotlib.pyplot as plt
import numpy as np
import random
import csv, math

def f(x):# provide any function here
    return 2*x**4-(3*x**2)+2*x

xvals = []
fxvals = []
# for i in range(-200,200):
#     xvals.append()
#     fxvals.append(f((i-5*random.random())))

xvals = np.arange(-2, 2, 0.05).tolist()
print(xvals)
for i in xvals:
    fxvals.append(f(i))
f=open("data.csv","w",newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["X","FX"])
for i, j in zip(xvals, fxvals):
    csv_writer.writerow([i,j])
f.close()
plt.plot(xvals,fxvals)
plt.show()
    