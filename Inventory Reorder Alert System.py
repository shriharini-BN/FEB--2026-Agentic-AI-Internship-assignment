def check_inventory(products):
    for item, stock in products.items():
        if stock < 15:
            print(item, "- Reorder Alert")
        else:
            print(item, "- Stock OK")
products = {
    "Rice": 20,
    "Oil": 10,
    "Sugar": 5
}
check_inventory(products)