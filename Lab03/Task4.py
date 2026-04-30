class Environment:
    def __init__(self):
        self.optionA = {"time": 2, "cost": 10}  
        self.optionB = {"time": 5, "cost": 5}    

    def get_options(self):
        return self.optionA, self.optionB


class ShoppingAssistant:
    def __init__(self, time_weight, cost_weight):
        self.time_weight = time_weight
        self.cost_weight = cost_weight

    def calculate_utility(self, option):
        return (self.time_weight * (1 / option["time"])) + \
               (self.cost_weight * (1 / option["cost"]))

    def act(self, options):
        utilityA = self.calculate_utility(options[0])
        utilityB = self.calculate_utility(options[1])

        if utilityA > utilityB:
            return "Option A (Fast Delivery)"
        else:
            return "Option B (Cheap Delivery)"


env = Environment()
options = env.get_options()

customers = [
    {"name": "Customer 1", "time_weight": 0.7, "cost_weight": 0.3},  
    {"name": "Customer 2", "time_weight": 0.5, "cost_weight": 0.5}, 
    {"name": "Customer 3", "time_weight": 0.3, "cost_weight": 0.7},  
]

print("Utility-Based Shopping Assistant for Multiple Customers\n")
print("Option A:", options[0])
print("Option B:", options[1])
print()

for c in customers:
    agent = ShoppingAssistant(c["time_weight"], c["cost_weight"])
    decision = agent.act(options)
    print(f"{c['name']} (Time weight: {c['time_weight']}, Cost weight: {c['cost_weight']}) → Selected: {decision}")
