def main():

    task_description = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    task_timebound = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            if task_timebound == "yes":
                print(f"Reminder: {task_description} is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: {task_description} is a low priority task. Consider completing it when you have free time.")
        case "medium":
            if task_timebound == "yes":
                print(f"Reminder: {task_description} is a {priority} priority task that requires immediate attention today!")
            else:
                print(f"Note: {task_description} is a {priority} priority task. Consider completing it when you have free time.")
        case "low":
            if task_timebound == "yes":
                print(f"Reminder: {task_description} is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: {task_description} is a low priority task. Consider completing it when you have free time.")
            
    return

if __name__ == "__main__":
    main()



#     Instructions:

# Prompt for a Single Task:

# Ask the user to input a task description and save it into a task variable
# Prompt for the task’s priority (high, medium, low) and save it into a priority variable
# In a time_bound variable, Ask if the task is time-bound (yes or no)
# Process the Task Based on Priority and Time Sensitivity:

# Use a Match Case statement to react differently based on the task’s priority.
# Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
# Provide a Customized Reminder:

# Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
# A message should be ‘that requires immediate attention today!’
# Enter your task: Finish project report
# Priority (high/medium/low): high
# Is it time-bound? (yes/no): yes

# Reminder: 'Finish project report' is a high priority task that requires immediate attention today!