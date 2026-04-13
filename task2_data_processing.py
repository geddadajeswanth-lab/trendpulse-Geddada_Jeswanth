# TASK -- 2

# 1 — Load the JSON File
import json
import pandas as pd

# opening the json file
with open(filename,'r') as f:   # here we can use the file name directly also like data/trends_20260410.json
    data = json.load(f)

# converting into a data frame
df = pd.DataFrame(data)
print(f'\nThe loaded stories are of size {len(df)}')



# 2 — Clean the Data

# checking duplicates and removing them
df = df.drop_duplicates(subset = 'post_id')
print(f'\nLength of the data frame after removing duplicates {len(df)}')

# Checking missing values
df.isnull().sum()
# Actually i did'nt found out any missing values 
# if there by any chance ,to drop them
df = df.dropna(subset = ['post_id','title','score'])

# Data type
df.info()  # First check the data types of every row
df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)

# Low quality records
df = df[df['score'] >= 5]
print(f'\nLength of the data frame after removing low quality records {len(df)}')

#  Removing white spaces
df['title'] = df['title'].astype(str).str.strip()


# 3 — Save as CSV

# Saving the df into a csv file
output = 'data/trends_clean.csv'
df.to_csv(output,index = False)

print(f'\nsaved {len(df)} cleaned stories to {output}')

# Displaying stories per categories
print(f'\nStories per category:')
print(df['category'].value_counts())