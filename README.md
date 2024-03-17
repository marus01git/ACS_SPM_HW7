# ACS_HW6

# Sprint Planning and Execution - Feature A and B

## Feature A: Calculate a Sprint Team’s Velocity

### Code Logic
- Collect an array of integers where each integer represents the points completed in a previous sprint. Calculate the average of these points to determine the team's average velocity.

### Inputs
- A list of integers, with each integer representing the sprint points completed in a previous sprint. These are historical data points indicating the output of the team for each past sprint.


### Output
- A single float value representing the average sprint velocity. This is an average rate of work the team can accomplish in a sprint and is used for planning and forecasting future sprints.


## Feature B: Calculate Team Effort-Hour Capacity

### Code Logic
- For each team member, input details regarding their availability and commitments during the sprint. 
Calculate the available effort-hours per person by subtracting the hours taken off (PTO) and hours committed to sprint ceremonies from the total hours available (sprint days multiplied by daily hours).
Sum the effort-hours for all team members to find the total team effort-hours.

### Inputs
- **Number of Sprint Days (Integer):** The total number of days in the sprint.
- **Team Member Details (List of Dictionaries):**
  - **PTO (Paid Time Off in Hours):** The number of hours a team member is taking off during the sprint.
  - **Sprint Ceremonies (Hours):** The number of hours a team member will spend in sprint-related ceremonies for the whole sprint.
  - **Daily Hours (Hours/Day):** The number of hours per day a team member is available to work on sprint tasks.

### Outputs
- **Available Effort-Hours/Person (Float):** The total number of hours each team member is available to contribute to sprint tasks accounting for PTO and sprint ceremony commitments.
- **Available Effort-Hours for Team (Float):** The sum of all available effort-hours from all team members, providing a total capacity for what the team can accomplish in terms


