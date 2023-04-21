# write() - writes the listed string to the file

# Read more here! https://realpython.com/read-write-files-python/

class FileWrite:

    def __init__(self, basics):
        print('File writer created!')
        self.basics = basics

    def writeStringOverFile(self, fileName, stringData):
        """ Write String data to file, overwriting previous file contents """
        try:
            with open(fileName, 'w') as writer:
                writer.write(stringData)
        except IOError:
            print('Error writing to file: ', fileName)

    def writeStringToFile(self, fileName, data):
        """ Write String data to file, appending onto exiting file contents """
        try:
            with open(fileName, 'a') as writer:
                writer.write(data)
        except IOError:
            print('Error writing to file: ', fileName)

    def writeDataOverFile(self, fileName, data):
        """ Write list data to file, overwriting previous file contents """
        try:
            with open(fileName, 'w') as writer:
                for entry in data:
                    writer.write(entry + '\n')  # add each data entry on its own line
        except IOError:
            print('Error writing to file: ', fileName)

    def writeListDataToFile(self, fileName, data):
        """ Write list data to file, appending onto existing file contents """
        try:
            with open(fileName, 'a') as writer:
                for entry in data:
                    writer.write(entry + '\n')  # add each data entry on its own line
        except IOError:
            print('Error writing to file: ', fileName)

    def writeDataOverFileCustom(self, fileName, data, delimiter):
        """ Write list data to file, overwriting previous file contents, using custom delimiter """
        try:
            with open(fileName, 'w') as writer:
                for entry in data:
                    writer.write(entry + delimiter)  # add each data entry separated by custom delimiter
        except IOError:
            print('Error writing to file: ', fileName)

    def writeDataToFileCustom(self, fileName, data, delimiter):
        """ Write list data to file, appending onto existing file contents, using custom delimiter """
        try:
            with open(fileName, 'a') as writer:
                for entry in data:
                    writer.write(entry + delimiter)  # add each data entry separated by custom delimiter
        except IOError:
            print('Error writing to file: ', fileName)

    def writeNumbersTo100ToFile(self, fileName, append):
        """ Write the numbers 1 to 100 to given file, appending or overwriting based in boolean input """

        # Begin by generating a string with the numbers 1 to 100 organized into 10 rows
        num = 1  # variable holding first number to be printed
        stringToWrite = ''  # variable to hold the String being built
        for a in range(10):  # loop for rows
            for b in range(10):  # loop for numbers in each row
                nextEntry = '\t' + str(num)
                stringToWrite += nextEntry  # add the next number to the master string
                num += 1  # increase number by 1
            stringToWrite += '\n'  # add a new line to string to create new row

        # Finally, write this string to a file in manner determined (write or append)
        if append:
            self.writeStringToFile(fileName, stringToWrite)
        else:
            self.writeStringOverFile(fileName, stringToWrite)

    def writeNumbersToFileAdvanced(self, fileName, append, maxNum, numsPerRow):
        """ Write a custom number of numbers using custom organization to file, appending or overwriting based on boolean input """
        numRows = int(
            maxNum / numsPerRow)  # determine number of rows that will fit custom organization with no remainder
        extraNums = maxNum % numsPerRow  # determine the number of overflow values (the final row) that need to be added
        num = 1  # value to start counting from
        customAligner = '            '  # Whitespace used to organize output alignment; make bigger if numbers expect to get large
        stringToWrite = ''  # variable to hold the String being built

        print(numRows)
        print(extraNums)

        # write all full rows to master String
        for row in range(numRows):
            for val in range(numsPerRow):
                stringLength = len(str(num))  # calculate the length of the number, for content organization
                nextEntry = str(num) + customAligner[
                                       stringLength:]  # Concatenate the number to the customAligner, adjusting aligner spaces in relation to number length
                stringToWrite += nextEntry  # add the next number to the master string
                num += 1
            stringToWrite += '\n'  # add a new line to string to create new row

        # writer overflow row to master String - if there is one!
        for val in range(extraNums):
            stringLength = len(str(num))  # calculate the length of the number, for content organization
            nextEntry = str(num) + customAligner[
                                   stringLength:]  # Concatenate the number to the customAligner, adjusting aligner spaces in relation to number length
            stringToWrite += nextEntry
            num += 1

        # Finally, write this string to a file in manner determined (write or append)
        if append:
            self.writeStringToFile(fileName, stringToWrite)
        else:
            self.writeStringOverFile(fileName, stringToWrite)

    """
        My Methods
    """

    def merge_files(self, file1, file2, file3):
        """ Merges 3 different files together into a single file."""
        files = [file1, file2, file3]  # list containing all original files.
        try:
            for file in files:
                with open(file, 'r') as f:
                    content = f.readlines()  # reads content of file
                    with open("merged files.txt", "a") as new_file:
                        for text in content:
                            new_file.write(f"\n{text}")  # adds content of original file to new file.
        except IOError:
            print(f"An error occurred while trying to merge these 3 files!: {file1}, {file2}, {file3}.")

    def create_copy_of_file_based_on_parameter(self, original_file, word_length: bool):
        # How to get rid of white space?
        """ Creates a copy of a given file that arranges the contents in alphabetical order or word length."""
        try:
            with open(original_file, 'r') as open_file:
                data = open_file.read().split()  # opens file and converts content into a string
                if word_length:
                    sorted_words = sorted(data, key=len)  # Sorts by word length
                    new_file_name = "create_copy_of_file_based_on_word_length"
                elif word_length is False:
                    sorted_words = sorted(data)  # Sorts by alphabetic order
                    new_file_name = "create_copy_of_file_based_on_alphabetic order"

            with open(new_file_name + ".txt", 'w') as new_open_file:  # creates new file
                for text in sorted_words:
                    new_open_file.write("\n" + text)  # writes content into new file

        except IOError:
            print(f"Unable to create copy of file: {original_file}.")

    def write_data_to_file(self, data, file):
        """ Create a method that writes all sent data (either a String or a List) to a file with a common format decided by you. """
        try:
            if self.basics.is_given_data_type(data, str):  # Write string data to file
                with open(str(file), 'w') as open_file:
                    open_file.write(data)
            elif self.basics.is_given_data_type(data, list): # Write list data to file
                with open(str(file), 'a') as open_file:
                    for text in data:
                        open_file.write(text)
        except IOError:
            print(f"Something went wrong when trying to write data to this file: {file}.")


