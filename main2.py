import string
import random

alphabet = ' ' + string.ascii_letters
positions = {}
for i in range(len(alphabet)):
    positions[alphabet[i]] = i

def generate_key():
    min_key_length = 48
    key_length = random.randint(min_key_length, len(alphabet))
    key = ''.join(random.choices(alphabet, k=key_length))
    return key

def get_key_positions(key):
    key_positions = [positions[char] for char in key]
    return key_positions

def encoding(message, key):
    coded_message = ''
    key_positions = get_key_positions(key)
    key_length = len(key_positions)
    for i, char in enumerate(message):
        if char in alphabet:
            shift = key_positions[i % key_length]
            coded_message += alphabet[(positions[char] + shift) % len(alphabet)]
        else:
            coded_message += char
    return coded_message

def decoding(encoded_message, key):
    decoded_message = ''
    key_positions = get_key_positions(key)
    key_length = len(key_positions)
    for i, char in enumerate(encoded_message):
        if char in alphabet:
            shift = key_positions[i % key_length]
            decoded_message += alphabet[(positions[char] - shift) % len(alphabet)]
        else:
            decoded_message += char
    return decoded_message


def main():
    message = input("\nEnter the message: ")

    print("Choose an option:\n1. Encode\n2. Decode\n")
    choice = input("\033[93m\nChoice: \033[0m")

    if choice == '1':
        key = generate_key()
        encoded_message = encoding(message, key)
        print(f"\nEncoded message: \033[92m{encoded_message}\033[0m")
        print(f"Encryption key: \033[92m{key}\033[0m")
    elif choice == '2':
        key = input("Enter the decryption key: ")
        decoded_message = decoding(message, key)
        print(f"\nDecoded message: \033[92m{decoded_message}\033[0m")
    else:
        print("Invalid choice.")


previous_output = False
while True:
    if previous_output:
        print("--------------------------------------------------")
    main()
    previous_output = True
