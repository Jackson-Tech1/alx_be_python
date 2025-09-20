task = input("Enter your task: ").strip()

# Prompt for priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate the customized reminder message
if priority in ["high", "medium"]:
    reminder = f"Reminder: '{task}' is a {priority} priority task"
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
elif priority == "low":
    reminder = f"Note: '{task}' is a low priority task"
    if time_bound == "yes":
        reminder += " that requires attention soon."
    else:
        reminder += ". Consider completing it when you have free time."
else:
    reminder = f"'{task}' has an unknown priority level"

# Print the customized reminder
print(reminder)
