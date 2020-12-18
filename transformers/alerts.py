import io
import os
import pandas as pd
import requests

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRWN6o99FDJN4KsnAyq9KeWKEerF2_v1Z0wWbKiHPI0_Whuf00ZLW2n-GfoXciKgVXkBSoBEz6IhreC/pub?gid=0&single=true&output=csv"

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

# convert and save the json file
csv_df.to_json("data/alerts.json", orient="records", force_ascii=False)