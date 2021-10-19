import numpy as np
from common.functions import function_type


class MLP:
    """
    Neural Network Class
    """

    def __init__(self, layers, activation_function, transfer_function, epochs, learning_rate, learning_coefficient, seed, bias=False):
        """
        Args:
            layers (list): list of layers in the network
            activation_function (function): sigmoid function used in the internal neurons of the network
            transfer_function (function): activation function used on the output layer
            epochs (int): number of epochs to learn
            learning_rate (float): learning rate coefficient
            learning_coefficient (float): learning coefficient
            seed (int): number used as a seed for random number generator
        """
        np.random.seed(seed)
        self.layers = layers
        self.activation_function = activation_function
        self.transfer_function = transfer_function
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.learning_coefficient = learning_coefficient
        self.bias = bias

        self.weights = []
        self.biases = []
        for i in range(len(layers)-1):
            if self.bias:
                b = np.random.randn(layers[i + 1])
                self.biases.append(b / np.sqrt(layers[i + 1]))
                # self.biases.append([1 for _ in range(layers[i + 1])])
            w = np.random.randn(layers[i], layers[i + 1])
            # w = [[1 for _ in range(layers[i + 1])] for _ in range(layers[i])]
            self.weights.append(w / np.sqrt(layers[i]))
            # self.weights.append(np.array(w))
            # self.delta_weights = [np.zeros((layer_s[i], layer_s[i+1])) for i in range(len(layer_s)-1)
        # ]

    def feed_forward(self, data):
        output = [data]
        z = [data]
        tmp = data

        for i in range(len(self.weights)):
            tmp = np.dot(tmp, self.weights[i])
            if self.bias:
                tmp += self.biases[i]
            z.append(np.array(tmp))
            tmp = np.array([self.activation_function(x) for x in tmp])
            output.append(tmp)
        return output, z

    def backpropagation(self, outputs, z, result, data):
        error = outputs[-1] - np.array(result)
        D_weights = [np.multiply(error, [outputs[-2].T])]
        D_biases = [error]
        tmp = error
        for layer in range(len(self.weights) - 2, -1, -1):  # PYTANIE: wzór ? dobry?
            tmp = np.multiply(tmp, self.weights[layer+1].T)
            tmp = np.multiply(
                tmp, self.activation_function.derivative(z[layer+1]))
            D_biases.append(tmp[0])
            tmp1 = np.multiply(tmp, outputs[layer].T)
            D_weights.append(tmp1)

        # D_weights = D_weights[::-1]
        # D_weights = [k for k in reversed(D_weights)]
        # D_biases = D_biases[::-1]
        # print("WEI", self.weights)
        # print("BIA", self.biases)
        # print("WEIG_D",D_weights)
        # print("BIAS_D",D_biases)
        # input()
        # PYTANIE: UPDATE wag przy propagacji wstecznej czy po przejściu przez wyszystkie wagi?
        for i in range(len(self.weights)-1, -1, -1):
            tmp_i = len(self.weights) - i - 1
            self.weights[tmp_i] -= self.learning_rate * D_weights[i]
            if self.bias:
                self.biases[tmp_i] -= self.learning_rate * D_biases[i]

    def train(self, dataset, show_percentage=1):
        print('----START TRAINING----')
        showing_param = 0
        for i in range(self.epochs):
            for X, Y in dataset:
                output, z = self.feed_forward(X)
                self.backpropagation(output, z, Y, X)
            if i/self.epochs >= showing_param/100:
                print(f'Training progress status: {showing_param}%')
                showing_param += show_percentage
        print(f'Training progress status: {100}%')
        print('----TRAINING FINISHED----')

    def predict(self, data):
        return self.feed_forward(data)[0][-1]

    def test(self, dataset, show_percentage=1):
        print('----START TEST----')
        counter = 0
        showing_param = 0
        non_zero = 0
        len_dataset = len(dataset)
        for i in range(len_dataset-1):
            data, result = dataset[i]
            prediction = self.predict(data)
            if i/len_dataset >= showing_param/100:
                print(f'Test progress status: {showing_param}%')
                showing_param += show_percentage
            if prediction == result:
                counter += 1
            if prediction != 0:
                non_zero = non_zero + 1
        print(f'Test progress status: {100}%')
        print('----TEST FINISHED----')
        print(f'Correct predicted rate: {counter/len_dataset * 100}%')
        print("Non zero: ", str(non_zero))


if __name__ == "__main__":
    perceptron = MLP([1, 3, 1], function_type.Simple,
                     function_type.Simple, 1, 0.5, 0.5, 0, True)
    # data_set = [[np.array([1,2]),1],[np.array([-1,-2]),0],[np.array([2,2]),1]]
    data_set = [[np.array([1]), 1]]
    perceptron.train(data_set)
    print("-------")
    print(perceptron.predict(data_set[0][0]))
