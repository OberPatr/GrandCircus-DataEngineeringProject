#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the data from a CSV file
data = pd.read_csv('/Users/patrickoberly/Desktop/Combined_Version_3.csv')

# Remove duplicates and NaN values from the 'Skills' column
skills = data['Skills'].drop_duplicates().dropna()

# Convert the 'Skills' column to string
skills_str = ' '.join(skills.astype(str))

# Create a word cloud object
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      min_font_size=10).generate(skills_str)

# Display the generated image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
  
plt.show()

