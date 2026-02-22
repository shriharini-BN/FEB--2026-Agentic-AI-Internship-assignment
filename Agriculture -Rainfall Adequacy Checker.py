def rainfall_checker(rainfall, required):
    total = 0
    for r in rainfall:
        total += r
    average = total / len(rainfall)
    if average >= required:
        status = "Adequate Rainfall"
    else:
        status = "Inadequate Rainfall"

    print("Average Rainfall:", average)
    print("Rainfall Status:", status)
rainfall_checker([70, 75, 72, 71], 70)