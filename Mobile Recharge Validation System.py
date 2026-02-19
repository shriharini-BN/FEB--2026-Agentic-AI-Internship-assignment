def recharge_validation():
    valid_plans = [199, 299, 399, 599]
    while True:
        amount = int(input("Enter recharge amount: "))
        if amount >= 50 and amount in valid_plans:
            print("Recharge Successful")
            break
        else:
            print("Invalid recharge. Try again.")