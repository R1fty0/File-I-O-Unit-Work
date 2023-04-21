class FileRead:

    def __init__(self):
        print('File reader created!')

    def readFirstLineFromFile(self, file):
        """ Print out the contents from the first line of a file. """
        try:
            with open(file, 'r') as reader:
                data = reader.readline()
                print(data)
        except IOError:
            print(f'Unable to read from file: ', {file})

    def readFileLineByLine(self, file):
        """ Prints out contents of the file line by line """
        with open(file, 'r') as reader:
            line = reader.readline()
            while line:  # loop as long as line is defined (stops after last line is read and returns null
                print(line)
                line = reader.readline()  # update line with next line data

    def getFileAllLines(self, file) -> list:
        """ Returns a list of file contents, 1 line per entry """
        data = list()

        with open(file, 'r') as reader:
            line = reader.readline()
            while line:  # loop as long as line is defined (stops after last line is read and returns null)
                data.append(line)  # add line to data
                line = reader.readline()  # update line with next line data

        return data     # return list containing all data after file reading complete

    def getAllDataFromFile(self, file):
        """ Returns a String containing all data from a file """
        try:
            with open(file, 'r') as reader:
                data = reader.read()
                return data
        except IOError:
            print('Unable to read from file: ', file)

    # Allows us to clean up a list of data to remove '\n' (newline) content from it
    def removeNewlinesFromData(self, data):
        """ Returns a file with all \n (newline) content removed """
        for i in range(len(data)):  # through all data
            data[i] = data[i].replace("\n", "")   # remove all references to new lines in data
            if len(data[i]) == 0:  # if there are now empty entries in the data, remove them!
                data.remove(data[i])
                i -= 1  # after removing an entry, we need to move back a step (the list is now 1 shorter)
        return data


    """
        My Functions
    """

    def get_total_number_of_lines(self, file: str) -> int:
        """ Returns the total number of lines of data in a file. """
        num_of_lines = 0  # Initialize line counter
        try:
            with open(file, 'r') as reader:
                for _ in reader:  # Loop through each line in the file
                    num_of_lines += 1  # Increment line counter
            return num_of_lines  # Return the final line count
        except IOError:
            print(f'Unable to read from file: {file}')

    def get_total_characters(self, file: str) -> int:
        """ Returns the total amount of characters in a file. """
        data = str()  # String that contains the file's contents
        try:
            with open(file, 'r') as open_file:
                text = open_file.readlines()  # Reads the content of the file and stores it as a list
                for words in text:  # Converts file contents into a string
                    data += words
                num_of_char = len(data)  # Gets the total number of characters
                return num_of_char  # Returns the total number of characters
        except IOError:
            print(f"Unable to read file: {file}.")

    def is_keyword_present(self, file: str, word: str) -> bool:  # if text.find(word) != -1: was debugged with ChatGPT
        """ Returns whether a file contains a given word or phrase. """
        try:
            with open(file, 'r') as reader:  # Open file
                text = reader.read()  # Read entire file
                if text.find(word) != -1:  # Check if file has word
                    return True
                else:
                    return False

        except IOError:
            print("Something went wrong!")

    def get_words_of_certain_length(self, length: int, file: str) -> list:
        """ Returns a list that only includes words of a certain length. """
        # How do I remove the print-out "None" from the terminal.
        # Add the ability to receive string data
        list_of_words = list()
        try:
            with open(file, 'r') as reader:  # Open file
                text = reader.read().split()  # Read contents and split into words
            for word in text:
                if len(word) == length:  # Add the word to the list if it is length required.
                    list_of_words.append(word)  # Adds the word to the list.
            if len(list_of_words) != 0:
                return list_of_words  # Return list of words
            else:
                print(f"There are no words in the file:{file} that are the length you inputted!")
        except IOError:
            print(f"Unable to open this file: {file}")

