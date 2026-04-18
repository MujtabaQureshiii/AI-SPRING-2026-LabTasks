class LightSystem:
    def __init__(self, room):
        self.room = room
        self.status = "OFF"

    def turningOn(self):
        self.status = "ON"
        print(f"{self.room} light turned ON.")

    def turningOff(self):
        self.status = "OFF"
        print(f"{self.room} light turned OFF.")

    def show_status(self):
        print(f"{self.room} light is {self.status}.")
        
living_room = LightSystem("Living Room")
bedroom = LightSystem("Bedroom")

living_room.turningOn()
bedroom.turningOff()

living_room.show_status()
bedroom.show_status()
