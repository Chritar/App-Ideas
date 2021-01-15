# Die Funktion testet ob die Laenge des Inputstrings groeßer als 8 ist

def lengthCheck(str):

    return True if len(str) <= 8 else print('Dude. No more than 8 numbers!')

# Die Funktion testet ob der Inhalt des Inputstrings aus 0 uns 1 besteht

def binaryCheck(str):

    for i in range(len(str)):
        if int(str[i]) != 0 and int(str[i]) != 1: return False
        else: continue
    return True

# Die Funktion gibt den String rueckwarts aus, um die Rechnung der Exponenten korrekt darzustellen

def reverseString(str):
    return str[::-1]


print('Binary to Decimal Converter')
print('you can add up to 8 numbers, those have to be either 1 or 0')

binaryString = input('')

decimal = 0
exponent = 0

if lengthCheck(binaryString) and binaryCheck(binaryString):

    #print(binaryString)
    binaryString = reverseString(binaryString)
    #print(binaryString)

    #print(lengthCheck(binaryString))
    #print(binaryCheck(binaryString))

    for i in range(len(binaryString)):
        decimal += int(binaryString[i])*2**exponent
        exponent += 1

    
    print(binaryString, "entspricht dezimal", decimal)




        