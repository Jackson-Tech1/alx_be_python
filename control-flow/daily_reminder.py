task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
<<<<<<< HEAD

# Generate the customized reminder message
if priority in ["high", "medium"]:
    reminder = f"Reminder: '{task}' is a {priority} priority task"
    if time_bound == "yes":
=======
reminder = ""
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"
if time_bound == "yes":
    if priority in ["high", "medium"]:
>>>>>>> 57cf2db7d7ace0da9913706e5b2b5675b3e22347
        reminder += " that requires immediate attention today!"
elif priority == "low":
    reminder = f"Note: '{task}' is a low priority task"
    if time_bound == "yes":
        reminder += " that requires attention soon."
<<<<<<< HEAD
    else:
        reminder += ". Consider completing it when you have free time."
else:
    reminder = f"'{task}' has an unknown priority level"

# Print the customized reminder
=======
elif time_bound == "no" and priority == "low":
    reminder += ". Consider completing it when you have free time."
>>>>>>> 57cf2db7d7ace0da9913706e5b2b5675b3e22347
print(reminder)
