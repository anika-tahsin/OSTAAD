import save_contacts
import search_contacts

def delete_contact(filename, contacts, phone):
    """
    Delete a contact by phone number.
    """
    contact_to_delete = search_contacts(contacts, phone)
    if contact_to_delete:
        contacts.remove(contact_to_delete)
        save_contacts(filename, contacts)  # Save the updated contacts back to the file
        print(f"\nContact with phone number {phone} has been deleted.")
    else:
        print(f"\nNo contact found with phone number {phone}.")
