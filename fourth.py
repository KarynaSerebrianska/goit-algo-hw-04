def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Please provide both name and new phone number."
    name, new_phone = args
    if name not in contacts:
        return "Not found."
    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) < 1:
        return "Please provide a contact name."
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
