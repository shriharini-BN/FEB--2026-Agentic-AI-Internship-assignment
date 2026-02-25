def server_load(cpu_readings):
    total = 0
    for i in cpu_readings:
        total = total + i
    average = total / len(cpu_readings)
    print("Average CPU Load:", int(average), "%")
    if average < 50:
        print("Server Status: Normal")
    elif average <= 80:
        print("Server Status: Warning")
    else:
        print("Server Status: Critical")
cpu_readings = [45, 60, 70, 85, 90]
server_load(cpu_readings)