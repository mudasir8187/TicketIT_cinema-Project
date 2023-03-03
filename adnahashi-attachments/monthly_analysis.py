import pandas as pd
from datetime import datetime

# Read the ticket_prep.dat file into a DataFrame
df = pd.read_csv('ticketit_prep_dat.csv')

# Convert the booking date column to a datetime object
df['bkg_date'] = pd.to_datetime(df['bkg_date'])

# Filter the DataFrame to keep only the records with a booking date in 2022
df = df[df['bkg_date'].dt.year == 2022]

# Create a new column for the month of the booking date
df['month_num'] = df['bkg_date'].dt.month
df['month'] = df['month_num'].apply(lambda x: datetime.strptime(str(x), "%m").strftime("%b"))

# Group the DataFrame by month and genre and count the number of bookings
grouped_df = df.groupby(['month', 'genre']).size().reset_index(name='count')

# Reshape the resulting DataFrame to long format
melted_df = pd.melt(grouped_df, id_vars=['month', 'genre'], value_vars=['count'],  value_name='value')

# Change column order
melted_df = melted_df[['month', 'genre', 'value']]

# Pivot the table to have months as columns and genres as rows
pivoted_df = melted_df.pivot(index='genre', columns='month', values='value')

# Write the resulting DataFrame to a CSV file
pivoted_df.to_csv('month_genre.csv')