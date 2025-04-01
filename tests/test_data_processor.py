import unittest
import pandas as pd
from src.data_processor import getCountry, getData


class Test_Data_Processor(unittest.TestCase):
    def test_GetCountry(self):
        # if country == "Saint Barthélemy":
        #     return(17.9000,62.8333)

        countrydata = {
            "name": ["Botswana", "Belarus", "Greece", "Saint Barthélemy"],
            "latitude": [-22.328474, 53.709807, 39.074208, 17.9000],
            "longitude": [24.684866, 27.953389, 21.824312, 62.8333],
        }

        countrydf = pd.DataFrame(countrydata)
        data = {
            "Country": ["Botswana", "Belarus", "Greece", "Saint Barthélemy"],
            "Latitude": [-22.328474, 53.709807, 39.074208, 17.9000],
            "Longitude": [24.684866, 27.953389, 21.824312, 62.8333],
        }

        df = pd.DataFrame(data)
        for item in df.iterrows():
            row = item[1]
            country = row["Country"]
            res = getCountry(countrydf, country)
            self.assertEqual(row["Longitude"], res[1])
            self.assertEqual(row["Latitude"], res[0])


if __name__ == "main":
    unittest.main()
