class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
    def display_price_tag(self):
        print("Product:", self.product_name)
        print("Price: ₹" + str(self.price))
product = Product("Headphones", 2499)
product.display_price_tag()