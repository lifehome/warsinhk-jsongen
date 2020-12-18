import io
import os
import pandas as pd
import requests

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRTVp8L95wLd23_2CuA57V-lU6tCRhGAPWSCghGhBuV4xKV_XMVjniCEoDxZnBMXEJ2MPlAi6WzOxlp/pub?gid=0&single=true&output=csv"

# fetch the fucker
r = requests.get(URL, allow_redirects=True)

# override the encoding
r.encoding = "utf-8"

# Iterate the raw CSV data into Pandas DataFrame
csv_df = pd.DataFrame(pd.read_csv(
  io.StringIO(r.text), sep=",", header=0, index_col=None
))

# set index column
csv_df = csv_df.set_index("key")

# convert and save the json file
csv_df.to_json("data/site-i18n.json", force_ascii=False)