def add_contact(contacts):
    """Adds new contact & updates contacts book"""
    name = input("Enter Your name:")
    phone = input("Enter Your Phone:")
    email = input("Enter Your Email:")
    if name in contacts:
        print("❌Contact already exists")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print("✅Contact is saved")



def search_contact(contacts):
    """Search for the contact & returns whereabouts if it exists"""
    search_name = input("Enter name to search:")
    if search_name not in contacts:
        print("❌Contact not found")
    else:
        print(search_name, "👉" ,contacts.get(search_name))



def update_contact(contacts):
    """Updates the existing contact"""
    update_name = input("enter name to update: ")
    if update_name not in contacts:
        print("❌Contact not found")
        return
    update_option = input("What to update (Phone/ Email/ Both): ")
    if update_option == "phone":
        new_phone = input("Enter your new phone: ")
        contacts[update_name].update({"phone":new_phone})
    elif update_option == "email":
        new_email = input("Enter your new email: ")
        contacts[update_name].update({"email": new_email})
    else:
        new_phone = input("Enter your new phone: ")
        new_email = input("Enter your new email: ")
        contacts[update_name].update({"phone":new_phone, "email": new_email})
    print(f"✅{update_name}'s {update_option} updated")



def delete_contact(contacts):
    """deletes an existing contact if user confirms"""
    delete_name = input("Enter name to delete: ")
    surity = input("Are you sure, (yes/no): ")
    if surity == "no":
        return 
    else:
        delete_name_result = contacts.pop(delete_name, None)
        if delete_name_result is None:
            print("❌Contact not found")
        else:
            print(f"✅Contact {delete_name} deleted")



def view_all(contacts):
    """prints all existing contacts"""
    if not contacts:
        print("❌No contact saved yet")
        return
    for name, details in contacts.items():
        print(f"📋 {name} | Phone: {details['phone']} | Email: {details['email']}")



def main():
    """runs contact book"""
    contacts = {}
    while True:
        print("=== Contact Book ===")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. View all contacts")
        print("6. Quit")
        option = input("Choose an option: ")
        if option == '1':
            add_contact(contacts)
        elif option == '2':
            search_contact(contacts)
        elif option == '3':
            update_contact(contacts)
        elif option == '4':
            delete_contact(contacts)
        elif option == '5':
            view_all(contacts)
        elif option == '6':
            print("Quit")
            break

if __name__ == "__main__":
    main()