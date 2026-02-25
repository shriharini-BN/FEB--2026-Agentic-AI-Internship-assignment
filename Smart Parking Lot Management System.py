def smart_parking(capacity, logs):
    count = 0
    for i in logs:
        if i == "IN":
            count = count + 1
        elif i == "OUT":
          count = count - 1
    print("Currently Parked Vehicles:", count)
    if count > capacity:
        print("Parking Status: Full")
    else:
        print("Parking Status: Available")
capacity = 50
logs = ["IN", "IN", "IN", "OUT", "IN", "IN", "OUT"]
smart_parking(capacity, logs)