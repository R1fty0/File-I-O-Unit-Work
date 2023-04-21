from Decrypter import FileDecrypter
decrypter = FileDecrypter()

test_str = "ifmmp xpsme"  # hello world
test_str_2 = "qzuipo"  # python


test_str_data = ["ifmmp xpsme", "qzuipo"]


result = decrypter.decrypt_list_of_str(test_str_data, 1)
print(result)