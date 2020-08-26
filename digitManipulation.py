def multiplyDigits(number):
    mult = 1
    while thereAreStillDigits(number):
        mult *= getMostSignificatDigit(number)
        number = shiftRight(number)
    return mult

def thereAreStillDigits(number): return number != 0

def getMostSignificatDigit(number): return number % 10

def shiftRight(number): return number // 10

def numberOfDigits(number):
    digits = 0
    while thereAreStillDigits(number):
        digits += 1
        number = shiftRight(number)
    return digits


def validNumberOfDigits(digits): return digits > 1
