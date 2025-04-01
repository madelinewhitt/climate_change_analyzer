import requests
import json
import os
import io
from dotenv import load_dotenv, dotenv_values
import pandas as pd

load_dotenv()


def interact_api():
    # URL of the IBTrACS dataset (Global CSV)
    url = "https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r00/access/csv/ibtracs.ALL.list.v04r00.csv"

    # Download file
    response = requests.get(url)

    if response.status_code == 200:
        print("Response status code:", response.status_code)
        # Load dataset into Pandas using StringIO
        df = pd.read_csv(io.StringIO(response.text), low_memory=False)

        # Display first 5 rows
        print(df.head())
    else:
        print(f"Error {response.status_code}: Unable to fetch data.")


# Call the function
interact_api()
