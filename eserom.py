# Create a dictionary with the Morse code
MORSE_CODE = {
    '10': 'A',
    '0111': 'B',
    '0101': 'C',
    '011': 'D',
    '1': 'E',
    '1101': 'F',
    '001': 'G',
    '1111': 'H',
    '11': 'I',
    '1000': 'J',
    '010': 'K',
    '1011': 'L',
    '00': 'M',
    '01': 'N',
    '000': 'O',
    '1001': 'P',
    '0010': 'Q',
    '101': 'R',
    '111': 'S',
    '0': 'T',
    '110': 'U',
    '1110': 'V',
    '100': 'W',
    '0110': 'X',
    '0100': 'Y',
    '0011': 'Z',
    '00000': '0',
    '10000': '1',
    '11000': '2',
    '11100': '3',
    '11110': '4',
    '11111': '5',
    '01111': '6',
    '00111': '7',
    '00011': '8',
    '00001': '9'
}

# Function to decode the Morse code
def decodeMorse(message):
    # Split the message into words
    words = message.split('  ')
    # Split the words into letters
    letters = [word.split(' ') for word in words]
    # Decode the letters
    decoded_message = ''
    for word in letters:
        for letter in word:
            decoded_message += MORSE_CODE[letter]
        decoded_message += ' '
    # Return the decoded message
    return decoded_message.strip()

# Test the function
print(decodeMorse('1111 1 1011 1011 000  100 000 101 1011 011')) # 'HELLO WORLD'
