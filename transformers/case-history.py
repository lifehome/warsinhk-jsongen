import io
import os
import pandas as pd
import requests

##                                                ##
# Table 1: Confirmed cases of Jan 2020 to Dec 2020 #
##                                                ##

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSr2xYotDgnAq6bqm5Nkjq9voHBKzKNWH2zvTRx5LU0jnpccWykvEF8iB_0g7Tzo2pwzkTuM3ETlr_h/pub?gid=0&single=true&output=csv"

# fetch the fucker
r = requests.get(URL, allow_redirects=True)

# override the encoding
r.encoding = "utf-8"

# Iterate the raw CSV data into Pandas DataFrame
csv_df_table1 = pd.DataFrame(pd.read_csv(
  io.StringIO(r.text), sep=",", header=0, index_col=None, skiprows=1
))

# drop disabled rows
csv_df_table1 = csv_df_table1[csv_df_table1.enabled == "Y"]

# drop specific columns
csv_df_table1.drop('enabled', inplace=True, axis=1)

# Normalize the integer format
csv_df_table1.dropna(subset=['case_no'], inplace=True)
csv_df_table1['case_no'] = csv_df_table1['case_no'].astype('float').astype('int')

##                                                ##
# Table 2: Confirmed cases of Jan 2021 to Dec 2021 #
##                                                ##

# set the fucker
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT-Xw-QHYydz_kJCJLBqTKGbb2OF8_gisdUsduPbdR6Dp3tLbWxy_mkfRx2tMmGJ0q64uNsLLv3bbfb/pub?gid=0&single=true&output=csv"

# fetch the fucker
r = requests.get(URL, allow_redirects=True)

# override the encoding
r.encoding = "utf-8"

# Iterate the raw CSV data into Pandas DataFrame
csv_df_table2 = pd.DataFrame(pd.read_csv(
  io.StringIO(r.text), sep=",", header=0, index_col=None, skiprows=1
))

# drop disabled rows
csv_df_table2 = csv_df_table2[csv_df_table2.enabled == "Y"]

# drop specific columns
csv_df_table2.drop('enabled', inplace=True, axis=1)

# Normalize the integer format
csv_df_table2.dropna(subset=['case_no'], inplace=True)
csv_df_table2['case_no'] = csv_df_table2['case_no'].astype('float').astype('int')

##                                      ##
# Join tables and export as JSON dataset #
##                                      ##

tables_array = [csv_df_table1, csv_df_table2]

final_table = pd.concat(tables_array)

# convert and save the json file
final_table.to_json("data/case-history.json", orient="records", force_ascii=False)