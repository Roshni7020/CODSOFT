class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in (contact.name.lower() or contact.phone_number.lower())]
        if not results:
            print("No matching contacts found.")
        else:
            print("\nMatching Contacts:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        print(f"Contact {name} deleted successfully.")

def body():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)
        elif choice == "4":
            name = input("Enter name to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == "5":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__=="__main__":
    body()
