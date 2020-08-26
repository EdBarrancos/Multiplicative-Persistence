# ALso check multiplicative digital root

from digitManipulation import *

def calculateFirstNumber(startingDigits): return 10**(startingDigits - 1)

    
def multiplicativePersistence(number):
    def _multiplicativePersistence(number, maxPersistance):
        
        print( number)
        
        if validNumberOfDigits(numberOfDigits(number)): 
            return _multiplicativePersistence(multiplyDigits(number), maxPersistance + 1)
        else: return maxPersistance
        
    return _multiplicativePersistence(number, 0)