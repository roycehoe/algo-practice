"""
https://open.kattis.com/problems/falsesecurity"""

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '_': '..--', '.': '---.', ',': '.-.-', '?': '----'}

MORSE_CODE_DICT = dict((v, k) for k, v in MORSE_CODE_DICT.items())

# code = '.- -.-. -- ..-- --. .-. . .- - . .-. ..-- -. -.-- ..-- .-. . --. .. --- -.'
# decode = [i for i in code.split()]
# for i in decode:
#     print(MORSE_CODE_DICT[i])

code = ".--.-.--..----..-...--..-...---.-.--..--.-..--...----."
spaces = '232313442431121334242'

spaces = [int(i) for i in spaces]
print(spaces)
