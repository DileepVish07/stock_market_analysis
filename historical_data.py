import pandas as pd
import os
import re
os.getcwd()
os.listdir('/Stock Market/historical_data')[0]

os.listdir('historical_data/Nifty_100_intraday_data')

import glob
print (glob.glob("Stock Market/historical_data/Nifty_100_intraday_data")[0])
jpgFilenamesList = glob.glob('/historical_data/Nifty_100_intraday_data/day_data*.csv')

jpgFilenamesList


# Get CSV files list from a folder
path = '/historical_data/Nifty_100_intraday_data/'

for py in glob.glob(path + "*.csv"):
    print(py)

csv_files = glob.glob(path + "*.csv")
csv_files

# Read each CSV file into DataFrame
# This creates a list of dataframes
df_list = (pd.read_csv(file) for file in csv_files)

# Concatenate all DataFrames
big_df   = pd.concat(df_list, ignore_index=True)


# This is working ######

files = [f for f in os.listdir('historical_data/Nifty_100_intraday_data') if re.search(r'day_data.csv', f)]

temp_df = []

for f in files:
    df = pd.read_csv("historical_data/Nifty_100_intraday_data/"+f, index_col=None, header=0)
    temp_df.append(df)

day_df = pd.concat(li, axis=0, ignore_index=True)

########################

test = "historical_data/Nifty_100_intraday_data/"+files[1]
pd.read_csv(test)

# print(("historical_data/Nifty_100_intraday_data/",files[1]).replace(" ", ""))

df_list = (pd.read_csv(f) for f in "historical_data/Nifty_100_intraday_data/" , files)

big_df   = pd.concat(df_list, ignore_index=True)

# df = pd.concat(map(pd.read_csv, "historical_data/Nifty_100_intraday_data"+files))

pd.read_csv(test)

files