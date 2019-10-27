# -*-coding: utf-8 -*
import sys

def partToLetter(part):
    if part == 0:
        return(['I', 'V', 'X'])
    elif part == 10:
        return(['X', 'L', 'C'])
    else:
        return(['C', 'D', 'M'])

def convertToLetter(n, part):
    partVec = partToLetter(part)
    if n < 4:
        result = n * partVec[0]
    elif n == 4:
        result = partVec[0] + partVec[1]
    elif n == 5:
        result = partVec[1]
    elif n > 5 and n < 9:
        result = partVec[1] + (n-5) * partVec[0]
    else:
        result = partVec[0] + partVec[2]
    return(result)

def convertNumberToRomanNumber(n):

    result = ""
    if n > 999:
        result = int(str(n)[0])*'M'
        n -= int(str(n)[0]) * 1000
    if n > 99:
        nTemp = int(str(n)[0])
        result += convertToLetter(nTemp, part=100)
        n -= int(str(n)[0]) * 100
    if n > 9:
        nTemp = int(str(n)[0])
        result += convertToLetter(nTemp, part=10)
        n -= int(str(n)[0]) * 10
    if n > 0:
        result += convertToLetter(n, part=0)
    return(result)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print('Error input : use only one argument')
    elif len(sys.argv) == 1:
        print('Error input : must enter only one argument')
    else:
        try:
            n = int(sys.argv[1])
            if n < 0 or n > 3999:
                print('Error input : int must be between 1 and 3999')
            else:
                result = convertNumberToRomanNumber(n)
                print(result)
        except ValueError as v:
            print('Error input : must enter int as argument')
