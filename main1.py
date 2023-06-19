import string

alphabet = ' ' + string.ascii_letters
positions = {}
for i in range(len(alphabet)):
    positions[alphabet[i]] = i

def encoding(message, key):
    coded_message = ''
    for char in message:
        if char in alphabet:
            coded_message += alphabet[(positions[char] + key) % len(alphabet)]
        else:
            coded_message += char
    return coded_message

def decoding(encoded_message, key):
    decoded_message = ''
    for char in encoded_message:
        if char in alphabet:
            decoded_message += alphabet[(positions[char] - key) % len(alphabet)]
        else:
            decoded_message += char
    return decoded_message


def main():
    message = input("\nEnter the message: ")

    print("Choose an option:\n1. Encode\n2. Decode\n")
    choice = input("\033[93m\nChoice: \033[0m")

    if choice == '1':
        key = int(input("Enter the encryption key: "))
        encoded_message = encoding(message, key)
        print(f"\nEncoded message: \033[92m{encoded_message}\033[0m")
    elif choice == '2':
        key = int(input("Enter the decryption key: "))
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
