import unittest
import pandas as pd
from src.algorithms import prep, pred, vis
from src.clust import distance_to_line


class TestAlgorithms(unittest.TestCase):
    """Test class for distance_to_line. Testing that the correct distance is returned."""

    def test_distance_to_line(self):
        p = pd.Series([1, 2])
        a = pd.Series([0, 0])
        b = pd.Series([3, 3])
        result = distance_to_line(p, a, b)
        expected_result = 0.7071067811865475
        self.assertAlmostEqual(result, expected_result)

    """Test case for the prep function. Testing that the model is not None and that the MSE is printed."""

    def test_prep(self):
        data = {
            "Start Year": [2020, 2021, 2022],
            "Start Month": [1, 2, 3],
            "Latitude": [34.05, 36.16, 40.71],
            "Longitude": [-118.25, -115.15, -74.00],
            "Total Deaths": [100, 200, 300],
        }
        df = pd.DataFrame(
            data,
        )
        result = prep(df)
        self.assertIsNotNone(result)
        return result

    """Test case for the pred function. Testing that the future_df is not None and that the MSE is printed."""

    def test_pred(self):
        data = {
            "Start Year": [2020, 2021, 2022],
            "Start Month": [1, 2, 3],
            "Latitude": [34.05, 36.16, 40.71],
            "Longitude": [-118.25, -115.15, -74.00],
            "Total Deaths": [100, 200, 300],
        }
        df = pd.DataFrame(
            data,
        )
        model = self.test_prep()
        future_df = pred(df, model)
        self.assertIsNotNone(future_df)


if __name__ == "main":
    unittest.main()
