
## This file contains the train function that trains 
#  the specified neural network on the specified dataset 
#  and prints out the AUC metric of model performance on the testing subset
# 

# for user-friendly usage from the command line
import argparse
import textwrap

# importing the models
from models import FullyConNN, ConvNN

# importing the dataloaders
from dataloaders import MNIST, CIFAR10

# for training
import tensorflow as tf

# for performance analysis
from sklearn.metrics import roc_auc_score


## Trains the model and prints out AUC metric of model performance on the testing subset
#
def train(dset, nn_type, epochs = 10, neurons = 50, batch_size = 256):

    # ensure that epochs and neurons are as expected
    assert epochs > 0, "epochs should be an integer greater than zero"
    assert neurons > 0, "neurons should be an integer greater than zero"



    # defines optimizer with an appropriate learning rate
    optimizer = tf.keras.optimizers.Adam(learning_rate = 5e-4)

    # use MNIST dataloader class if a user specified "mnist"
    if dset == "mnist":      
        data_loader = MNIST()

    # use CIFAR10 dataloader class if a user specified "cifar10"
    elif dset == "cifar10":
        data_loader = CIFAR10()

    # ensure that batch_size is within expected range
    if (batch_size < 1) or (batch_size > data_loader.x_tr.shape[0]):
        raise ValueError("batch_size should be an integer between 1 and the number of images in the training subset")
    
    # create tf data loader object with specified batch_size
    tr_data = data_loader.loader(batch_size = batch_size)
    

    # use FullyConNN model if a user specified "fully_con"
    if nn_type == "fully_con":
        # the number of neurons passed are the ones that a user specified
        # the number of classes should be 10 independent of user choices
        model = FullyConNN(neurons = neurons, y_dim = 10)

    # use ConvNN model if a user specified "conv"
    elif nn_type == "conv":
        # the number of neurons passed are the ones that a user specified
        # the number of classes should be 10 independent of user choices
        model = ConvNN(neurons = neurons, y_dim = 10)


    # training routine
    step = 0 # counter for current epoch
    while step < epochs: # iterate epochs number of times
        
        # load data in batches
        for i, data_batch in enumerate(tr_data): 
            
            # train model on each batch 
            losses = model.train(data_batch, optimizer)
        
        # print out the current epoch and loss of the last batch
        print(f"Epoch: {step}, last batch's loss: {losses.numpy().mean():.4f}") 
        
        # move to the next epoch
        step += 1

    # calculate (pseudo)probabilities for test subset
    pi_hat = model.test(data_loader.x_te)

    # estimate auc score and print it out        
    auc = roc_auc_score(data_loader.y_te, pi_hat)
    print("final auc %0.4f" % (auc))




if __name__ == "__main__":
    
    # define parser 
    parser = argparse.ArgumentParser(description = 
                                     textwrap.dedent("""Train function for a fully connected neural network on MNIST dataset and for a convolutional neural network on CIFAR10 dataset."""),
                                    epilog = 
                                    textwrap.dedent("""This code may be run by using the following commands:
    python3 train.py --dset cifar10 --nn_type conv --epochs 10
    python3 train.py --dset mnist --nn_type fully_con --epochs 10"""),
                                    formatter_class = argparse.RawTextHelpFormatter)

    # add the expected arguments to out parser
    # only MNIST and CIFAR10 can be used, that's why we use choices here
    parser.add_argument("--dset", choices = ["mnist", "cifar10"], help = "Dataset for model training and testing")
    
    # only fully_con and conv models can be used, that's why we use choices here
    parser.add_argument("--nn_type", choices = ["fully_con", "conv"], help = "Neural network architecture")
    
    # epochs should be an integer
    parser.add_argument("--epochs", default = 10, type = int, help = "Number of epochs for model training")
    
    # neurons should be an integer
    parser.add_argument("--neurons", default = 50, type = int, help = "Number of neurons to be used")
    
    # batch_size should be an integer
    parser.add_argument("--batch_size", default = 256, type = int, help = "Number of images to be processed during one iteration of model training")
    
    # parse the arguments so that we can pass them to train() function
    args = parser.parse_args()
    
    # call train() function using the provided inputs
    train(dset = args.dset, nn_type = args.nn_type, epochs = args.epochs, neurons = args.neurons, batch_size = args.batch_size)
