def multiplyDigits(number):
    mult = 1
    while number != 1:
        mult *= number % 10
        number = number // 10
    return mult


def calculateFirstNumber(startingDigits):
    return 10**(startingDigits - 1)
    
    
def validNumberOfDigits(digits):
    return digits > 1


def numberOfDigits(number):
    digits = 1
    while number > 1:
        digits += 1
        number = number // 10
    return digits


def multiplicativePersistence(startingDigits=1, maxDigits=10, endGoal=None):
    currentNumber = calculateFirstNumber(startingDigits)
    
    def _multiplicativePersistence(currentNumber, maxPersistance, maxDigits):
        
        print(f'current number {currentNumber}')
        print(f'digits {numberOfDigits(currentNumber)}')
        print(f'max {maxPersistance}')
        
        if validNumberOfDigits(numberOfDigits(currentNumber)):
            
            return _multiplicativePersistence(multiplyDigits(currentNumber), maxPersistance + 1)
        else:
            return maxPersistance
        
    return _multiplicativePersistence(currentNumber, 0)
        
        
print(f'Multiplicative Persistence: {multiplicativePersistence()}')
        