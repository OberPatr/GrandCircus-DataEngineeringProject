#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import plotly.express as px
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('/Users/patrickoberly/Desktop/Combined_Version_3.csv')

# Get the count of results per website
count_data = data['Job Website'].value_counts().reset_index()
count_data.columns = ['Job Website', 'Count']

# Create the treemap chart
fig = px.treemap(count_data, path=['Job Website'], values='Count',
                 color='Job Website', color_discrete_map={'Indeed': 'blue'})

# Customize the font and color
fig.update_traces(textfont_size=16, textfont_color='white')

# Show the chart
fig.show()

