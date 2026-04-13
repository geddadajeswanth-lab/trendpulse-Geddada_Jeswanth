# TASK - 3

# 1 — Load and Explore
import pandas as pd
df_data = pd.read_csv('data/trends_clean.csv')

# printing top 5 records
print(df_data.head(5))

# shape
print(f'Loaded data : {df_data.shape}')

# printing the abg score and avg num_comments 
print(f'\nAverage score : {df_data['score'].mean():.2f}')
print(f'Average comments {df_data['num_comments'].mean():.2f}')

# 2 — Basic Analysis with NumPy 

import numpy as np
# saving the scores of all stories 
scores = np.array(df_data['score'])

# applying numpy operations
mean = np.mean(scores)
median = np.median(scores)
std = np.std(scores)

print('\n','\n--- NumPy Stats ---')
print(f'Mean Score : {mean:.3f}')
print(f'Median Score : {median:.3f}')
print(f'Std deviation : {std:.3f}')

#  Finding Highest and Lowest scores
max_score = np.max(scores)
min_score = np.min(scores)

print(f"Max score: {max_score}")
print(f"Min score: {min_score}")

# Categories with most stories
categories = np.array(df_data['category'])

# Now getting the unique values 
unique , counts = np.unique(categories, return_counts = True)

# Finding the index of maximum count
max_count = np.max(counts)
most_repeted_category = unique[counts == max_count]

print(f'\nCategory with most stories : {most_repeted_category}')

# story with most comments
comments = np.array(df_data['num_comments'])
index = np.argmax(comments)
print(f'\nMost commented story : {df_data['title'].iloc[index]} - {df_data['num_comments'].iloc[index]} comments')

# 3 — Add New Columns 
# Adding new columns
df_data['engagement'] = df_data['num_comments']/(df_data['score'] + 1)

df_data['is_popular'] = df_data['score'] > df_data['score'].mean()

# 4 — Save the Result 

output_file = "data/trends_analysed.csv"

# save dataframe
df_data.to_csv(output_file, index=False)

# confirmation message
print(f"\nSaved to {output_file}")