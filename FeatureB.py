# This will be a list of dictionaries, with each dictionary representing a team member's details.
team_members = [
    {"name": "Alice", "pto_hours": 8, "ceremony_hours": 2, "daily_hours": 8},
    {"name": "Bob", "pto_hours": 0, "ceremony_hours": 2, "daily_hours": 8},
    
]

def input_team_member_details():
    """
    Interactively collects team member details.
    Returns:
        List of dictionaries, each containing details of a team member.
    """
    team_members = []
    print("Enter team member details. Type 'done' when you finish adding members.")

    while True:
        name = input("Team member's name (or type 'done'): ")
        if name.lower() == 'done':
            break

        try:
            pto_hours = float(input(f"Enter PTO hours for {name}: "))
            ceremony_hours = float(input(f"Enter hours committed to sprint ceremonies for {name}: "))
            daily_hours = float(input(f"Enter available hours per day for {name}: "))
            team_members.append({
                "name": name,
                "pto_hours": pto_hours,
                "ceremony_hours": ceremony_hours,
                "daily_hours": daily_hours
            })
        except ValueError:
            print("Please enter valid numbers for hours.")

    return team_members

def calculate_effort_hours(team_members, sprint_days):
    """
    Calculates the total available effort-hours for the team and per person.
    Args:
        team_members: List of dictionaries with each team member's details.
        sprint_days: Integer representing the number of days in the sprint.
    Returns:
        A tuple containing total team effort-hours and a dictionary of individual effort-hours.
    """
    total_team_effort_hours = 0
    individual_effort_hours = {}

    for member in team_members:
        available_hours = (sprint_days * member["daily_hours"]) - member["pto_hours"] - member["ceremony_hours"]
        individual_effort_hours[member["name"]] = available_hours
        total_team_effort_hours += available_hours

    return total_team_effort_hours, individual_effort_hours


def main():
    sprint_days = int(input("Enter the number of sprint days: "))
    team_members = input_team_member_details()
    total_team_effort_hours, individual_effort_hours = calculate_effort_hours(team_members, sprint_days)

    print(f"\nTotal Team Effort-Hours: {total_team_effort_hours}")
    for name, hours in individual_effort_hours.items():
        print(f"{name}: {hours} available effort-hours")

if __name__ == "__main__":
    main()
