class Delivery:
    def __init__(self, customer_name, address):
        self.customer_name = customer_name
        self.address = address
    def display_delivery(self):
        print("Delivery Details")
        print("Customer:", self.customer_name)
        print("Address:", self.address)
delivery = Delivery("Suman", "Hyderabad")
delivery.display_delivery()