task = input("Enter your task: ").strip()

# Prompt for priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize reminder message
reminder = ""

# Match-case to handle priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Use if statement to modify the reminder if the task is time-bound
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    elif priority == "low":
        reminder += " that requires attention soon."
elif time_bound == "no" and priority == "low":
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print(reminde
