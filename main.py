# Convert non-minimal Roman Numeral to Decimal
def RomanToDecimal(input_roman = str):
    #word_array=input_roman.split('')
    decimal_number=0
    print(input_roman)
    for i in input_roman:
        if (i == 'I'):
            decimal_number = decimal_number + 1
        elif (i == 'V'):
            decimal_number = decimal_number + 5
        elif (i == 'X'):
            decimal_number = decimal_number + 10
        elif (i == 'L'):
            decimal_number = decimal_number + 50
        elif (i == 'C'):
            decimal_number = decimal_number + 100
        elif (i == 'D'):
            decimal_number = decimal_number + 500
        elif (i == 'M'):
            decimal_number = decimal_number + 1000

    print(decimal_number)



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

    next_decimal = next_decimal % 100
    Count_L = int(next_decimal / 50)
    print(Count_L)
    # if Count_L >= 1:
    next_decimal = next_decimal % 50
    Count_X = int(next_decimal / 10)
    print(Count_X)
    # if Count_X >= 1:
    next_decimal = next_decimal % 10
    Count_V = int(next_decimal / 5)
    print(Count_V)
    # if Count_V >= 1:
    next_decimal = next_decimal % 5
    Count_I = int(next_decimal / 1)
    print(Count_I)
    # if Count_I >= 1:
    Min_String_normal = 'M'*Count_M + 'D'*Count_D + 'C'*Count_C+ 'L'*Count_L + 'X'*Count_X + 'V'*Count_V + 'I'*Count_I

    Min_String_length = len(Min_String_normal)
    print(Min_String_normal)
    print(Min_String_length)
    return [Min_String_length, Min_String_normal]





















#path = f'code{os.sep}files{os.sep}text{os.sep}'
filename = 'roman_number.txt'
input_file = open(filename, 'r')
print(input_file)
#print(input_file.read())
lines = input_file.readlines()
for line in lines:
    input_roman = line.strip()
    input_decimal = RomanToDecimal(input_roman)
    roman = ToRoman(input_decimal)
input_file.close()

