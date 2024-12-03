def search_contact(contacts, phone):
    """
    Search for a contact by phone number.
    """
    for contact in contacts:
        if contact[1] == phone:
            return contact
    return None
