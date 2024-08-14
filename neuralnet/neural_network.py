import numpy as np

np.random.seed(1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def predict(input):
    training_set_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = np.array([[0, 1, 1, 0]]).T

    synaptic_weights = 2 * np.random.random((3, 1)) - 1

    for i in range(100_000):
        output = sigmoid(np.dot(training_set_inputs, synaptic_weights))

        if i % 1000 == 0:
            print("Output: ", output)
            print("Training Input (Transposed): ", training_set_inputs.T)
            print("Training Output: ", training_set_outputs)

        synaptic_weights += np.dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))

    result = 1 / (1 + np.exp(-(np.dot(np.array(input), synaptic_weights))))
    return result


input = [0, 1, 0]

result = predict(input)

print(result)
