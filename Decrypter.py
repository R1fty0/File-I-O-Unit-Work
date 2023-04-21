class FileDecrypter:
    def __init__(self):
        print("Decrypter Online.")

    def decrypt_string(self, encrypted_string, cypher) -> str:
        """ Decrypts a string using a given cypher/shift and then returns the encrypted data."""
        # Need to remove space symbols...
        decrypted_string = ''

        data_list = list(encrypted_string)  # list containing each character in the string

        try:
            for character in data_list:  # decrypts each character in the string
                char_unicode = ord(character)
                decrypted_char = chr(char_unicode - cypher)
                decrypted_string += decrypted_char
            return decrypted_string  # returns the decrypted string

        except TypeError:
            print("An error occurred.")

    def decrypt_list_of_str(self, data, cypher):
        decrypted_data = list()  # list containing decrypted string data
        if type(data) is not type(list):
            encrypted_data_list = list(data)  # creates a list of data
        else:
            encrypted_data_list = data
        for data in encrypted_data_list:
            result = self.decrypt_string(data, cypher)  # decrypt string
            decrypted_data.append(result)  # add to list of decrypted data
        return decrypted_data   # returns the list containing the decrypted data
