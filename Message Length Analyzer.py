messages=["Hi","Welcome to the platform","OK"]
for message in messages:
    length=len(message)
    print(length)
    if length>10:
     print("Flag: Message is longer than 10 characters")