# TASK -- 4

# 1 — Setup
# Loading into the data frame
import pandas as pd
df = pd.read_csv('data/trends_analysed.csv')

# Creating a folder
import os
os.makedirs('outputs/',exist_ok = True)

# 2 — Chart 1: Top 10 Stories by Score (Bar chart)
import matplotlib.pyplot as plt

top_10= df.sort_values(by = 'score', ascending = False).head(10)

# shortening the titles
top_10["short_title"] = top_10["title"].str[:50] + "..."

plt.figure()

plt.barh(top_10['short_title'],top_10['score'],color = 'lightblue',edgecolor = 'black')
plt.xlabel('Score')
plt.ylabel('Title')
plt.title('Top 10 stories by score')

# Save before showing
plt.savefig('outputs/chart1_top_stories.png')

plt.show()


# 3 — Chart 2: Stories per Category

category_count = df['category'].value_counts()

plt.figure(figsize = (12,5))
plt.bar(category_count.index, category_count.values,
        color='lightgreen', edgecolor='black', width = 0.375)
plt.title('Stories per Category')
plt.xlabel('Category')
plt.ylabel('No of Stories')
plt.grid(axis='y', alpha=0.3)

plt.savefig('outputs/chart2_categories.png')

plt.show()


# Chart 3: Score vs Comments, i used seaborn for this plot
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.scatterplot(x='score', y='num_comments', data=df,
                hue = 'is_popular',s = 70, alpha = 0.9)
plt.xlabel('Score',fontsize = 12)
plt.ylabel('No of comments',fontsize = 12)
plt.title('Scatter plot between Score and Comments',fontsize = 14)
plt.grid(True,alpha = 0.3)

# saving before displaying 
plt.savefig('outputs/chart3_scatter.png')
plt.show()


# BONUS — Dashboard 

plt.figure(figsize=(18, 5))

# Chart 1
plt.subplot(1, 3, 1)
plt.barh(top_10['short_title'], top_10['score'],
         color='skyblue', edgecolor='black')
plt.title('Top 10 Stories by Score')
plt.xlabel('Score')
plt.ylabel('Title')
plt.grid(axis='x', alpha=0.3)

# Chart 2 
plt.subplot(1, 3, 2)
plt.bar(category_count.index, category_count.values,
        color='lightgreen', edgecolor='black')
plt.title('Stories per Category')
plt.xlabel('Category')
plt.ylabel('No of Stories')
plt.grid(axis='y', alpha=0.3)

# Chart 3 
plt.subplot(1, 3, 3)
sns.scatterplot(x='score', y='num_comments',
                data=df, hue='is_popular', s=70, alpha=0.9)
plt.title('Scatter Plot between Score and Comments')
plt.xlabel('Score')
plt.ylabel('Comments')
plt.grid(alpha=0.3)

plt.suptitle('TrendPulse Dashboard')

plt.tight_layout()

# save
plt.savefig('outputs/dashboard.png')

plt.show()



