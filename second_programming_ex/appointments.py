
## This script contains Classes Appointment, Onetime, Daily, and Monthly.
#  It also contains the tester function for all classes, 
#  and my explanations for the parts for which the explanations were required
#  by the task description
#


class Appointment:
    
    """
    
    An abstract class to represent an appointment

    Instance variables:

        _description: description of an appointment. Default value = None.
        _year: year of an appointment. Default value = None.
        _month: month of an appointment. Default value = None.
        _day: day of an appointment. Default value = None.

    Public methods:

        occursOn(year, month, day)
            Abstract method. Should be developed in all subclasses to inlcude a
            test of whether the appointment occurs on a specified date.  
            @param year: year of the date that is tested.
            @param month: month of the date that is tested.
            @param day: day of the date that is tested.
    
        save(path)
            Saves the type, description, year, month, and day of an appointment to a file
            @param path: path to a file where the data should be saved

        load(path)
            Loads the type, description, year, month, and day of an appointment from a file
            @param path: path to a file where the data is stored

    Examples of use:

        a1 = Appointment("Abstract Appointment", 2023, 11, 7)
        # This class containt abstract methods. Therefore it is expected that 
        # it will not be used to create objects that are going to be used elsewhere

    """


    ## Constructs an object and creates instance variables
    #  @param description: description of an appointment. Default value = None.
    #  @param year: year of an appointment. Default value = None.
    #  @param month: month of an appointment. Default value = None.
    #  @param day: day of an appointment. Default value = None.
    #
    def __init__(self, description = None, year = None, month = None, day = None):

        # Each parameter has a default value of None so that any appointment 
        # can be created empty and have data loaded into it after instantiation 
        self._description = description
        self._year = year
        self._month = month
        self._day = day


    ## Abstract method. Should be developed in all subclasses to inlcude a
    #  test of whether the appointment occurs on a specified date. 
    #  @param year: year of the date that is tested.
    #  @param month: month of the date that is tested.
    #  @param day: day of the date that is tested.
    #
    def occursOn(self, year, month, day):
        raise NotImplementedError
    

    ## Saves the type, description, year, month, and day of an appointment to a file
    #  @param path: path to a file where the data should be saved
    # 
    def save(self, path):

        # open a file in the writing mode using the provided path
        with open(path, "w") as f:

            # for each element that is intended to be saved to a file
            for line in [str(type(self)), 
                         self._description,
                         str(self._year),
                         str(self._month),
                         str(self._day)]:
                
                # write an element to a file and add a newline
                f.write(line)
                f.write("\n")
    

    ## Loads the type, description, year, month, and day of an appointment from a file
    #  @param path: path to a file where the data is stored
    #
    def load(self, path):

        # open a file in the reading mode using the provided path
        with open(path, "r") as f:

            # read all the lines that were saved previously and assign 
            # the loaded data to the corresponding instance variables

            # type is not used in the execution, but it is nice to have it in a 
            # file with an appointment
            appointment_type = f.readline() 
            self._description = f.readline()
            self._year = int(f.readline())
            self._month = int(f.readline())
            self._day = int(f.readline())




