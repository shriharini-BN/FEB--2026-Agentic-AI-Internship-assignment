class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def display_contact(self):
        print("Contact Saved")
        print("Name:", self.name)
        print("Phone:", self.phone)
contact = Contact("Anita", "9876543210")
contact.display_contact()