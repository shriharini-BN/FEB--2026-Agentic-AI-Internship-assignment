def seat_occupancy(total_seats, booked_seats):
    booked = len(booked_seats)
    occupancy = (booked / total_seats) * 100
    print("Occupancy:", int(occupancy), "%")
    if occupancy >= 100:
        print("Show Status: Housefull")
    elif occupancy >= 75:
        print("Show Status: Almost Full")
    else:
        print("Show Status: Available")
total_seats = 200
booked_seats = [1] * 150
seat_occupancy(total_seats, booked_seats)