import sys

morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/'
}

nb = len(sys.argv)
s = ""

for i in range(1, nb):
    for j in range(0, len(sys.argv[i])):
        if ((sys.argv[i][j]).isalnum() == 0 and (sys.argv[i][j]) != ' '):
            sys.exit("ERROR")

for i in range(1, nb):
    for j in range(0, len(sys.argv[i])):
        s += morse_code[(sys.argv[i][j]).upper()]
        s += " "
    if (i < nb - 1):
        s += "/ "
print(s)
