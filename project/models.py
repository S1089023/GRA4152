
## This file contains NeuralNetwork, FullyConNN, and ConvNN classes
#  It also contains the tester function for all classes
# 

# for models bulding
from tensorflow.keras import layers, Model
from tensorflow.keras.models import Sequential
import tensorflow as tf




class NeuralNetwork(Model):

    """

    A Neural Network designed for classification problems

    Instance variables:

        _cls: classification layer of a neural network.

        While calling the constructor method the following parameters are expected:
            @neurons: int, the number of neurons in the last layer before the classification layer
            @y_dim: int, the number of classes the model is intended to identify

    Public methods:

        classifier(neurons, y_dim)
            Adds the classification layer
            @neurons: int, the number of neurons in the last layer before the classification layer
            @y_dim: int, the number of classes the model is intended to identify 

        call(x, y)
            Given the features and true class labels, uses the neural network 
            to generate (pseudo)probabilities  based on observed features and calculates 
            a loss function given true labels and (pseudo)probabilities
            @x: array of features (e.g. images)
            @y: array of true class labels, one-hot encoded
            @return loss: array, the result of appliction of the loss function given true labels and (pseudo)probabilities

        train(inputs, optimizer)
            Updates model parameters using the provided optimizer 
            @inputs: a tuple (x, y) which contains an array of features and an array of labels 
            @optimizer: optimizer object from keras, optimizer to be used for training of a neural network 
            @return loss: array, the result of appliction of the loss function given true labels and (pseudo)probabilities

        test(x)
            Generates (pseudo)probabilities for provided observations without true labels
            @x: array, features of observations (e.g. images) for which (pseudo)probabilities should be calculated
            @return pi_hat: array, predicted (pseudo)probabilities

    Examples of usage:

        # creates a neural network with a classification layer that expects the last hidden 
        # layer to have 50 neurons, and this layer is intended to identify 10 classes in the dataset
        nn = NeuralNetwork(neurons = 50, y_dim = 10)

        # Since this class is a superclass for the purposes of this project and doesn't contain hidden layers
        # other method calls (expect for print(nn)) are not expected
    
    """

    ## Defines instance variables of the superclass Model and calls 
    #  classifier() method to add the output layer 
    #  for classification problem  
    #  @neurons: int, the number of neurons in the last layer before the classification layer
    #  @y_dim: int, the number of classes the model is intended to identify
    # 
    def __init__(self, neurons, y_dim):
        
        # calls the constructor method of a superclass imported from tf.keras
        super().__init__()
        
        # creates an instance variable that contains classification layer
        self.classifier(neurons = neurons, y_dim = y_dim)


    ## Prints a short description of the class
    #
    def __repr__(self):
        return "Neural Network designed for classification problems."


    ## Adds the classification layer
    #  @neurons: int, the number of neurons in the last layer before the classification layer
    #  @y_dim: int, the number of classes the model is intended to identify 
    #
    def classifier(self, neurons, y_dim):

        # creates an instance variable that contains classification layer
        self._cls = Sequential([layers.InputLayer(input_shape = neurons), 
                                layers.Dense(y_dim, activation='softmax')])


    ## Given the features and true class labels, uses the neural network 
    #  to generate (pseudo)probabilities  based on observed features and calculates 
    #  a loss function given true labels and (pseudo)probabilities
    #  @x: array of features (e.g. images)
    #  @y: array of true class labels, one-hot encoded
    #  @return loss: array, the result of application of the loss function given true labels and (pseudo)probabilities
    #  
    def call(self, x, y):
        
        # applies hidden layer(s) transformations to features contained in x
        out = self._hidden(x)

        # applies classification layer to the output of hidden layer(s)
        out = self._cls(out)
        
        # calculates the loss function 
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, out))
        
        return loss
    

    ## Updates model parameters using the provided optimizer 
    #  @inputs: a tuple (x, y) which contains an array of features and an array of labels 
    #  @optimizer: optimizer object from keras, optimizer to be used for training of a neural network 
    #  @return loss: array, the result of appliction of the loss function given true labels and (pseudo)probabilities
    # 
    def train(self, inputs, optimizer):

        # creates a type object from tensorflow
        with tf.GradientTape() as tape:
            
            # calls call() method on provided features and labels
            loss = self.call(*inputs)

        # calculates gradients
        gradients = tape.gradient(loss, self._params)

        # updates the model parameters given the gradients and previously used parameters
        optimizer.apply_gradients(zip(gradients, self._params))
        
        return loss
    

    ## Generates (pseudo)probabilities for provided observations without true labels
    #  @x: array, features of observations (e.g. images) for which (pseudo)probabilities should be calculated
    #  @return pi_hat: array, predicted (pseudo)probabilities
    # 
    def test(self, x):
        
        # applies hidden layer(s) transformations to features contained in x
        out = self._hidden(x)
        
        # applies classification layer to the output of hidden layer(s)
        pi_hat = self._cls(out)

        return pi_hat



