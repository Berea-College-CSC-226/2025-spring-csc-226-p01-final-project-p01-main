class CaesarCipher:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # The alphabet, which will be used to do our shifts

    def __init__(self, crypt_type, input_file="letters/message_input.txt", key=0):
        """
        Initializes a CaesarCipher object.
        """
        self.input_file = input_file  # The file to be encrypted or decrypted
        self.key = key  # The amount each message/cipher will be shifted
        self.crypt_type = crypt_type  # Either "encrypt" or "decrypt"
        if self.crypt_type == "encrypt":
            self.message = ""  # A placeholder for the message
        else:
            self.cipher = ""  # A placeholder for the cipher
        self.import_file()  # Calls the import_file() method below

    def import_file(self):
        """
        Imports a file stored in the variable self.input_file

        :return: a string representing the contents of the file
        """
        f = open(self.input_file, "r")
        if self.crypt_type == "encrypt":
            self.message = f.read()  # Set self.message to the file contents
        elif self.crypt_type == "decrypt":
            self.cipher = f.read()  # Set self.cipher to the file contents
        f.close()
        if __name__ == "__main__":
            print("File imported: {0}".format(self.input_file))

    def export_file(self, filename):
        """
        Exports a file called filename

        :param text_to_export: the string to be written to the exported file
        :param filename: a string representing the name of the file to be exported to
        """
        f = open(filename, "w")
        if self.crypt_type == "encrypt":
            f.write(self.cipher)
        else:
            f.write(self.message)
        f.close()
        if __name__ == "__main__":
            print("File exported: {0}".format(filename))

    def encrypt(self):
        """
        Converts an original message into a ciphered message with each letter shifted to the right by the key.

        :return: None
        """
        if self.crypt_type == "encrypt":
            output = ""
            for i in self.message:
                if i.upper() in self.alphabet:
                    old_letter = self.alphabet.find(i.upper())
                    # Uses modulus to return the correct index for each letter after the shift
                    # (for cases where the index is outside the range of self.alphabet,
                    #  it wraps back to the beginning of the alphabet)
                    output += self.alphabet[(old_letter + self.key) % 26]
                else:
                    output += i  # Adds non-alphabet characters directly
            if __name__ == "__main__":
                print("Message Encrypted")
            self.cipher = output

    def decrypt(self):
        """
        Decrypts a message encrypted with the Caesar cipher.

        :return:
        """
        if self.crypt_type == "decrypt":
            output = ""
            for i in self.cipher:
                if i.upper() in self.alphabet:
                    old_letter = self.alphabet.find(i.upper())
                    output += self.alphabet[(old_letter - self.key) % 26]
                else:
                    output += i
            if __name__ == "__main__":
                print("Message Decrypted")
            self.message = output


def main():
    """
    Main function to execute encryption and decryption tasks.
    """

    # Constructs a new CaesarCipher object called cipher0
    cipher0 = CaesarCipher("encrypt", "letters/message_input.txt", 2)
    cipher0.encrypt()  # Encrypts the file specified above
    cipher0.export_file("cipher_sample.txt")  # Writes the output to a file

    # Caesar has some letters to send and receive.
    # Letter 1 goes to P. Lentulus Spinther, who has agreed with Caesar to use a key of 3
    cipher_lentulus = CaesarCipher("encrypt", "letters/letter_to_friend_1.txt", 3)
    cipher_lentulus.encrypt()
    cipher_lentulus.export_file("ciphers/cipher_to_friend_1.txt")

    # Letter 2 goes to Marcus Tullius Cicero, who has agreed to use a key of 14
    cipher_marcus = CaesarCipher("encrypt", "letters/letter_to_friend_2.txt", 14)
    cipher_marcus.encrypt()
    cipher_marcus.export_file("ciphers/cipher_to_friend_2.txt")

    # Letter 3 is coming from Cicero for Caesar to decrypt. Again, they agreed to use key 14
    cipher3 = CaesarCipher("decrypt", "ciphers/cipher_from_friend_3.txt", 14)
    cipher3.decrypt()
    cipher3.export_file("letters/message_from_friend_3.txt")


if __name__ == "__main__":
    main()
