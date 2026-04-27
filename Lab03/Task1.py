class SmartStreetLightAgent:
    def select_action(self, light_intensity, motion_detected):
        if light_intensity == "Bright":
            return "Light OFF"
        elif light_intensity == "Dim" and motion_detected == "Yes":
            return "Light ON"
        else:
            return "Light OFF"

    def act(self, percept):
        light_intensity, motion_detected = percept
        return self.select_action(light_intensity, motion_detected)


class Environment:
    def __init__(self):
        self.light_intensity = "Bright"
        self.motion_detected = "No"

    def get_percept(self):
        return self.light_intensity, self.motion_detected

    def update_environment(self):
        self.light_intensity = input("\nEnter Light Intensity (Bright/Dim) or X to exit: ")
        if self.light_intensity.upper() == "X":
            return False
        self.motion_detected = input("Motion Detected? (Yes/No) or X to exit: ")
        if self.motion_detected.upper() == "X":
            return False
        return True

def run_agent(agent, environment):
    print("Smart Street Light System Started")

    while True:
        if not environment.update_environment():
            print("\nSystem Terminated.")
            break

        percept = environment.get_percept()
        action = agent.act(percept)

        print(f"Light Intensity: {percept[0]}, Motion: {percept[1]} → Action: {action}")


agent = SmartStreetLightAgent()
env = Environment()
run_agent(agent, env)
