import unittest
import numpy as np
import os
import pandas as pd
from src.data_processor import getCountry, load_disaster, updateCoords, checkCoords

TEST_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "../data/generated_data/NaturalDisasters1900-2025WithCoords.csv"
)


class Test_Data_Processor(unittest.TestCase):
    """Test case for the CheckCoords function. Testing that the proper number of coordinate pairs are found."""

    def test_CheckCoords(self):
        countrydata = {
            "name": ["Botswana", "Belarus", "Greece", "Saint Barthélemy"],
            "Latitude": [-22.328474, np.nan, 39.074208, np.nan],
            "Longitude": [24.684866, np.nan, 21.824312, 62.8333],
        }

        countrydf = pd.DataFrame(countrydata)
        val = (("Pairs:", 2), ("Only Long", 1), ("Only Lat", 0), ("Nothing", 1))
        self.assertEqual(checkCoords(countrydf), val)

        countrydata = {
            "name": ["Botswana", "Belarus", "Greece", "Saint Barthélemy"],
            "Latitude": [-22.328474, 53.709807, 39.074208, 17.9000],
            "Longitude": [24.684866, 27.953389, 21.824312, 62.8333],
        }
        countrydf = pd.DataFrame(countrydata)

        val = (("Pairs:", 4), ("Only Long", 0), ("Only Lat", 0), ("Nothing", 0))
        self.assertEqual(checkCoords(countrydf), val)

    """Test case for GetCountry function. Testing that the correct coordinates are returned for a given country."""

    def test_GetCountry(self):
        countrydata = {
            "name": ["Botswana", "Canary Islands", "Greece", "Saint Barthélemy"],
            "latitude": [-22.328474, 28.2916, 39.074208, 0],
            "longitude": [24.684866, 16.6291, 21.824312, 0],
        }

        countrydf = pd.DataFrame(countrydata)

        data = {
            "Country": ["Botswana", "Canary Islands", "Greece", "Saint Barthélemy"],
            "Latitude": [-22.328474, 28.2916, 39.074208, 17.9000],
            "Longitude": [24.684866, 16.6291, 21.824312, 62.8333],
        }

        df = pd.DataFrame(data)
        for item in df.iterrows():
            row = item[1]
            country = row["Country"]
            res = getCountry(countrydf, country)
            self.assertEqual(row["Longitude"], res[1])
            self.assertEqual(row["Latitude"], res[0])

    """Test case for the updateCoords function. Testing that the coordinates are updated correctly."""

    def test_load_disaster(self):
        df = load_disaster(
            "Earthquake",
            [
                "Disaster Type",
                "Start Year",
                "Start Month",
                "Latitude",
                "Longitude",
                "Total Deaths",
            ],
            file=TEST_FILE_PATH,
        )
        self.assertIsNotNone(df)


if __name__ == "main":
    unittest.main()