class Onetime(Appointment):

    """

    A class to represent a one time appointment.

    Instance variables:

        All instrance variables are inherited from Appointment superclass.
        
        Each parameter has a default value of None so that any one time appointment 
        can be created empty and have data loaded into it after instantiation  

        The meaning of _year, _month, _day in this class is modified so that
        they correspond to a particular date for which a one time appointment is 
        scheduled. This was not specified in the superclass.

    Public methods:

        occursOn(year, month, day)
            This method is overridden in this subclass. Checks whether the appointment is 
            scheduled exactly for the date that is provided to the method.
            @param year: year of the date that is tested.
            @param month: month of the date that is tested.
            @param day: day of the date that is tested.
            @return Boolean (True if an appointment occurs on the provided date, False otherwise)

        save(path)
            Inherited from Appointment superclass

        load(path)
            Inherited from Appointment superclass

    Examples of use:

        o1 = Onetime("Visit the doctor", 2023, 12, 1)
        o1.occursOn(2023, 12, 12) # returns False
        o1.occursOn(2023, 8, 29)  # returns False
        o1.occursOn(2022, 7, 18)  # returns False
        o1.occursOn(2023, 12, 1)  # returns True
        print(o1) # prints "One time appointment. Date: 1-12-2023. Description: Visit the doctor"
        o1.save("second_programming_ex/onetime_0.txt") # saves appointment data to a file 
        o2 = Onetime() # creates empty one time appointment
        
        # now I fill the created empty appointment with the data loaded from a file
        o2.load("second_programming_ex/onetime_0.txt") 

    """


    ## Constructs an object and creates instance variables
    #  @param description: description of an appointment. Default value = None.
    #  @param year: year of an appointment. Default value = None.
    #  @param month: month of an appointment. Default value = None.
    #  @param day: day of an appointment. Default value = None.
    #
    def __init__(self, description = None, year = None, month = None, day = None):

        # calls the constructor method of the superclass 
        super().__init__(description, year, month, day)


    ## This method is overridden in this subclass. Checks whether the appointment is 
    #  scheduled exactly for the date that is provided to the method.
    #  @param year: year of the date that is tested.
    #  @param month: month of the date that is tested.
    #  @param day: day of the date that is tested.
    #
    def occursOn(self, year, month, day):

        ## the provided year, month, and day should match the corresponding intance
        #  variables exactly
        # 
        if (self._year == year) and (self._month == month) and (self._day == day):
            return True
        else:
            return False 


    ## Overridden in-build method __repr__ with a string representation of 
    #  one time appointment objects
    # 
    def __repr__(self):
        return 'One time appointment. Date: {}-{}-{}. Description: {}'.format(self._day, 
                                                         self._month,
                                                         self._year,
                                                         self._description)




class Daily(Appointment):

    """

    A class to represent a daily appointment.
    
    Instance variables:

        All instrance variables are inherited from Appointment superclass.
        
        Each parameter has a default value of None so that any daily appointment 
        can be created empty and have data loaded into it after instantiation  

        The meaning of _year, _month, _day in this class is modified so that
        they correspond to the date when this daily appointment starts. 
        This was not specified in the superclass.

    Public methods:

        occursOn(year, month, day)
            This method is overridden in this subclass. Checks whether an appointment 
            occurs on the provided date, i.e. whether the provided date is greater than 
            or equal to the date when an appointment starts
            @param year: year of the date that is tested.
            @param month: month of the date that is tested.
            @param day: day of the date that is tested.
            @return Boolean (True if an appointment occurs on the provided date, False otherwise)

        save(path)
            Inherited from Appointment superclass

        load(path)
            Inherited from Appointment superclass

    Examples of use:

        d1 = Daily("Wake up", 2023, 1, 1)
        d1.occursOn(2024, 12, 8)  # returns True
        d1.occursOn(2023, 8, 5)   # returns True
        d1.occursOn(2023, 1, 12)  # returns True
        d1.occursOn(2022, 12, 12) # returns False
        print(d1) # prints "Daily time appointment starting 1-1-2023. Description: Wake up"
        d1.save("second_programming_ex/daily_0.txt")
        d2 = Daily() # creates empty daily appointment
        
        # now I fill the created empty appointment with the data loaded from a file
        d2.load("second_programming_ex/daily_0.txt")

    """


    ## Constructs an object and creates instance variables
    #  @param description: description of an appointment. Default value = None.
    #  @param year: the year in which an appointment starts. Default value = None.
    #  @param month: the month in which an appointment starts. Default value = None.
    #  @param day: the day in which an appointment starts. Default value = None.
    #
    def __init__(self, description = None, year = None, month = None, day = None):

        # calls the constructor method of the superclass 
        super().__init__(description, year, month, day)


    ## This method is overridden in this subclass. Checks whether an appointment 
    #  occurs on the provided date, i.e. whether the provided date is greater than 
    #  or equal to the date when an appointment starts
    #  @param year: year of the date that is tested.
    #  @param month: month of the date that is tested.
    #  @param day: day of the date that is tested.
    #
    def occursOn(self, year, month, day):
        
        ## in case if the provided year is higher than 
        #  the corresponding intance variable, an appointment 
        #  definitely occurs on the provided date 
        #  
        if self._year < year:
            return True
        
        ## if the year is the same, than we should should check the month
        #  if the month is higher, then an appointment occurs on the provided date
        #
        elif self._year == year:
            if self._month < month:
                return True

            ## if the provided year and the provided months are equal to the 
            #  corresponding instance variables, the provided day should be 
            #  at least as high as the corresponding instance variable
            #  
            elif self._month == month:
                if self._day <= day:
                    return True
        
        ## if none of the condions above resulted in "return True" statement,
        #  an appointment doesn't oocur on the provided date
        #        
        return False
    

    ## Overridden in-build method __repr__ with a string representation of 
    #  daily appointment objects
    # 
    def __repr__(self):
        return 'Daily time appointment starting {}-{}-{}. Description: {}'.format(self._day,
                                                                    self._month,
                                                                    self._year,
                                                                    self._description)
    
    


