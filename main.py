import numpy as np
from Interface import displayed_window

def load_the_data():
    interface = displayed_window()

    #Loads the Data from the MNIST dataset, that was converted into a CSV format

    training_data = np.genfromtxt('Handwriting Data\MNIST Data (Digits)\mnist_train_data.csv',delimiter=',')
    training_labels = np.genfromtxt('Handwriting Data\MNIST Data (Digits)\mnist_train_labels.csv', delimiter=',')

    testing_data = np.genfromtxt('Handwriting Data\MNIST Data (Digits)\mnist_test_data.csv',delimiter=',')
    testing_labels = np.genfromtxt('Handwriting Data\MNIST Data (Digits)\mnist_test_labels.csv',delimiter=',')




    interface.main(training_data, training_labels, testing_data, testing_labels)
load_the_data()
