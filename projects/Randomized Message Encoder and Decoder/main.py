import random
import string

def encode_message():
    message = input("Enter the message to encode: ")
    words = message.split()
    new_word = ''
    for word in words:
        letter1 = random.choice(string.ascii_letters)
        letter2 = random.choice(string.ascii_letters)
        letter3 = random.choice(string.ascii_letters)
        digit1 = random.choice(string.digits)
        digit2 = random.choice(string.digits)
        digit3 = random.choice(string.digits)
        new_word += letter1 + letter2 + letter3 + word + digit1 + digit2 + digit3 + ' '

    print("Encoded message:", new_word.strip())

def decode_message():
    encoded_message = input("Enter the message to decode: ")
    words = encoded_message.split()
    decoded_message = ''
    for word in words:
        decoded_word = word[3:-3]  # Remove the first 3 letters and last 3 digits
        decoded_message += decoded_word + ' '
    print("Decoded message:", decoded_message.strip())


def main():
    while True:
        user_input = input("Enter 1 to encode a message, 2 to decode a message, or 3 to exit: ")
        if user_input == '1':
            encode_message()
        elif user_input == '2':
            decode_message()
        elif user_input == '3':
            break
        else:
            print("Invalid input. Please try again.")

if __name__=="__main__":
    main()