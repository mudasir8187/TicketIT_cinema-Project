import pandas as pd
import numpy as np

# read the CSV file
df = pd.read_csv('ticketit_prep_dat.csv')

# convert the 'rating' column to floats
df['film_rating'] = pd.to_numeric(df['film_rating'], errors='coerce')

# round the ratings to the nearest integer and add 0.5
df['rounded_rating'] = np.floor(df['film_rating']) + 0.5

# create a new dataframe to store the output
output_df = pd.DataFrame(columns=['seg', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

# iterate over each segment in the original dataframe
for seg in df['cust_seg'].unique():
    # count the number of ratings for each rounded score (0-10)
    rounded_ratings = df[df['cust_seg'] == seg]['rounded_rating'].value_counts().sort_index()
    
    # create a new row for the output dataframe
    new_row = {'seg': seg}
    for i in range(11):
        # if the rounded score has no ratings, set the count to 0
        if (i + 0.5) not in rounded_ratings.index:
            new_row[str(i)] = 0
        else:
            new_row[str(i)] = rounded_ratings[i + 0.5]
    
    # add the new row to the output dataframe
    output_df = output_df.append(new_row, ignore_index=True)

# print the output dataframe
print(output_df.to_string(index=False))
output_df.to_csv('rating_analysis.csv', index=False)