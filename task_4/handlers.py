def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Add a new contact to the contacts dictionary.

    Creates a new contact entry with the provided name and phone number.
    If a contact with the same name exists, it will be overwritten.

    Args:
        args: List of arguments where args[0] is contact name and args[1] is phone number.
              Must contain at least 2 elements.
        contacts: Dictionary to store contact information with name as key.

    Returns:
        Success message "Contact added." or error message "Invalid command."
        if insufficient arguments are provided.

    Example:
        >>> contacts = {}
        >>> add_contact(["John", "1234567890"], contacts)
        "Contact added."
        >>> contacts
        {"John": "1234567890"}
    """

    if len(args) < 2:
        return "Invalid command."

    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Change phone number for an existing contact.

    Updates the phone number for a contact that already exists in the dictionary.
    Contact must exist before updating.

    Args:
        args: List of arguments where args[0] is contact name and args[1] is new phone number.
              Must contain at least 2 elements.
        contacts: Dictionary containing existing contact information.

    Returns:
        Success message "Contact updated." if contact exists and was updated.
        Returns "Invalid command." if insufficient arguments provided.
        Returns "Contact not found." if the named contact does not exist.

    Example:
        >>> contacts = {"John": "1234567890"}
        >>> change_contact(["John", "0987654321"], contacts)
        "Contact updated."
        >>> contacts
        {"John": "0987654321"}
    """

    if len(args) < 2:
        return "Invalid command."

    name, phone = args[0], args[1]
    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Retrieve and return phone number for a specific contact.

    Looks up a contact by name and returns their phone number.

    Args:
        args: List of arguments where args[0] is the contact name to look up.
              Must contain at least 1 element.
        contacts: Dictionary containing contact information.

    Returns:
        The phone number string if contact is found.
        Returns "Invalid command." if no arguments provided.
        Returns "Contact not found." if the named contact does not exist.

    Example:
        >>> contacts = {"John": "1234567890"}
        >>> show_phone(["John"], contacts)
        "1234567890"
        >>> show_phone(["Jane"], contacts)
        "Contact not found."
    """

    if len(args) < 1:
        return "Invalid command."

    name = args[0]
    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    """
    Display all contacts in a formatted table.

    Returns all contacts sorted alphabetically by name with phone numbers
    displayed in a formatted table with aligned columns.

    Args:
        contacts: Dictionary containing contact information with names as keys.

    Returns:
        Formatted table string with header, separator, and contact entries.
        Each line contains name and phone number separated by " | ".
        Returns "No contacts found." if the contacts dictionary is empty.

    Example:
        >>> contacts = {"Alice": "1111111111", "Bob": "2222222222"}
        >>> print(show_all(contacts))
        Name | Phone
        ---- | -----
        Alice | 1111111111
        Bob | 2222222222
    """

    if not contacts:
        return "No contacts found."

    # Sort contacts alphabetically by name (case-insensitive)
    sorted_contacts = sorted(contacts.items(), key=lambda item: item[0].lower())

    # Calculate maximum name length for proper alignment
    max_name_len = max(len(name) for name, _ in sorted_contacts)

    # Build table header and separator
    header = f"{'Name'.ljust(max_name_len)} | Phone"
    separator = f"{'-' * max_name_len} | {'-' * 5}"
    lines = [header, separator]

    # Add contact rows
    lines.extend(
        f"{name.ljust(max_name_len)} | {phone}" for name, phone in sorted_contacts
    )

    return "\n".join(lines)
