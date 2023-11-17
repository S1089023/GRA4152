
## This file contains DataLoader, MNIST, and CIFAR10 classes 
#  It also contains the tester function for all classes
# 

# for accessing MNIST and CIFAR10
from keras.datasets import mnist
from keras.datasets import cifar10

# for transformations
import tensorflow as tf



class DataLoader:

    """
    
    Dataloader designed for working with image classification problems

    Instance variables:

        x_te: array, features from test subset
        x_tr: array, features from training subset
        y_te: array, labels from test subset
        y_tr: array, labels from training subset

    Public methods:

        preprocess()
            Applies preprocessing trasformations on dataset.
            Image scaling and one-hot-encoding of labels.

        loader(batch_size)
            Enables a user to load dataset in batches 
            @batch_size: int, number of images in one batch
            @return tf data loader object

    Examples of usage:
        
        # creates an instance of DataLoader class
        d = DataLoader()
        
    """

    ## Constructs an object 
    #
    def __init__(self):
        pass


    ## Accessor for _x_tr
    #
    @property
    def x_tr(self):
        return self._x_tr


    ## Accessor for _x_te
    #
    @property
    def x_te(self):
        return self._x_te


    ## Accessor for _y_tr
    #
    @property
    def y_tr(self):
        return self._y_tr
    

    ## Accessor for _y_te
    #
    @property
    def y_te(self):
        return self._y_te


    ## Applies preprocessing trasformations on dataset
    # 
    def preprocess(self):
        
        # scales features (image represenations) to be between 0 and 1
        # and ensures that features in both subsets are are number float32
        self._x_tr = (self._x_tr / 255).astype(dtype = "float32")
        self._x_te = (self._x_te / 255).astype(dtype = "float32")
        
        # Applies one-hot-encoding to labels in both subsets
        self._y_tr = tf.keras.utils.to_categorical(self._y_tr)
        self._y_te = tf.keras.utils.to_categorical(self._y_te)


    ## Enables a user to load dataset in batches 
    #  @batch_size: int, number of images in one batch
    #  @return tf data loader object
    # 
    def loader(self, batch_size):
        tf_dl = tf.data.Dataset.from_tensor_slices((self._x_tr, self._y_tr)).shuffle(self._x_tr.shape[0]).batch(batch_size)
        return tf_dl




class MNIST(DataLoader):


    """

    Dataloader for MNIST dataset

    Instance variables:

        All instance variables are the same as in the superclass DataLoader

    Public methods:

        preprocess()
            Applies preprocessing trasformations for MNIST dataset.
            Essentially applies all the steps from the superclass DataLoader and
            also reshapes each image from 2D (28, 28) to 1D (784) for all images
            in training and test subsets

    Examples of usage:

        # create an object of class MNIST
        m = MNIST()

        # create tf data loader object for MNIST dataset with batch_size of 256
        tr_data = m.loader(batch_size = 256)
    
    """

    ## Constructs and object, loads MNIST data, asserts that the subsets are of correct shape
    #  and calls preprocess() method
    #
    def __init__(self):
        
        # loads MNIST data
        (self._x_tr, self._y_tr), (self._x_te, self._y_te) = mnist.load_data()

        # asserting that arrays with the data have correct shapes
        assert self._x_tr.shape == (60000, 28, 28)
        assert self._x_te.shape == (10000, 28, 28)
        assert self._y_tr.shape == (60000,)
        assert self._y_te.shape == (10000,)

        # applying preprocessing transformations
        self.preprocess()


    ## applies preprocessing trasformations for MNIST dataset
    # 
    def preprocess(self):
        
        # applies all the steps from the superclass
        super().preprocess()

        # reshaping from (60000, 28, 28) to (60000, 784)
        nImages_tr = self._x_tr.shape[0]
        nFeatures_tr = self._x_tr.shape[1] * self._x_tr.shape[2] 
        self._x_tr  = self._x_tr.reshape((nImages_tr, nFeatures_tr))

        # reshaping from (10000, 28, 28) to (10000, 784)
        nImages_te = self._x_te.shape[0]
        nFeatures_te = self._x_te.shape[1] * self._x_te.shape[2] 
        self._x_te  = self._x_te.reshape((nImages_te, nFeatures_te))




class CIFAR10(DataLoader):

    """

    Dataloader for CIFAR10 dataset

    Instance variables:

        All instance variables are the same as in the superclass DataLoader

    Public methods:

        All public methods are the same as in the superclass DataLoader

    Examples of usage:

        # create an object of class CIFAR10
        c = CIFAR10()

        # create tf data loader object for CIFAR10 dataset with batch_size of 256
        tr_data = c.loader(batch_size = 256)
    
    """


    def __init__(self):
                
        # loads CIFAR10 data
        (self._x_tr, self._y_tr), (self._x_te, self._y_te) = cifar10.load_data()

        # asserting that arrays with the data have correct shapes
        assert self._x_tr.shape == (50000, 32, 32, 3)
        assert self._x_te.shape == (10000, 32, 32, 3)
        assert self._y_tr.shape == (50000, 1)
        assert self._y_te.shape == (10000, 1)
        
        # applying preprocessing transformations
        self.preprocess()
        

if __name__ == "__main__":

    # check whether an object can be created
    d = DataLoader()

    # create an object of class MNIST
    m = MNIST()

    # create an object of class CIFAR10
    c = CIFAR10()

    for obj in (m, c):
    # create tf data loader object for MNIST dataset with batch_size of 256
    # create tf data loader object for CIFAR10 dataset with batch_size of 256
        tr_data = obj.loader(batch_size = 256)

