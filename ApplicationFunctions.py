class Menu:
    def __init__(self, greeting_message: str):
        self.menu = self.populate_menu()
        self.greeting = greeting_message

    def display_menu(self):
        """ Displays the menu to the user."""
        for key, value in self.menu.items():
            print(str(key) + ": " + value)
        choice = input("What would you like to do?: ")

    def populate_menu(self) -> dict:
        """ Populates the initial menu dictionary with keys and values."""
        menu = {1: "Encrypt string data.", 2: "Decrypt string data.", 3: "Encrypt list data",
                4: "Decrypt list data", 5: "Encrypt data sent to a file", 6: "Decrypt data from a file",
                7: "Extension problems"}
        return menu

    def greet_user(self):
        """ Greets the user. """
        print(self.greeting + "\n_____________________________________")

