task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
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
case _:
reminder = f"'{task}' has an unknown priority level."
print(reminder)
