
## This module defines and tests Message class
#


class Message:

    """
    
    A class to represent a model of an e-mail message
    
    Class variables:

        _no_messages: a number of messages created
        _log: a dictionary of messages created with senders' names being 
            keys in the dictionary, and each value containing a separate
            dictionary with the keys being recipients' names and values - 
            messages' bodies 

    Instance variables:

        _sender: sender's name
        _receipent: recipient's name
        _messageBody: the message of body

    Public methods:

        append(text)
            Adds a line of text to the message body.
            @param text: a line of text

        toString()
            Makes a message into one long string.
            @return a string with the formatted message

        log_messages()
            Keeps track of the number of messages and saves a log of messages sent.

    Examples of use:

        # creating a message from 'Harry Morgan' to 'Rudolf Reindeer'
        m1 = Message('Harry Morgan', 'Rudolf Reindeer') 

        # appending a message body to the message
        m1.append('Greetings! How are you?')

        # converting a message into one string
        m1.toString() # returns the following string:
                      # 'From: Harry Morgan\nTo: Rudolf Reindeer\nGreetings! How are you?'

    """

    _no_messages = 0
    _log = {}

    ## Constructs an object
    #  
    def __init__(self, sender, recipient):
        
        # creating instance variables
        self._sender = sender
        self._recipient = recipient
        self._messageBody = ""        

    ## Adds a line of text to the message body.
    # @param text: a line of text
    # 
    def append(self, text):
        self._messageBody = self._messageBody + text
        
        # invoke log_messages 
        self.log_messages()

    ## Makes a message into one long string.
    # @return a string with the formatted message
    # 
    def toString(self):
        return f"From: {self._sender}\nTo: {self._recipient}\n" + self._messageBody
    

    ## Keeps track of the number of messages and saves a log of messages sent.
    #  
    def log_messages(self):

        # increments the number of messages
        Message._no_messages += 1
        
        # creates a dictionary for logging messages of a new sender 
        if self._sender not in Message._log:
            Message._log[self._sender] = {}
        
        # logs a new message body
        Message._log[self._sender][self._recipient] = self._messageBody
        


## the following code tests Message Class
#

if __name__ == "__main__":

    # create two separate instances 
    m1 = Message('Harry Morgan', 'Rudolf Reindeer')
    m2 = Message('John Doe', 'Ann Smith')


    # append messages and trigger log_messages two times
    m1.append('Greetings! How are you?')
    m2.append('Hi! Where are you')

    # checks toString() method
    assert m1.toString() == 'From: Harry Morgan\nTo: Rudolf Reindeer\nGreetings! How are you?'

    # there were two messages appended 
    assert Message._no_messages == 2
    # and they should be stored in a nested dictionary
    assert Message._log == {'Harry Morgan': {'Rudolf Reindeer': 'Greetings! How are you?'},
                           'John Doe': {'Ann Smith': 'Hi! Where are you'}}
    
    # adding a third message
    m3 = Message('Rudolf Reindeer', 'Harry Morgan')
    
    m3.append('Greetings! I am fine')
    assert Message._no_messages == 3

    # there should be one more sender in a dictionary used for logging now 
    assert Message._log == {'Harry Morgan': {'Rudolf Reindeer': 'Greetings! How are you?'},
                           'John Doe': {'Ann Smith': 'Hi! Where are you'},
                           'Rudolf Reindeer': {'Harry Morgan': 'Greetings! I am fine'}}
    
    m4 = Message("John Doe", "Harry Morgan")
    m4.append("Hi, Harry! Have you seen Ann?")

    assert Message._no_messages == 4

    # we are now extending the dictionary for 'John Doe' by one more key-value pair
    assert Message._log == {'Harry Morgan': {'Rudolf Reindeer': 'Greetings! How are you?'},
                           'John Doe': {'Ann Smith': 'Hi! Where are you',
                                        #  new recepient added for John Doe
                                        'Harry Morgan': 'Hi, Harry! Have you seen Ann?'},
                           'Rudolf Reindeer': {'Harry Morgan': 'Greetings! I am fine'}}
    
    # even though m4 had the same sender and recepient, we need to
    # create a new object as it is another email
    m5 = Message("John Doe", "Harry Morgan")
    m5.append("By the way, how are you?")

    assert Message._no_messages == 5
    assert Message._log == {'Harry Morgan': {'Rudolf Reindeer': 'Greetings! How are you?'},
                           'John Doe': {'Ann Smith': 'Hi! Where are you',
                                        # the previous message was replaced with a new one
                                        # this is in line with the description of the task as 
                                        # we should have senders as the keys of outer dictionary
                                        # and recipients as the keys of inner dictionary
                                        # thus we cannot store more than one message for each
                                        # sender-recipient pair 
                                        # this is a limitation of the current logging approach
                                        'Harry Morgan': 'By the way, how are you?'},
                           'Rudolf Reindeer': {'Harry Morgan': 'Greetings! I am fine'}}
