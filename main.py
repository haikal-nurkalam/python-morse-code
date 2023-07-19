MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': '.......'}


 # Get the data
user_input = input('Input your morse code')

# List of split input
split_input = []

#Append each input into a split_input list
for a in user_input:
    split_input.append(a.capitalize())



# here is the string for morse code
morse_code = ''

# we can loop for each character in split input here
for i in split_input : 

# Check if the character exists in the MORSE_CODE_DICT
    if i in MORSE_CODE_DICT:
        # If the character exists in the MORSE_CODE_DICT, add its corresponding Morse code values to morse_code
        morse_code += f'{MORSE_CODE_DICT[i]}, '
    else:
        # if the character is not exist, print this to console
        print(f"this character '{i}' is'nt available")

#lastly we can print the morse code
print(morse_code)
