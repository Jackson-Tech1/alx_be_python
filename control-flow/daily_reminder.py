task = input("Enter your task: ").strip()
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid input. Please enter 'high', 'medium', or 'low'.")
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input. Please enter 'yes' or 'no'.")
match priority:
    case "high" | "medium":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a {priority} priority task."
    case "low":
        if time_bound == "yes":
reminder = f"Note: '{task}' is a low priority task that requires attention soon."
else:
reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
print(reminder)
