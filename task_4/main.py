from input_parser import parse_input
from handlers import add_contact, change_contact, show_phone, show_all


def main() -> None:
    """
    Main CLI loop for the contact assistant bot.

    Provides an interactive command-line interface for managing contacts.
    Supported commands:
    - hello: Display greeting
    - add <name> <phone>: Add a new contact
    - change <name> <phone>: Update an existing contact's phone
    - phone <name>: Look up a contact's phone number
    - all: Display all contacts in a formatted table
    - close/exit: Terminate the program

    The bot runs in an infinite loop until the user enters "close" or "exit".
    """

    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))


# For testing purposes
if __name__ == "__main__":
    main()
