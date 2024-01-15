import pandas as pd
import os
import re

# This is working ######

files = [f for f in os.listdir('historical_data/Nifty_100_intraday_data') if re.search(r'day_data.csv', f)]

temp_df = []

for f in files:
    df = pd.read_csv("historical_data/Nifty_100_intraday_data/"+f, index_col=None, header=0)
    df['symbol_frequency'] = f[:-9]
    df['symbol'] = df['symbol_frequency'].str.split('_').str[0]
    temp_df.append(df)

day_df = pd.concat(temp_df, axis=0, ignore_index=True)

# check
day_df.head()

# check
day_df[day_df['symbol_frequency'] == 'NIFTY BANK_day'].head()

########################