class Monthly(Appointment):

    """

    A class to represent a monthly appointment

    Instance variables:

        All instrance variables are inherited from Appointment superclass.
        
        Each parameter has a default value of None so that any monthly appointment 
        can be created empty and have data loaded into it after instantiation  

        The meaning of _year, _month, _day in this class is modified so that
        they correspond to the date when this monthly appointment starts. 
        This was not specified in the superclass.

    Public methods:

        occursOn(year, month, day)
            This method is overridden in this subclass. Checks whether an appointment 
            occurs on the provided date, i.e. whether the provided date is greater than 
            or equal to the date when an appointment starts and whether the provided
            day of the month is the same as the corresponding instance variable
            @param year: year of the date that is tested.
            @param month: month of the date that is tested.
            @param day: day of the date that is tested.
            @return Boolean (True if an appointment occurs on the provided date, False otherwise)

        save(path)
            Inherited from Appointment superclass

        load(path)
            Inherited from Appointment superclass

    Examples of use:

        m1 = Monthly("Check your financial position", 2023, 9, 1)
        m1.occursOn(2022, 12, 28) # returns False
        m1.occursOn(2023, 8, 1)   # returns False
        m1.occursOn(2023, 10, 1)  # returns True
        m1.occursOn(2023, 11, 1)  # returns True
        m1.occursOn(2024, 1, 10)  # returns False
        print(m1) # prints "Monthly time appointment starting 1-9-2023. Description: Check your financial position"
        m1.save("second_programming_ex/monthly_0.txt")
        m2 = Monthly() # creates empty monthly appointment
        
        # now I fill the created empty appointment with the data loaded from a file
        m2.load("second_programming_ex/monthly_0.txt")

    """


    ## Constructs an object and creates instance variables
    #  @param description: description of an appointment. Default value = None.
    #  @param year: the year in which an appointment starts. Default value = None.
    #  @param month: the month in which an appointment starts. Default value = None.
    #  @param day: the day in which an appointment starts. Default value = None.
    #
    def __init__(self, description = None, year = None, month = None, day = None):

        # calls the constructor method of the superclass 
        super().__init__(description, year, month, day)


    ## This method is overridden in this subclass. Checks whether an appointment 
    #  occurs on the provided date, i.e. whether the provided date is greater than 
    #  or equal to the date when an appointment starts and whether the provided
    #  day of the month is the same as the corresponding instance variable
    #  @param year: year of the date that is tested.
    #  @param month: month of the date that is tested.
    #  @param day: day of the date that is tested.
    #
    def occursOn(self, year, month, day):

        ## if the provided year is higher than the corresponding instance variable
        #  and the day of the month is the same, an appointment occurs on the provided date 
        #
        if self._year < year and self._day == day:
            return True
        
        ## if the provided year is the same as the corresponding instance variable,
        #  the month is at least as high as the correposnding instance variable,
        #  and the day of the month is the same as the corresponding instance variable,
        #  then an appointment occurs on the provided date
        #
        elif self._year == year and self._month <= month and self._day == day:
            return True
        
        ## In all other cases, an appointment doesn't occur on the provided date
        #
        else:
            return False
    
        
    ## Overridden in-build method __repr__ with a string representation of 
    #  monthly appointment objects
    #
    def __repr__(self):
        return 'Monthly time appointment starting {}-{}-{}. Description: {}'.format(self._day,
                                                                      self._month,
                                                                      self._year,
                                                                      self._description)




