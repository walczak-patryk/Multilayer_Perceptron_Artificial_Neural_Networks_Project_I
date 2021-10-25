import numpy as np
from common.functions import function_type, cross_entropy, mse
from common.problem_type import problem_type


class MLP:
    """
    Neural Network Class
    """

    def __init__(self, problem_type, layers, activation_function, output_function, epochs, learning_rate, seed, bias=False):
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
        self.problem_type = problem_type
        self.layers = layers
        self.activation_function = activation_function
        self.output_function = output_function
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.bias = bias

        self.weights = []
        self.biases = []
        for i in range(len(layers)-1):
            if self.bias:
                b = np.random.randn(layers[i + 1])
                self.biases.append(b / np.sqrt(layers[i + 1]))
            w = np.random.randn(layers[i], layers[i + 1])
            self.weights.append(w / np.sqrt(layers[i]))

    def feed_forward(self, data):
        output = [data]
        z = [data]
        tmp = data

        for i in range(len(self.weights)):
            tmp = np.dot(tmp, self.weights[i])
            if self.bias:
                tmp += self.biases[i]
            z.append(np.array(tmp))
            if i < (len(self.weights) - 1):
                tmp = np.array([self.activation_function(x) for x in tmp])
            else:
                if self.problem_type == problem_type.Classification:
                    tmp = np.array([self.activation_function(x) for x in tmp])
                elif self.problem_type == problem_type.Regression:
                    tmp = np.array([self.output_function(x) for x in tmp])
            output.append(tmp)
        return output, z

    def backpropagation(self, outputs, z, result):
        error = outputs[-1] - np.array(result)
        D_weights = [np.multiply(np.atleast_2d(
            error), np.atleast_2d(outputs[-2]).T)]
        D_biases = [error]
        tmp = error
        for layer in range(len(self.weights) - 2, -1, -1):
            tmp = np.dot(tmp, self.weights[layer+1].T)
            tmp = np.multiply(
                tmp, self.activation_function.derivative(z[layer+1]))
            D_biases.append(tmp[0])
            tmp1 = np.multiply(tmp, np.atleast_2d(outputs[layer]).T)
            D_weights.append(tmp1)

        for i in range(len(self.weights)-1, -1, -1):
            tmp_i = len(self.weights) - i - 1
            self.weights[tmp_i] -= self.learning_rate * D_weights[i]
            if self.bias:
                self.biases[tmp_i] -= self.learning_rate * D_biases[i]

    def train(self, dataset, show_percentage=1):
        print('----START TRAINING----')
        showing_param = 0
        np.random.shuffle(dataset)
        for i in range(self.epochs):
            for X, Y in dataset:
                output, z = self.feed_forward(X)
                self.backpropagation(output, z, Y)
            if i/self.epochs >= showing_param/100:
                print(f'Training progress status: {showing_param}%')
                showing_param += show_percentage
        print(f'Training progress status: {100}%')
        print('----TRAINING FINISHED----')

    def predict(self, data):
        prediction = self.feed_forward(data)[0][-1]
        if self.problem_type == problem_type.Classification:
            prediction = self.output_function(prediction)
            prediction = np.argmax(prediction)
        return prediction

    def test(self, dataset, show_percentage=1):
        print('----START TEST----')
        counter = 0
        showing_param = 0
        len_dataset = len(dataset)
        targets = []
        predictions = []
        for i in range(len_dataset):
            data, result = dataset[i]
            prediction = self.predict(data)
            if self.problem_type == problem_type.Classification:
                result = np.nonzero(result)[0][0]
                if prediction == result:
                    counter += 1
            targets.append(result)
            predictions.append(prediction)
            if i/len_dataset >= showing_param/100:
                print(f'Test progress status: {showing_param}%')
                showing_param += show_percentage   
        print(f'Test progress status: {100}%')
        print('----TEST FINISHED----')
        prediction_rate = counter/len_dataset * 100
        loss = 0  # mse(predictions, targets)
        print(f'Correct predicted rate: {prediction_rate}%')
        # print(f'Loss function : {loss}')
        return prediction_rate, loss, predictions


if __name__ == "__main__":
    perceptron = MLP(problem_type.Regression, [1, 3, 2, 10, 8, 1231, 513, 123, 1], function_type.Simple,
                     function_type.Simple, 1, 0.5, 0.5, 0, True)
    # data_set = [[np.array([1,2]),1],[np.array([-1,-2]),0],[np.array([2,2]),1]]
    data_set = [[np.array([1]), 1]]
    perceptron.train(data_set)
    print("-------")
    print(perceptron.predict(data_set[0][0]))
