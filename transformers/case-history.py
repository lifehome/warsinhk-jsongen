import io
import os
import pandas as pd
import requests

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSr2xYotDgnAq6bqm5Nkjq9voHBKzKNWH2zvTRx5LU0jnpccWykvEF8iB_0g7Tzo2pwzkTuM3ETlr_h/pub?gid=0&single=true&output=csv"

# fetch the fucker
r = requests.get(URL, allow_redirects=True)

# override the encoding
r.encoding = "utf-8"

# Iterate the raw CSV data into Pandas DataFrame
csv_df = pd.DataFrame(pd.read_csv(
  io.StringIO(r.text), sep=",", header=0, index_col=None, skiprows=1
))

# drop specific columns
csv_df.drop('enabled', inplace=True, axis=1)

# Normalize the integer format
csv_df.dropna(subset=['case_no'], inplace=True)
csv_df['case_no'] = csv_df['case_no'].astype('int')

# convert and save the json file
csv_df.to_json("data/case-history.json", orient="records", force_ascii=False)