class FullyConNN(NeuralNetwork):

    """

    A fully connected neural network 

    Instance variables:

        _hidden: hidden layer(s)
        _params: trainable_variables from hidden layer(s) and classification layer  

        While calling the constructor method the following parameters are expected:
            @neurons: int, the number of neurons in the last layer before the classification layer
            @y_dim: int, the number of classes the model is intended to identify

    Public methods:

        hidden_layers(neurons, input_shape = (28 * 28))
            Defines two hidden layers for a fully connected neural network
            @neurons: int, the number of neurons to be used in both hidden layers
            @input_shape: the size of a vector of features for each observation, default value of (28 * 28) is for MNIST dataset 
        
    Examples of usage:

        # creates a fully connected neural network with a classification layer that expects the last hidden 
        # layer to have 50 neurons, and this layer is intended to identify 10 classes in the dataset
        # Also, it expects input data to have 28*28 dimensions as it is developed primarily for working with MNIST dataset
        # Furthemore, it already has two hidden layers with 50 neurons in each layer
        fcnn = FullyConNN(neurons = 50, y_dim = 10)

    """

    ## Defines instance variables 
    #  @neurons: int, the number of neurons in the last layer before the classification layer
    #  @y_dim: int, the number of classes the model is intended to identify
    #  @input_shape: the size of a vector of features for each observation, default value of (28 * 28) is for MNIST dataset 
    # 
    def __init__(self, neurons, y_dim, input_shape = (28 * 28)):

        # calls the constructor method of NeuralNetwork class
        # as a result a classification layer is created with provided number 
        # of neurons (neurons parameter) expected from the last hidden layer 
        # and appropriate number of clases the model should identify (y_dim parameter)
        #  
        super().__init__(neurons = neurons, y_dim = y_dim)

        # calls hidden_layers() method to define self._hidden 
        # uses default values of input_shape, because in this assignment
        # we are asked to use fully connected neural network only for MNIST dataset
        self.hidden_layers(neurons = neurons, input_shape = input_shape)

        # defines _params instance variable that is going to store
        # trainable_variables from hidden layer(s) and classification layer  
        self._params = self._cls.trainable_variables + self._hidden.trainable_variables


    ## Prints a short description of the class
    #
    def __repr__(self):
        return "Fully Connected Neural Network."


    ## Defines two hidden layers for a fully connected neural network
    #  @neurons: int, the number of neurons to be used in both hidden layers
    #  @input_shape: the size of a vector of features for each observation
    #  
    def hidden_layers(self, neurons, input_shape):
        self._hidden = Sequential([layers.InputLayer(input_shape = input_shape), 
                                   layers.Dense(neurons),
                                   layers.Dense(neurons)])




