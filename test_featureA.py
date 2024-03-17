import unittest
from FeatureA import calculate_average_velocity

class TestCalculateAverageVelocity(unittest.TestCase):
    """
    Unit tests for calculating average sprint velocity in Feature A.
    """

    def test_with_multiple_sprint_points(self):
        """
        Test average velocity calculation with multiple sprint points.
        Should calculate the average correctly.
        """
        sprint_points = [10, 15, 20]
        result = calculate_average_velocity(sprint_points)
        self.assertEqual(result, 15)

    def test_with_empty_list(self):
        """
        Test average velocity calculation with an empty list of sprint points.
        Should handle empty list gracefully and return 0.0.
        """
        sprint_points = []
        result = calculate_average_velocity(sprint_points)
        self.assertEqual(result, 0.0)

    def test_with_single_sprint_point(self):
        """
        Test average velocity calculation with a single sprint point.
        Should return the point itself as the average.
        """
        sprint_points = [10]
        result = calculate_average_velocity(sprint_points)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
