
## This script contains Classes Animal, Cat, Dog, and Bigdog
#  It also contains the tester function for all classes and explanations of usage 
#  of inheritance, overriding, and polymorphism
#

class Animal:

    """

    An abstract class to represent an animal

    Instance variables:

        _name: name of an animal

    Public methods:

        greets()
            Abstract method. Should be implemented in subclasses to
            include greetings of animals.
            
        summary()
            Prints animal's name and calls greets() method.

    Examples of use:
    
        animal = Animal("Alpha")
        # Calling any of the public methods should result in NotImplementedError

    """

    ## Constructs an object and creates instance variable name
    # @param name: name of an animal
    #
    def __init__(self, name):
        self._name = name


    ## Abstract method for greeting
    #
    def greets(self):
        raise NotImplementedError
    

    ## Prints animal's name and calls greets() method
    #
    def summary(self):
        print(self._name)
        self.greets()




class Cat(Animal):

    """

    A class to represent a cat with a name and greeting.

    Instance variables:
    
        _name: cat's name. This variable is inherited from Animal superclass
               after calling the constructor method of the superclass.

    Public methods:

        greets() 
            This method is overridden in this subclass. Its name and parameter (self)
            were specified in the superclass, but in the subclass it is overridden
            so as to include printing out "meow".

        summary()
            Inherited from Animal superclass.
    
    Examples of use:

        cat = Cat("Bravo")
        cat.summary()
        print("Expected output:")
        print("Bravo")
        print("meow")

    """


    ## Constructs an object and creates instance variable name
    # @param name: name of a cat
    #
    def __init__(self, name):
        # Calling constructor of the superclass (Animal)
        super().__init__(name)


    ## Greeting of a cat. Here I'm using overriding to change the behaviour of 
    #  greets() method inherited from Animal superclass
    # 
    def greets(self):
        print("meow")




class Dog(Animal):

    """

    A class to represent a dog with a name and greeting

    Instance variables:
    
        _name: dog's name. This variable is inherited from Animal superclass
               after calling the constructor method of the superclass 

    Public methods:

        greets() 
            This method is overridden in this subclass. Its name and parameter (self)
            were specified in the superclass, but in the subclass it is overridden
            so as to include printing out "woof".

        summary()
            Inherited from Animal superclass.

    Examples of use:

        dog = Dog("Charlie")
        dog.summary()
        print("Expected output:")
        print("Charlie")
        print("woof")

    """


    ## Constructs an object and creates and instance variable name
    #  @param name: name of a dog
    #
    def __init__(self, name):
        # Calling constructor of the superclass (Animal)
        super().__init__(name)


    ## Greeting of a dog. Here I'm using overriding to change the behaviour of 
    #  greets() method inherited from Animal superclass
    #
    def greets(self):
        print("woof")




class BigDog(Dog):

    """

    A class to represent a big dog with a name and greeting

    Instance variables:
    
        _name: dog's name. This variable is inherited from Dog superclass
               after calling the constructor method of the class Dog (and is essentially
               inherited from Animal superclass, because in the constructor method of the 
               class Dog the constructor of the class Animal is called)

    Public methods:

        greets() 
            This method is overridden in this subclass. Firstly, it calls the 
            greets() method of the superclass (Dog) and "woof" if printed, then it prints
            "woooof" so as to complete the behaviour of this method of any BigDog object.

        summary()
            Inherited from Dog superclass (and in Dog superclass it was inherited from
            Animal superclass).

    Examples of use:
        
        bigdog = BigDog("Delta")
        bigdog.summary()
        print("Expected output:")
        print("Delta")
        print("woof")
        print("woooof")

    """

    ## Constructs an object and creates instance variable name
    #  @param name: name of a big dog
    #
    def __init__(self, name):
        # Calling constructor of the superclass (Dog)
        super().__init__(name)


    ## Greeting of a big dog. As the first step, I'm calling the greets() method
    #  of the superclass (Dog). After that, I'm further developing the method
    #  by including another "woooof".
    #
    def greets(self):
        # inheriting method from the superclass
        super().greets()
        # overriding the method to extend its behaviour
        print("woooof")




if __name__ == "__main__":

    # create an object of Animal class
    animal = Animal("Alpha")
    
    try:
        # name of the animal should be printed first
        # after that there should be NotImplementedError
        # becauase greets() method is abstract in Animal class
        animal.summary()
    except NotImplementedError:
        print("Abstract class Animal was tested successfully\n")

    # create an object of Cat class 
    cat = Cat("Bravo")
    print("Testing Class Cat:")

    # Here I'm using inheritance, because summmary() method was 
    # only developed in Animal class. Cat class inherits summary()
    # method allowing me to call it on an object of Cat class here
    cat.summary()
    print("Expected output:")
    print("Bravo")
    print("meow")

    # create an object of Dog class 
    dog = Dog("Charlie")
    print("\nTesting Class Dog")

    # Here I'm using inheritance, because summmary() method was 
    # only developed in Animal class. Dog class inherits summary()
    # method allowing me to call it on an object of Dog class here
    dog.summary()
    print("Expected output:")
    print("Charlie")
    print("woof")

    # create an object of BigDog class
    bigdog = BigDog("Delta")
    print("\nTesting Class BigDog:")

    # Here I'm using inheritance, because summary() method was only
    # developed in Animal class. BigDog class inherits summary() method from 
    # Dog class, which in its turn has inherited it from Animal class. 
    bigdog.summary()
    print("Expected output:")
    print("Delta")
    print("woof")
    print("woooof")
    
    
    # Here I am using polymophism. I have three objects of different classes which 
    # all inherit from the same superclass. All of them have inherited summary() method
    # from Animal class, but summary() method calls greets() method which has different 
    # implementation in all three classes. Nevertheless, by calling the same method 
    # in the for loop below each time I use an implementation of the greets() method 
    # that correspond to the object on which I call the method. In this way I'm using
    # dynamic method lookup, i.e. polymorphism.
    print("\n" + "-" * 20)
    print("Using polymorphism:")
    for obj in [cat, dog, bigdog]:
        obj.summary()
