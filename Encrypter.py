class FileEncrypter:
    def __init__(self):
        print("Encrypter Online.")

    def encode_string(self, message: str, cipher_key: int) -> str:
        """ Encodes a given string using a Cesarean cipher and returns the encoded string. """
        encrypted_string = ''
        try:
            message_list = list(message)

            for character in message_list:
                char_unicode = ord(character)  # Gets the character's unicode code point

                # Checks to see if character's unicode is not a unicode representing a letter
                if char_unicode > 126:
                    char_unicode -= 95
                elif char_unicode < 32:
                    char_unicode += 95
                else:
                    # encrypts the character based on the cipher's key
                    new_encoded_char = chr(char_unicode + cipher_key)
                    encrypted_string += new_encoded_char

            print(f"Encrypted message: {encrypted_string}")  # prints the encoded string
            return encrypted_string  # returns the encoded string

        except TypeError:
            print("An error occurred.")

    def encode_to_file(self, new_file_name, data, encryption_key):
        """ Data given will be encoded as well as written to a custom file. """
        pass

    def encode_list_of_data(self, data: list, cipher_key) -> list:
        """ Accepts a list of Strings, encodes all of them, and returns a list of the encoded content. """
        encoded_content = list()
        try:
            for string in data:  # Encodes each string in list of data
                encoded_data = self.encode_string(string, cipher_key)
                encoded_content.append(encoded_data)
            return encoded_content  # Returns list containing encoded data
        except TypeError:
            print("The data or cipher key you inputted is invalid. Please try again and enter a proper value for both attributes.")
