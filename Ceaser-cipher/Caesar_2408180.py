# Name: ISHA BHATTA
# Student ID: 2408180

import os

# Step 1
def welcome():
    """
    Displays a welcome message for the Caesar Cipher program.
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher!\n")

# Step 2
def enter_message():
    """
    Takes user input for encryption or decryption mode, message, and shift number.
    Returns a tuple containing mode ('e' or 'd'), message, and shift.
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        message = input(f"What message would you like to {'' if mode == 'e' else 'de'}crypt: ").upper()
        shift_str = input("What is the shift number: ")

        try:
            shift = int(shift_str)
            break
        except ValueError:
            print("Invalid Shift")

    return mode, message, shift

# Step 3
def encrypt(message, shift):
    """
    Encrypts the given message using the Caesar Cipher with the specified shift.
    Returns the encrypted message.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

# Step 4
def decrypt(message, shift):
    """
    Decrypts the given message using the Caesar Cipher with the specified shift.
    Returns the decrypted message.
    """
    return encrypt(message, -shift)

# Step 5
def process_file(filename, mode, shift):
    """
    Reads messages from a file, encrypts or decrypts them based on the mode and shift,
    and returns a list of processed messages.
    """
    messages = []
    with open(filename, 'r') as file:
        for line in file:
            if mode == 'e':
                messages.append(encrypt(line.strip(), shift))
            elif mode == 'd':
                messages.append(decrypt(line.strip(), shift))
    return messages

def is_file(filename):
    """
    Check if a file exists.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(filename)

def write_messages(messages):
    """
    Write messages to a file.
    Args:
        messages (list): A list of messages to write to the file.
    """
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

def message_or_file():
    """
    Prompt the user to choose between encryption or decryption mode,
    and whether to read input from the console or a file.
    Returns:
        tuple: A tuple containing the mode ('e' for encryption, 'd' for decryption),
               the message (if input from console), and the filename (if input from a file)."""

    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ['f', 'c']:
            break
        else:
            print("Invalid Input")

    if source == 'c':
        message = input(f"What message would you like to {'' if mode == 'e' else 'de'}crypt: ").upper()
        return mode, message, None
    else:
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")
        return mode, None, filename
#Step_6
def main():
    """
    The main function that coordinates the entire program flow.
    Calls other functions based on user input to perform encryption or decryption.
    """
    welcome()

    while True:
        mode, message, filename = message_or_file()

        while True:
            try:
                shift = int(input("What is the shift number: "))
                break
            except ValueError:
                print("Invalid Shift")

        if filename:
            messages = process_file(filename, mode, shift)
            write_messages(messages)
            print("Output written to results.txt")
        else:
            result = encrypt(message, shift) if mode == 'e' else decrypt(message, shift)
            print(result)

        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message != 'y':
            print("Thanks for using the program, goodbye!")
            break

if __name__ == "__main__":
    main()
