

# Subtask A1: Define a Data Structure for Storing Sprint Points
# This will be a simple list to store points from each sprint.

sprint_points = [10, 12, 8, 14]  # Example data

# Subtask A2: Implement a function to input previous sprints' points

def input_sprint_points():
    """
    Interactively collects sprint points from the user.
    Returns:
        List of integers representing sprint points.
    """
    sprint_points = []
    print("Enter the points for each sprint completed, type 'done' to finish:")
    while True:
        input_point = input("Sprint points: ")
        if input_point.lower() == 'done':
            break
        try:
            points = int(input_point)
            sprint_points.append(points)
        except ValueError:
            print("Please enter a valid integer or 'done' to finish.")
    return sprint_points

def main():
    sprint_points = input_sprint_points()

if __name__ == "__main__":
    main()
