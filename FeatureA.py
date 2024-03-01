# Subtask A1: Define a Data Structure for Storing Sprint Points
# This will be a simple list to store points from each sprint.

sprint_points = [10, 12, 8, 14]  # Example data

# Subtask A2: Implement the Calculation Logic for Average Velocity

def calculate_average_velocity(sprint_points):
    if not sprint_points:
        return 0
    return sum(sprint_points) / len(sprint_points)

# Example usage:
average_velocity = calculate_average_velocity(sprint_points)
print(f"Average Velocity: {average_velocity}")