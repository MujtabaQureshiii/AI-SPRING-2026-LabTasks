import math

def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def delivery_optimizer(start, jobs):

    time_now = 0
    current = start
    completed = []

    tasks = jobs.copy()

    while tasks:

        best_choice = None
        best_score = float('inf')

        for job in tasks:

            travel = distance(current, job["point"])
            arrival = time_now + travel

            if arrival > job["deadline"]:
                continue

            urgency = job["deadline"] - arrival

            score = travel + (1/(urgency+1))*10

            if score < best_score:
                best_score = score
                best_choice = job

        if best_choice is None:
            print("Delivery failed due to time constraint")
            return None

        travel = distance(current, best_choice["point"])
        time_now += travel

        if time_now < best_choice["start"]:
            time_now = best_choice["start"]

        print(f"Delivered at {best_choice['point']} at time {time_now}")

        completed.append(best_choice["point"])
        current = best_choice["point"]
        tasks.remove(best_choice)

    print("Final_Route:", completed)
    print("Total_Time:", time_now)
    return completed


orders = [
    {"point":(2,5),"start ":0,"deadline":9},
    {"point":(6,2),"start":1,"deadline":12},
    {"point":(3,7),"start":4,"deadline":8},
    {"point":(8,3),"start":3,"deadline":15}
]

delivery_optimizer((0,0), orders)
