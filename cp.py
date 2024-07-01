# import numpy as np

# biases =[2,3,0.5]


# def spiral_data(points, classes):
#     X = np.zeros((points*classes, 2))
#     y = np.zeros(points*classes, dtype='uint8')
#     for class_number in range(classes):
#         ix = range(points*class_number, points*(class_number+1))
#         r = np.linspace(0.0, 1, points)  # radius
#         t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
#         X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
#         y[ix] = class_number
#     return X, y
# import matplotlib.pyplot as plt

# print("Here")
# X,y = spiral_data(100,12)
# plt.scatter(X[:,0],X[:,1],c=y,cmap="brg")
# plt.show()

import math

layer_outputs = [4.8,1.21,2.385]

E = math.e

exp_values = [E**i for i in layer_outputs]

normalize = [i/sum(exp_values) for i in exp_values]


print(normalize)