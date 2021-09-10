# Convert Roman Numeral to Decimal
def RomanToDecimal(input_roman = str):
    #word_array=input_roman.split('')
    decimal_number=0
    print(input_roman)
    for i in range(len(input_roman)-1):
        if (input_roman[i] == 'I'):
            if(i==len(input_roman) - 1):
                decimal_number = decimal_number + 1
            elif(input_roman[i+1] != 'V' or input_roman[i+1] != 'X'):
                decimal_number = decimal_number + 1
            elif(input_roman[i+1] == 'V'):
                decimal_number = decimal_number + 4
                i = i + 1
            elif(input_roman[i+1] == 'X'):
                decimal_number = decimal_number + 9
                i = i+1
        elif (input_roman[i] == 'X'):
            if(i==len(input_roman) - 1):
                decimal_number = decimal_number + 10
            elif(input_roman[i+1] != 'L' or input_roman[i+1] != 'C'):
                decimal_number = decimal_number + 1
            elif(input_roman[i+1] == 'L'):
                decimal_number = decimal_number + 40
                i = i + 1
            elif(input_roman[i+1] == 'C'):
                decimal_number = decimal_number + 90
                i = i + 1
        elif (input_roman[i] == 'C'):
            if(i==len(input_roman) - 1):
                decimal_number = decimal_number + 10
            elif(input_roman[i+1] != 'D' or input_roman[i+1] != 'M'):
                decimal_number = decimal_number + 1
            elif(input_roman[i+1] == 'D'):
                decimal_number = decimal_number + 400
                i = i + 1
            elif(input_roman[i+1] == 'M'):
                decimal_number = decimal_number + 900
                i = i + 1
        elif(input_roman[i] == 'V'):
            decimal_number = decimal_number + 5
        elif(input_roman[i] == 'L'):
            decimal_number = decimal_number + 50
        elif(input_roman[i] == 'D'):
            decimal_number = decimal_number + 500
        elif(input_roman[i] == 'M'):
            decimal_number = decimal_number + 1000
                #decimal_number = decimal_number + 5
        #elif (i == 'X'):
            #decimal_number = decimal_number + 10
        #elif (i == 'L'):
            #decimal_number = decimal_number + 50
        #elif (i == 'C'):
            #decimal_number = decimal_number + 100
        #elif (i == 'D'):
            #decimal_number = decimal_number + 500
        #elif (i == 'M'):
            #decimal_number = decimal_number + 1000
    print(decimal_number)
    return decimal_number, len(input_roman)


#RomanToDecimal('MMDCCCLXXIX')



# Convert decimal to Minimal Roman Numeral

def ToRoman(input_decimal = int):
    next_decimal = input_decimal
    Count_M = int(next_decimal/1000)
    print(Count_M)
    # if Count_M >= 1
    next_decimal = next_decimal%1000
    Count_D = int(next_decimal/500)
    print(Count_D)
    # if Count_D >= 1:
    next_decimal = next_decimal%500
    Count_C = int(next_decimal/100)
    print(Count_C)
    if Count_C == 9:
        Count_CM = 1
        Count_C = 0
    if Count_C == 4:
        Count_CD = 1
        Count_C = 0
    next_decimal = next_decimal % 100
    Count_L = int(next_decimal / 50)
    print(Count_L)
    # if Count_L >= 1:
    next_decimal = next_decimal % 50
    Count_X = int(next_decimal / 10)
    if Count_X == 9:
        Count_XC = 1
        Count_X = 0
    if Count_X == 4:
        Count_XL = 1
        Count_X = 0
    print(Count_X)
    # if Count_X >= 1:
    next_decimal = next_decimal % 10
    Count_V = int(next_decimal / 5)
    print(Count_V)
    # if Count_V >= 1:
    next_decimal = next_decimal % 5
    Count_I = int(next_decimal / 1)
    if Count_I == 9:
        Count_IX = 1
        Count_I = 0
    if Count_I == 4:
        Count_IV = 1
        Count_I = 0
    print(Count_I)
    # if Count_I >= 1:
    Min_String_normal = 'M'*Count_M + 'D'*Count_D + 'CM'*Count_CM + 'CD'*Count_CD +'C'*Count_C+ 'L'*Count_L +'XC'*Count_XC+ 'XL'*Count_XL + 'X'*Count_X + 'IV'*Count_IV+ 'IX'*Count_IX+'V'*Count_V + 'I'*Count_I
    Min_String_length = len(Min_String_normal)
    print(Min_String_normal)
    print(Min_String_length)
    return Min_String_normal, Min_String_length





















filename = 'roman_number.txt'
with open(filename, 'r') as input_file:
    for line in input_file.readlines():

        input_roman = line.strip()
        input_decimal = RomanToDecimal(input_roman)
        roman = ToRoman(input_decimal)


