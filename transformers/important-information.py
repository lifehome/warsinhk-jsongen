import io
import os
import pandas as pd
import requests

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vShepjZrGpn8QlN8R3QFrIVhWLg9l0F99wYR9khAnhmoydOP7hkS2_L1imCjH9nHkqVQf3xGrUAi8Na/pub?gid=257173560&single=true&output=csv"

# fetch the fucker
r = requests.get(URL, allow_redirects=True)

# override the encoding
r.encoding = "utf-8"

# Iterate the raw CSV data into Pandas DataFrame
csv_df = pd.DataFrame(pd.read_csv(
  io.StringIO(r.text), sep=",", header=0, index_col=None, skiprows=1
))

# Drop rows that are disabled
csv_df = csv_df[csv_df.enabled == "Y"]

# drop specific columns
csv_df.drop('enabled', inplace=True, axis=1)

# pick specific column
csv_df = csv_df[["order", "type", "text_zh", "text_en"]]

# convert and save the json file
csv_df.to_json("data/important-information.json", orient="records", force_ascii=False)