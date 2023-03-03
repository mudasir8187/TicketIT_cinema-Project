import os
import glob
import pandas as pd

# set the directory containing CSV files
csv_dir = 'C:/Users/chmud/Downloads/adnahashi-attachments'       # Here you will insert your own path

# set the pattern to match CSV files
pattern = '*.csv'

# get a list of CSV files in the directory
csv_files = glob.glob(os.path.join(csv_dir, pattern))

# create an empty list to hold the data frames
df_list = []

# loop through the CSV files
for csv_file in csv_files:
    # read the CSV file into a data frame
    df = pd.read_csv(csv_file)
    # add the data frame to the list
    df_list.append(df)

# concatenate the data frames into a single data frame
merged_df = pd.concat(df_list, axis=1)

# write the merged data frame to a CSV file
merged_df.to_csv('C:/Users/chmud/Downloads/adnahashi-attachments/ticketit_prep.csv', index=False)      # Here you will insert your own path



df = pd.read_csv('ticketit_prep.csv')
df.drop(['price', 'showing_id', 'id.1', 'fname', 'lname', 'dob', 'contact', 'adr', 'id.2', 'film', 'id.3', 'name', 'id.4', 'venue_id', 'loc_id', 'date', 'seats', 'f_bkd', 'price.1'], axis=1, inplace=True)
df.to_csv('ticketit_prep_dat.csv', index=False)
