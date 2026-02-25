def delivery_time(distance, traffic, weather):
    time = distance * 5   # base time
    if traffic == "High":
        time = time + 15
    elif traffic == "Medium":
        time = time + 10
    if weather == "Rainy":
        time = time + 10
    print("Estimated Delivery Time:", time, "minutes")
delivery_time(8, "High", "Rainy")