if __name__ == "__main__":

    # create several appointments of different classes
    a1 = Appointment("Abstract Appointment", 2023, 11, 7)
    o1 = Onetime("Visit the doctor", 2023, 12, 1)
    d1 = Daily("Wake up", 2023, 1, 1)
    m1 = Monthly("Check your financial position", 2023, 9, 1)

    # checking occursOn() method implementation for one time appointments
    assert o1.occursOn(2023, 12, 12) == False  # wrong day
    assert o1.occursOn(2023, 8, 29) == False   # wrong month and day
    assert o1.occursOn(2022, 7, 18) == False   # wrong year, month, and day 
    assert o1.occursOn(2023, 12, 1) == True    # correct

    # checking occursOn() method implementation for daily appointments
    assert d1.occursOn(2024, 12, 8) == True    # occurs after 2023-1-1 
    assert d1.occursOn(2023, 8, 5) == True     # occurs after 2023-1-1
    assert d1.occursOn(2023, 1, 12) == True    # occurs after 2023-1-1
    assert d1.occursOn(2022, 12, 12) == False  # occurs before 2023-1-1

    # checking occursOn() method implementation for monthly appointments
    assert m1.occursOn(2022, 12, 28) == False  # occurs before 2023-9-1
    assert m1.occursOn(2023, 8, 1) == False    # occurs before 2023-9-1
    assert m1.occursOn(2023, 10, 1) == True    # occurs after 2023-9-1 and on the first day of the month
    assert m1.occursOn(2023, 11, 1) == True    # occurs after 2023-9-1 and on the first day of the month
    assert m1.occursOn(2024, 1, 10) == False   # occurs after 2023-9-1, but not on the first day of the month

    # checking string representations 
    assert o1.__repr__() == "One time appointment. Date: 1-12-2023. Description: Visit the doctor"
    assert d1.__repr__() == "Daily time appointment starting 1-1-2023. Description: Wake up"
    assert m1.__repr__() == "Monthly time appointment starting 1-9-2023. Description: Check your financial position"

    # saving three appointments to .txt files
    o1.save("second_programming_ex/onetime_0.txt")
    d1.save("second_programming_ex/daily_0.txt")
    m1.save("second_programming_ex/monthly_0.txt")
    
    # asking a user to determine a type of appointment to be loaded 
    appointment = input("Choose (type):\n0. Onetime\n1. Daily\n2. Monthly\n")
    
    # asking a user for a path to a file with appointment data
    appointmentPath = input("Type path:\n")

    # there are three options
    choices = [Onetime, Daily, Monthly]

    try:
        # create empty object of the chosen type
        obj = choices[int(appointment)]()
        
        # load data to the appointment object of the specified type
        obj.load(appointmentPath)

        # print string representation of the created object
        print(obj)

    ## checking input for different types of errors 
    #  and providing appropriate feedback to a user
    #
    except TypeError:
        print("Wrong type of input")
    except ValueError:
        print("Wrong value chosen for input")
    except IndexError:
        print("Index out of range")
    except FileNotFoundError:
        print("Wrong path")


"""

We could use a polymorphic approach for the save() method in the following way:
Instead of inheriting the same implementation of save() method, it could be
overridden in each subclass so that the filenames of appointments of different types
would include a certain default beginning line (for example, default filename 
for daily appointment could start with "daily_" which would be stored as a Class 
constant). The filenames could also be modified to include a counter of saved 
appointments of the corresponding type (we would have to include a corresponding 
Class variable in each Class). 

Polymorphism in such settings would manifest itself when we would develop a script
to save several appointments with just the following syntax:

for a in listOfAppointmentsOfDifferentTypes:
    a.save()

And each appointment would be saved with a different filename that would show its type 
and sequence number. 

This approach differs from the approach in the question number 2 in a way that we don't have
to provide filenames to each of the appointments that we save. They would be created automatically 
and differently for each type of appointment as dynamic method lookup would be used.

"""