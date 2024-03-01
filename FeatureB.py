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

def main():
    sprint_days = int(input("Enter the number of sprint days: "))
    team_members = input_team_member_details()

 
if __name__ == "__main__":
    main()
