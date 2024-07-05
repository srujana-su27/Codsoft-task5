import sys

contacts = []

def add_contact(name, phone, email, address):
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("List of Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact(query):
    query = query.lower()
    search_results = [contact for contact in contacts
                      if query in contact['name'].lower() or query in contact['phone']]
    
    if not search_results:
        print("No matching contacts found.")
    else:
        print("Search Results:")
        for idx, contact in enumerate(search_results, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def update_contact(index, name=None, phone=None, email=None, address=None):
    if 0 <= index < len(contacts):
        contact = contacts[index]
        if name:
            contact['name'] = name
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        if address:
            contact['address'] = address
        print(f"Contact updated successfully.")
    else:
        print("Invalid contact index.")

def delete_contact(index):
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted successfully.")
    else:
        print("Invalid contact index.")

def main():
    while True:
        print("\nContact Information")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email (optional): ")
            address = input("Enter contact address (optional): ")
            add_contact(name, phone, email, address)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_contact(query)

        elif choice == '4':
            index = int(input("Enter contact index to update: ")) - 1
            name = input("Enter new name (leave blank to keep unchanged): ")
            phone = input("Enter new phone number (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            address = input("Enter new address (leave blank to keep unchanged): ")
            update_contact(index, name, phone, email, address)

        elif choice == '5':
            index = int(input("Enter contact index to delete: ")) - 1
            delete_contact(index)

        elif choice == '6':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
