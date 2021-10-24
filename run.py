from common.functions import function_type
from perceptron import MLP
from common.problem_type import problem_type
from common.reader import normalize, prepare_data
from common.graphs import generate, generate_regression_graph, generate_classification_graph_of_points
import numpy as np
from matplotlib import pyplot

# Parameters

PROBLEM_TYPE = problem_type.Regression
PATH_TO_TRAIN_DATASET = "data/regression/data.activation.train.1000.csv"
PATH_TO_TEST_DATASET = "data/regression/data.activation.test.1000.csv"
# PATH_TO_TRAIN_DATASET = "data/classification/data.simple.train.100.csv"
# PATH_TO_TEST_DATASET = "data/classification/data.simple.test.100.csv"


LAYERS = [1, 32, 16, 1]
ACTIVATION_FUNCTION = function_type.Tanh
TRANSFER_FUNCTION = function_type.Simple
EPOCHS = 1000
LEARINN_RATE = 0.01
LEARINN_COEFFICIENT = 0.01
SEED = 141
SHOW_PERCENTAGE = 1
BIAS = True

if __name__ == "__main__":
    # perceptron = MLP(LAYERS, ACTIVATION_FUNCTION, TRANSFER_FUNCTION,
    #                  EPOCHS, LEARINN_RATE, LEARINN_COEFFICIENT, SEED, BIAS)
    # train_dataset = prepare_data(PROBLEM_TYPE, PATH_TO_TRAIN_DATASET)
    # test_dataset = prepare_data(PROBLEM_TYPE, PATH_TO_TEST_DATASET)

    # print("train", train_dataset[0][0], train_dataset[0][1])
    # print("test", test_dataset[0][0], test_dataset[0][1])

    # train_dataset, test_dataset = normalize(train_dataset, test_dataset)

    # print("train", train_dataset[0][0], train_dataset[0][1])
    # print("test", test_dataset[0][0], test_dataset[0][1])

    # x = []
    # y = []
    # for i in range(len(test_dataset)):
    #     x.append(test_dataset[i][0])
    #     y.append(test_dataset[i][1])

    # tx = []
    # ty = []
    # for i in range(len(train_dataset)):
    #     tx.append(train_dataset[i][0])
    #     ty.append(train_dataset[i][1])

    # perceptron.train(train_dataset, SHOW_PERCENTAGE)
    # _, _, predictions = perceptron.test(test_dataset, SHOW_PERCENTAGE)

    # generate_regression_graph((x, y), (x, predictions), (tx, ty))



    # generate_classification_graph_of_points(predictions)

    # predictions123 = []
    # for _ in range(20):
    #     perceptron.train(train_dataset, SHOW_PERCENTAGE)
    #     _, _, predictions = perceptron.test(train_dataset, SHOW_PERCENTAGE)
    #     predictions123.append(np.concatenate(predictions))

    #     # generate_regression_graph((x, y), (x, predictions))
    #     # generate_classification_graph_of_points(predictions)
    # pyplot.scatter(x, y, c="black")
    # color = "blue"
    # for i in range(20):
    #     pyplot.scatter(x, predictions123[i], c=color)
    #     if i == 7: color = "red"
    #     if i == 15: color = "yellow"
    # # pyplot.scatter(x, predictions123[0], c="red")
    # # pyplot.scatter(x, predictions123[1], c="blue")
    # # pyplot.scatter(x, predictions123[2], c="yellow")
    # # pyplot.scatter(x, predictions123[3], c="green")
    # # pyplot.scatter(x, predictions123[4], c="brown")
    # pyplot.show()

    dataset = prepare_data(problem_type.Classification, "data/classification/data.simple.test.1000.csv")
    generate(dataset)
    # generate_classification_graph_of_points(dataset)

