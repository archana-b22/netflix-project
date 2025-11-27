import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Netflix Dashboard", layout="wide")

st.title("🎬 Netflix Data Dashboard")
st.write("Interactive dashboard built using Streamlit")

# Load the cleaned dataset
df = pd.read_csv("./data/clean/netflix_cleaned.csv")

# ---- Sidebar Filters ----
st.sidebar.header("Filters")

types = df['type'].unique()
selected_type = st.sidebar.multiselect("Select Type", types, default=types)

countries = df['country'].unique()
selected_country = st.sidebar.multiselect("Select Country", countries, default=countries)

filtered_df = df[
    (df['type'].isin(selected_type)) &
    (df['country'].isin(selected_country))
]

# ---- Metrics ----
col1, col2, col3 = st.columns(3)

col1.metric("Total Titles", len(filtered_df))
col2.metric("Movies", len(filtered_df[filtered_df['type'] == 'Movie']))
col3.metric("TV Shows", len(filtered_df[filtered_df['type'] == 'TV Show']))

# ---- Visualization 1: Titles per Year ----
st.subheader("📅 Titles Added Per Year")

yearly = filtered_df['release_year'].value_counts().sort_index()

fig1, ax1 = plt.subplots(figsize=(10,4))
ax1.plot(yearly.index, yearly.values)
ax1.set_xlabel("Year")
ax1.set_ylabel("Count")
st.pyplot(fig1)

# ---- Visualization 2: Top Genres ----
st.subheader("🎭 Most Common Genres (Top 10)")

df['listed_in'] = df['listed_in'].astype(str)
all_genres = ",".join(df['listed_in']).split(",")
genre_counts = pd.Series(all_genres).value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.bar(genre_counts.index, genre_counts.values)
plt.xticks(rotation=45)
st.pyplot(fig2)

# ---- Table ----
st.subheader("📋 Filtered Dataset")
st.dataframe(filtered_df)

# ---- Visualization: Movies vs TV Shows ----
st.subheader("🎬 Distribution of Movies vs TV Shows")

type_counts = df['type'].value_counts()

fig3, ax3 = plt.subplots(figsize=(6,4))
ax3.bar(type_counts.index, type_counts.values)
ax3.set_xlabel("Type")
ax3.set_ylabel("Count")

st.pyplot(fig3)
