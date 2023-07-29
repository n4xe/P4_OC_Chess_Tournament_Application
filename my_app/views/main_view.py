class MainView:

    @classmethod
    def main_menu(cls):
        print("\nWelcome to the local chess application! Please, use the menu by entering the corresponding numbers"
              "to the desired items\n"
              "\nMain Menu:\n"
              "1. Player and Tournament creation\n"
              "2. Information and data\n"
              "3. Settings and modifications\n"
              "q. Quit")
        choice = input("Choose an option: ")
        return choice

    @classmethod
    def first_menu(cls):
        print("\nCreate Tournament Menu:")
        print("1. Add a player")
        print("2. Start tournament")
        print("b. Back to main menu")
        first_menu_choice = input("Choose an option: ")
        return first_menu_choice

    @classmethod
    def second_menu(cls):
        print("\nView Information Menu:")
        print("1. View players by alphabetical order")
        print("2. View all tournaments")
        print("b. Back to main menu")
        second_menu_choice = input("Choose an option: ")
        return second_menu_choice

    @classmethod
    def third_menu(cls):
        print("\nSettings and Modification Menu:")
        print("1. Delete tournament")
        print("2. Delete player")
        print("3. Modify a player")
        print("b. Back to main menu")
        third_menu_choice = input("Choose an option: ")
        return third_menu_choice

    @classmethod
    def invalid_option(cls):
        print("Invalid option. Please try again.")

    @classmethod
    def goodbye(cls):
        print("Thank you for using the application. Goodbye!")