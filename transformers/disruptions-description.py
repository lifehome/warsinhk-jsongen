import io
import os
import pandas as pd
import requests

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS0gZ-QBC6JGMS28kYUMz90ZNXFb40CtoLtOIC-QzzlqhPKCIrAojuuN2GX6AXaECONvxJd84tpqzFd/pub?gid=268131605&single=true&output=csv"

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
csv_df.to_json("data/disruption-description.json", orient="records", force_ascii=False)