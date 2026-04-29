class Environment:
    def __init__(self):
        self.position = 0
        self.energy_used = 0
        self.path = [0]

    def get_percept(self):
        return self.position

    def update(self, action):
        if action == "Move Forward":
            self.position += 1
            self.energy_used += 1
        elif action == "Move Back":
            self.position -= 1
            self.energy_used += 3

        self.path.append(self.position)


class DeliveryRobot:
    def __init__(self, goal):
        self.goal = goal

    def act(self, percept):
        if percept < self.goal:
            return "Move Forward"
        elif percept > self.goal:
            return "Move Back"
        else:
            return "Stop"


env = Environment()
robot = DeliveryRobot(goal=15)

print("Automated Delivery Robot Started\n")

steps = 0

while True:
    percept = env.get_percept()
    action = robot.act(percept)

    print(f"Position: {percept} → Action: {action}")

    if action == "Stop":
        print("\nGoal reached!")
        break

    env.update(action)
    steps += 1


print("\nPath Visited:", env.path)
print("Total Steps:", steps)
print("Total Energy Used:", env.energy_used)
