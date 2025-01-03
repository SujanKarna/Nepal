import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Area and land use by province")
st.markdown("---")
# Data import
df = pd.read_csv("assets/data/Area and land use by province.csv")

#Dataset details
st.markdown("Dataset")
st.dataframe(data=df,width=None,hide_index=True)
st.markdown("Source:https://opendatanepal.com/dataset/environment-statistics-of-nepal-2024/resource/74b3845b-549d-41c1-9f05-9304089b2254")

st.write("")
st.markdown("---")
#Pie chart of total areas occupied by each provience
labels = df['Province'].iloc[:-1]
values = df['Total'].iloc[:-1]

fig = go.Figure(data=[go.Pie(labels=labels, values=values,textinfo='label+percent', hole=.3)])
fig.update_layout(width=700,height=700,title_text='Total area occupied by Province')
st.plotly_chart(fig)