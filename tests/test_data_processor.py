import unittest
import pandas as pd
from src.data_processor import getCountry, getData



# class Test_Data_Processor(unittest.TestCase):
#     def test_GetCountry(self):
#         countrydf = getData("../data/CountryData.csv")
#         data = {
#             "Country": ['Botswana','Belarus', 'Greece'],
#             "Latitude": [-22.328474, 53.709807, 39.074208],
#             "Longitude": [24.684866,27.953389, 21.824312]
#         }
#
#
#         df = pd.DataFrame(data)
#         for item in df.iterrows():
#             row = item[1]
#             country = row['Country']
#             res = getCountry(countrydf, country)
#             self.assertEqual(row['Longitude'], res[0])
#             self.assertEqual(row['Latitude'], res[0])

if __name__ == 'main':
    unittest.main()