class ConvNN(NeuralNetwork):

    """

    A convolutional neural network

    Instance variables:

        _hidden: hidden layer(s)
        _params: trainable_variables from hidden layer(s) and classification layer

        While calling the constructor method the following parameters are expected:
            @neurons: int, the number of neurons in the last layer before the classification layer
            @y_dim: int, the number of classes the model is intended to identify
            @input_shape: tuple, the dimensions of input observations, by default is (32, 32, 3) which corresponds to images from CIFAR10
            @filters: int, the number of filters to be used in the first convolutional layer, and half the number of filters for the second convolutional layer, by default equals to 32
            @kernel_size: int, kernel size to be used in all three convolutional layers, by default is equal to 3
            @strides: tuple, strides to be used in the first two convolutional layers, by default is (2, 2)

    Public methods:

        hidden_layers(neurons, input_shape, filters, kernel_size, strides)
            Defines three convolutional layers in two dimensions and flattens the output of the last one
            @neurons: int, the number filters to use in the last convolutional layer
            @input_shape: tuple, the dimensions of input observations
            @filters: int, the number of filters to be used in the first convolutional layer, and half the number of filters for the second convolutional layer
            @kernel_size: int, kernel size to be used in all three convolutional layers
            @strides: tuple, strides to be used in the first two convolutional layers
        
    Examples of usage:

        # creates a convolutional neural network with three convolutional layers and a classication layer
        # expects an input shape of images to be (32, 32, 3) i.e. size of CIFAR10 images
        cnn = ConvNN(neurons = 50, y_dim = 10)
        
    """


    ## Defines instance variables 
    #
    def __init__(self, neurons, y_dim, input_shape = (32, 32, 3), filters = 32, kernel_size = 3, strides = (2,2)):

        # calls the constructor method of NeuralNetwork class 
        super().__init__(neurons = neurons, y_dim = y_dim)
        
        # calls hidden_layers() method to define self._hidden 
        self.hidden_layers(neurons = neurons, input_shape = input_shape, filters = filters, kernel_size = kernel_size, strides = strides)
        
        # defines _params instance variable that is going to store
        # trainable_variables from hidden layer(s) and classification layer  
        self._params = self._cls.trainable_variables + self._hidden.trainable_variables


    ## Prints a short description of the class
    #
    def __repr__(self):
        return "Convolutional Neural Network."


    ## Defines three convolutional layers in two dimensions and flattens the output of the last one
    #  @neurons: int, the number filters to use in the last convolutional layer
    #  @input_shape: tuple, the dimensions of input observations
    #  @filters: int, the number of filters to be used in the first convolutional layer, and half the number of filters for the second convolutional layer
    #  @kernel_size: int, kernel size to be used in all three convolutional layers
    #  @strides: tuple, strides to be used in the first two convolutional layers
    #
    def hidden_layers(self, neurons, input_shape, filters, kernel_size, strides):
        self._hidden = Sequential([layers.InputLayer(input_shape = input_shape), 
                                   layers.Conv2D(filters = filters, kernel_size = kernel_size, strides=strides), 
                                   layers.Conv2D(filters = 2 * filters, kernel_size = kernel_size, strides = strides), 
                                   layers.Conv2D(filters = neurons, kernel_size = kernel_size, strides = (5,5)), 
                                   layers.Flatten()])





if __name__ == "__main__":

    # testing NeuralNetwork
    print("Tesing NeuralNetwork")
    nn = NeuralNetwork(neurons = 50, y_dim = 10)
    print(nn)
    print("Expected output:")
    print("Neural Network designed for classification problems.")
    print("-" * 50)

    # testing FullyConNN
    print("Testing FullyConNN")
    fcnn = FullyConNN(neurons = 50, y_dim = 10)
    print(fcnn)
    print("Expected output:")
    print("Fully Connected Neural Network.")

    # input for classification layer
    assert fcnn._params[0].shape == (50, 10)
    
    # output of clasification layer
    assert fcnn._params[1].shape == (10)

    # transformations in the first dense layer
    assert fcnn._params[2].shape == (784, 50)
    assert fcnn._params[3].shape == (50,)

    # transformations in the second dense layer
    assert fcnn._params[4].shape == (50, 50)
    assert fcnn._params[5].shape == (50,)

    print("-" * 50)


    # testing ConvNN
    print("Testing ConvNN")
    cnn = ConvNN(neurons = 50, y_dim = 10)
    print(cnn)
    print("Expected output:")
    print("Convolutional Neural Network.")


    # input for classification layer
    assert cnn._params[0].shape == (50, 10)
    
    # output of clasification layer
    assert cnn._params[1].shape == (10)
    
    # transformations inside the first convolutional layer 
    assert cnn._params[2].shape == (3, 3, 3, 32)
    assert cnn._params[3].shape == (32,)

    # transformations inside the second convolutional layer 
    assert cnn._params[4].shape == (3, 3, 32, 64) 
    assert cnn._params[5].shape == (64,)

    # transformations inside the third convolutional layer 
    assert cnn._params[6].shape == (3, 3, 64, 50)
    assert cnn._params[7].shape == (50,)
