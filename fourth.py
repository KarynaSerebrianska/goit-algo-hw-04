def parse_input(user_input):
    # розбиваємо команду і аргументи
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    # додати контакт у словник
    if len(args) < 2:
        return "Please provide both name and phone number."
    name = args[0]
    phone = args[1]
    contacts[name] = phone
    return f"Contact added."

def change_contact(args, contacts):
    # змінити номер контакту
    if len(args) < 2:
        return "Please provide both name and new phone number."
    name = args[0]
    if name not in contacts:
        return "Not found."
    new_phone = args[1]
    contacts[name] = new_phone
    return f"Contact updated."

def show_phone(args, contacts):
    # показати номер телефону
    if len(args) < 1:
        return "Please provide a contact name."
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts):
    # вивести всі контакти
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
