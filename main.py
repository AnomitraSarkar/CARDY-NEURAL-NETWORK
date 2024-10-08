import numpy as np
import nnfs
import csv
from nnfs.datasets import spiral_data

nnfs.init()

# X = [[1,2,3,2.5],
#           [2.0,5.0,-1.0,2.0],
#           [-1.5,2.7,3.3, -0.8]]

X, y = spiral_data(1000,3)

f = open("spiral.csv","w",newline="")
csv_writer = csv.writer(f)
for i,j in zip(X,y):
    rec = [i[0],i[1],j]
    csv_writer.writerow(rec)
f.close()

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1*np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons),)
    
    def forward(self,inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
    
class Activation_ReLU:
    def forward(self,inputs):
        self.output = np.maximum(0,inputs)    
        

class Activation_Softmax:
    def forward(self,inputs):
        exp_values = np.exp(inputs - np.max(inputs,axis=1,keepdims=True))
        prob = exp_values/np.sum(exp_values,axis=1,keepdims=True)
        self.output = prob

class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_Categorical_Cross_Entropy(Loss):
    def forward(self, y_pred, y_true):
        sample = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7 , 1-1e-7)
        
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(sample), y_true]
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped*y_true, axis = 1)
            
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods
        

X,y = spiral_data(samples=100,classes=3)
dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()
dense2 = Layer_Dense(3,3)
activation2 = Activation_Softmax()

print(X.shape)


dense1.forward(X)
print(dense1.output.shape)

activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)

loss_function = Loss_Categorical_Cross_Entropy()
loss = loss_function.calculate(activation2.output, y)
        
print(loss)
# layer1 = Layer_Dense(2,5)
# activation1 = Activation_ReLU()

# layer1.forward(X)
# print(layer1.output)
# activation1.forward(layer1.output)
# print(activation1.output)
# layer2 = Layer_Dense(5,2)

# layer1.forward(X)
# layer2.forward(layer1.output)
# print(layer2.output)


    


# weights = [[0.2,0.8,-0.5,1.0],
#     [0.5,-0.91,0.26,-0.5],
#     [-0.26,-0.27,0.17,0.87],]

# biases =[2,3,0.5]
# weights2 = [[0.1,0.14,0.5],
#     [-0.5,0.12,0.33],
#     [-0.44,0.73,-0.13],]

# biases2 =[-1,2,-0.5]
# layer1_output = np.dot(inputs,np.array(weights).T) + biases
# layer2_output = np.dot(layer1_output,np.array(weights2).T) + biases2



# print(layer2_output)
# # layer_outputs = []

# # for neuron_weights, neuron_bias in zip(weights, biases):
# #     neuron_output = 0
# #     for n_input, weight in zip(inputs, neuron_weights):
# #         neuron_output += n_input*weight
# #     neuron_output += neuron_bias
# #     layer_outputs.append(neuron_output)

# # plt.plot(ls)
# # plt.show()