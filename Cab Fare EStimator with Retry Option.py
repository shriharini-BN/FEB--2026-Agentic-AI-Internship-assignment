def calculate_fare(distance, peak):
    fare = 50 + (12 * distance)
    if peak == "yes":
        fare += fare * 0.25
    return fare
while True:
    km = float(input("Enter distance in km: "))
    peak_hour = input("Is it peak hour? (yes/no): ")
    total_fare = calculate_fare(km, peak_hour)
    print("Total Fare:", total_fare)
    retry = input("Do you want to retry? (yes/no): ")
    if retry != "yes":
        break