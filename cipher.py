# assignment: programming assignment 4
# author: Aradhya Kapoor
# date: Nov/27/22
# file: cipher.py 
# input: User inputs for file names and then deocdes
# output: ciphers a reult by encoding and decoding 

def readfile():
    while True:
        try:
            filename = input("Please enter a file for reading:\n")
            with open(filename, 'r') as file:
                message = file.readlines()
            return message
        except FileNotFoundError:
            print("The selected file cannot be open for reading!")
            continue

# write a list of strings (message) to a file
# the function should contain an input statement, open file statement,
# and try-except statement
def writefile(message):
    while True:
        try:
            filename = input("Please enter a file for writing:\n")
            with open(filename, 'w') as file:
                file.writelines(message)
            break
        except:
            print("The selected file cannot be open for writing!")
            continue

# make a tuple of letters in the English alphabet
def make_alphabet():
    alphabet = tuple(chr(i) for i in range(65, 91))
    return alphabet

# encode plaintext letter by letter using a Caesar cipher 
# plaintext is a list of strings
# return a list of encoded strings
def encode(plaintext, shift=3):
    alphabet = make_alphabet()
    ciphertext = []
    for line in plaintext:
        encoded_line = ''
        for char in line:
            if char.isalpha():
                index = alphabet.index(char.upper())
                encoded_index = (index + shift) % len(alphabet)
                encoded_char = alphabet[encoded_index]
                encoded_line += encoded_char if char.isupper() else encoded_char.lower()
            else:
                encoded_line += char
        ciphertext.append(encoded_line)
    return ciphertext

# decode ciphertext letter by letter using a Caesar cipher
# ciphertext is a list of strings
# return a list of decoded strings
def decode(ciphertext, shift=-3):
    return encode(ciphertext, shift)

# convert a list into a string
def to_string(text):
    return ''.join(text)

# main program
if __name__ == '__main__':
    while True:
        print("Would you like to encode or decode the message?")
        print("Type E to encode, D to decode, or Q to quit:")
        choice = input().upper()

        if choice == 'E':
            message = readfile()
            encoded_message = encode(message)
            writefile(encoded_message)
            print("Plaintext:")
            print(to_string(message), end = '')
            print("Ciphertext:")
            print(to_string(encoded_message), end = '')
            
        elif choice == 'D':
            message = readfile()
            decoded_message = decode(message)
            writefile(decoded_message)
            print("Ciphertext:")
            print(to_string(message), end = '')
            
            print("Plaintext:")
            print(to_string(decoded_message), end = '')
            
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter E, D, or Q.")
