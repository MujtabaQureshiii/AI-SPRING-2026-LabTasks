class Environment:
    def __init__(self):
        self.rooms = ["Dirty", "Dirty", "Dirty"]
        self.position = 0   #start in room 1

    def get_percept(self):
        return self.rooms, self.position

    def update(self, action):
        if action == "Clean":
            self.rooms[self.position] = "Clean"
        elif action == "Move Right":
            self.position += 1

class CleaningRobot:
    def act(self, percept):
        rooms, position = percept

        if rooms[position] == "Dirty":
            return "Clean"

        if position < 2:
            return "Move Right"

        return "Stop"


env = Environment()
robot = CleaningRobot()

print("Floor Cleaning Robot Started\n")

while True:
    percept = env.get_percept()
    action = robot.act(percept)

    print(f"Position: Room {env.position + 1}")
    print("Rooms:", env.rooms)
    print("Action:", action)
    print()

    if action == "Stop":
        print("All rooms are clean. Task completed.")
        break

    env.update(action)
