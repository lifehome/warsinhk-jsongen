import io
import os
import pandas as pd
import requests

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRrwN4gNtogizNkYKGzMXpa7GTNJhE_vkZuYiFraU7f-N7ZKiT-araG-0jb586kczxc9Ua6oht8SVcE/pub?gid=0&single=true&output=csv"

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
csv_df.to_json("data/friendly-links.json", orient="records", force_ascii=False)