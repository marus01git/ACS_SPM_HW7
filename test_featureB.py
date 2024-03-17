import unittest
from FeatureB import calculate_effort_hours

class TestCalculateEffortHours(unittest.TestCase):
    """
    Unit tests for calculating effort hours in Feature B.
    """

    def test_with_multiple_members(self):
        """
        Test effort hour calculation with multiple team members.
        Should calculate total and individual effort hours correctly.
        """
        team_members = [
            {"name": "Alice", "pto_hours": 8, "ceremony_hours": 2, "daily_hours": 8},
            {"name": "Bob", "pto_hours": 0, "ceremony_hours": 2, "daily_hours": 8},
        ]
        sprint_days = 10
        total_hours, individual_hours = calculate_effort_hours(team_members, sprint_days)
        self.assertEqual(total_hours, 148)
        self.assertEqual(individual_hours, {"Alice": 70, "Bob": 78})

    def test_with_no_members(self):
        """
        Test effort hour calculation with no team members.
        Should return 0 total hours and an empty dictionary for individual hours.
        """
        team_members = []
        sprint_days = 10
        total_hours, individual_hours = calculate_effort_hours(team_members, sprint_days)
        self.assertEqual(total_hours, 0)
        self.assertEqual(individual_hours, {})

    def test_with_member_pto_and_ceremonies(self):
        """
        Test effort hour calculation for a member with PTO and ceremony hours.
        Should correctly subtract PTO and ceremony hours from total available hours.
        """
        team_members = [
            {"name": "Charlie", "pto_hours": 16, "ceremony_hours": 4, "daily_hours": 8},
        ]
        sprint_days = 10
        total_hours, individual_hours = calculate_effort_hours(team_members, sprint_days)
        self.assertEqual(total_hours, 60)
        self.assertEqual(individual_hours, {"Charlie": 60})

if __name__ == '__main__':
    unittest.main()
