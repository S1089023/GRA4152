
## This module defines and tests 
#  a class to handle a customer loyalty marketing campaign
#


class Customer:

    """

    A class to represent a Customer in a customer loyalty marketing campaign

    Class constants:
        
        _purchasesAmountForDiscount: how much a customer needs to accomulate 
            in purchases to get a discount
        _discount: an amount of a discount

    Instance variables:

        _totalPurchases: the total amount of purchases a customer has made 
        _discountEarned: the number of times a customer has received a discount

    Public methods:

        makePurchase(amount)
            Records a new purchase.
            @param amount: an amount (in dollars) of a new purchase
            @return a tuple that contains: 
                0. an amount that a customer has paid for the last purchase
                1. the total amount of purchases a customer has made so far
                2. the total number of times a customer has received a discount

        discountReached()
            Checks whether a customer has reached a discount.
            @return Boolean (True if a discount is reached, False otherwise)

    Examples of use:

        c1 = Customer()
        c1.makePurchase(50) # returns (50, 50, 0)
        c1.makePurchase(70) # returns (60, 120, 1) since the first discount is reached
        c1.makePurchase(40) # returns (40, 160, 1) 
        c1.discountReached() # returns False since it should return True only when making
                             # a new  purchase and after accumulating $100 in purchases since the last discount
        c1.makePurchase(38) # returns (38, 198, 1) no new discount has been yet recorded, 
                            # since c1 has made purchases for less than $200 so far
        c1.makePurchase(20) # returns (10, 218, 2) since the second discount is earned now
        c1.makePurchase(80) # returns (80, 298, 2)
        c1.makePurchase(8)  # returns (0, 306, 3) a customer pays $0 as the discount 
                            # for a purchase with a price of less than $10 shouldn't exceed the price 

    """

    _purchasesAmountForDiscount = 100
    _discount = 10

    ## Constructs an object
    #
    def __init__(self):
        self._totalPurchases = 0
        self._discountsEarned = 0

    ## Records a new purchase.
    # @param amount: an amount (in dollars) of a new purchase
    # @return a tuple that contains: 
    #            0. an amount that a customer has paid for the last purchase
    #            1. the total amount of purchases a customer has made so far
    #            2. the total number of times a customer has received a discount
    #
    def makePurchase(self, amount):
        
        # increases the total amount of purchases 
        self._totalPurchases += amount

        # decreases the amount paid by discount amount if discount is reached 
        if self.discountReached():

            # keeping track of discounts earned
            self._discountsEarned += 1
            
            # if an amount of a purchase is less than a discount amount when a discount is reached,
            # the purchase is free for a customer 
            if amount < Customer._discount:
                amount = 0
            
            else:
                amount -= Customer._discount

        # print amount paid to a user
        print("You paid ${} this time.".format(amount))

        return (amount, self._totalPurchases, self._discountsEarned)
        
    ## Checks whether a customer has reached a discount.
    #  @return Boolean (True if a discount is reached, False otherwise)
    def discountReached(self):
        
        # checks whether the accoumulated amount is equal or larger than
        purhasesSinceLastDiscount = (self._totalPurchases - self._discountsEarned * Customer._purchasesAmountForDiscount) 
            
        return (purhasesSinceLastDiscount >= Customer._purchasesAmountForDiscount)
    

## the following code tests Customer class 
#

if __name__ == "__main__":
    c1 = Customer()
    assert c1.makePurchase(50) == (50, 50, 0)
    assert c1.makePurchase(70) == (60, 120, 1)
    assert c1.makePurchase(40) == (40, 160, 1)
    assert c1.discountReached() == False
    assert c1.makePurchase(38) == (38, 198, 1)
    assert c1.makePurchase(20) == (10, 218, 2)
    assert c1.makePurchase(80) == (80, 298, 2)
    assert c1.makePurchase(8) == (0, 306, 3)
