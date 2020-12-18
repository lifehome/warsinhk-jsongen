import io
import os
import pandas as pd
import requests

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQc-XdUlx2VuIqZ71qze1Mg5m11OwA8wL5fYLdlU1VC1PcEqrRrKL6fL5_FbtihOtmeAi7t1puDXOvG/pub?gid=0&single=true&output=csv"

# fetch the fucker
r = requests.get(URL, allow_redirects=True)

# override the encoding
r.encoding = "utf-8"

# Iterate the raw CSV data into Pandas DataFrame
csv_df = pd.DataFrame(pd.read_csv(
  io.StringIO(r.text), sep=",", header=0, index_col=None, skiprows=1
))

# drop empty column by date
csv_df.dropna(subset=['date'], inplace=True)

# pick specific column
csv_df = csv_df[["date", "confirmed", "probably", "death", "discharged", "hospitalised", "bed_number", "bed_percent", "room_number", "room_percent", "reported", "ruled_out", "investigating"]]

# convert and save the json file
csv_df.to_json("data/latest-figures.json", orient="records", force_ascii=False)