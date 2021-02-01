import io
import os
import pandas as pd
import requests

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQS7Aay-dZbemZAxbW1oVrC5QKnT9wPjd55hSGGnXGj8_jdZJa9dsKYI--dTv4EU--xt_HGIDZsdNEw/pub?gid=0&single=true&output=csv"

# fetch the fucker
r = requests.get(URL, allow_redirects=True)

# override the encoding
r.encoding = "utf-8"

# Iterate the raw CSV data into Pandas DataFrame
csv_df = pd.DataFrame(pd.read_csv(
  io.StringIO(r.text), sep=",", header=0, index_col=None, skiprows=1
))

# drop disabled rows
csv_df = csv_df[csv_df.enabled == "Y"]

# drop specific columns
csv_df.drop('enabled', inplace=True, axis=1)

# strip all whitespace in case_no
csv_df["case_no"] = csv_df["case_no"].str.replace(" ", "")

# split case_no into array
csv_df["case_no"] = csv_df["case_no"].str.split(",")

# select specific columns
csv_df = csv_df[["case_no", "name_zh", "name_en", "description_zh", "description_en"]]

# convert and save the json file
csv_df.to_json("data/case-relationship.json", orient="records", force_ascii=False)