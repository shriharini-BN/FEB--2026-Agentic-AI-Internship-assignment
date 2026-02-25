def event_registration(capacity, registrations):
    if registrations > capacity:
        print("Confirmed Registrations:", capacity)
        print("Waitlisted Users:", registrations - capacity)
        print("Registration Status: Closed")
    else:
        print("Confirmed Registrations:", registrations)
        print("Waitlisted Users: 0")
        print("Registration Status: Open")
event_registration(100, 105)