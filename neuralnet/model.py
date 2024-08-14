import numpy as np

np.random.seed(1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def train_model(training_inputs, training_outputs):
    training_set_inputs = np.array(training_inputs)
    training_set_outputs = np.array(training_outputs).T

    synaptic_weights = 2 * np.random.random((3, 1)) - 1

    for i in range(100_000):
        output = sigmoid(np.dot(training_set_inputs, synaptic_weights))

        if i % 1000 == 0:
            print("Output: ", output)
            print("Training Input (Transposed): ", training_set_inputs.T)
            print("Training Output: ", training_set_outputs)

        synaptic_weights += np.dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    
    def predict(input):
        return 1 / (1 + np.exp(-(np.dot(np.array(input), synaptic_weights))))
    
    return predict


training_inputs = [[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]]
training_outputs = [[0, 1, 1, 0]]

model = train_model(training_inputs, training_outputs)

# Spróbuj zmienić input na rózne kombinacje 0 i 1
input = [1, 0, 0]

result = model(input)
print(result)
