class SmartLight:
    def __init__(self, light_name):
        self.light_name = light_name
        self.status = "OFF"   # Default status
    def turn_on(self):
        self.status = "ON"
    def turn_off(self):
        self.status = "OFF"
    def display_status(self):
        print(f"{self.light_name} is {self.status}")
light = SmartLight("Bedroom Light")
light.turn_on()
light.display_status()