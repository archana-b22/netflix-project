📊 Netflix Data Analysis & Dashboard Project

An end-to-end data cleaning, exploration, visualization & dashboard creation project based on the Netflix Titles Dataset.


---

📁 Project Overview

This project focuses on analyzing Netflix’s catalog to understand trends in movies and TV shows.
It includes:

✔ Data Cleaning

✔ Exploratory Data Analysis (EDA)

✔ Visualizations (Bar charts, Line charts, WordCloud, Metrics)

✔ Interactive Streamlit Dashboard

✔ PDF Report Generation

✔ GitHub Deployment



---

🗂 Dataset Information

Source: Netflix Titles Dataset

Rows: 8,790

Columns: 12


Dataset contains details like:
Titles, Directors, Cast, Country, Date Added, Release Year, Rating, Duration, and Genre.


---

🧹 Data Cleaning Steps

Removed duplicates

Handled missing values

Converted date formats

Split multiple genres & countries

Cleaned categorical columns

Exported cleaned dataset → netflix_cleaned.csv



---

🔍 Exploratory Data Analysis

Performed EDA to understand:

Movie vs TV Show distribution

Top 10 genres

Content added by year

Country-wise production

Most frequent words in description (WordCloud)



---

📈 Visualizations Included

🎬 Movies vs TV Shows

📅 Titles Added Per Year

🔟 Top 10 Genres

☁ Genre WordCloud

📊 Dashboard Metrics (Total Titles, Movies, TV Shows)


Images are available in reports/images/.


---

🎛 Interactive Streamlit Dashboard

Built using Streamlit for real-time filtering and exploration.

Dashboard Features:

Filter by:
✔ Type (Movie / TV Show)
✔ Country
✔ Release Year
✔ Genre

Metrics:

Total Titles

Total Movies

Total TV Shows


Charts:

Bar Charts

Line Charts

Genre Frequency


Dynamic Table View:
Displays filtered dataset.


Run locally:

streamlit run dashboards/app.py


---

📄 Generated Report

A complete PDF Report (Netflix_Reports.pdf) is included with:

Visual insights

Dashboard screenshots

Conclusion



---

🛠 Tech Stack Used

Python

Pandas, NumPy

Matplotlib, Seaborn

WordCloud

Streamlit

Jupyter Notebook

VS Code

Git & GitHub



---

🧾 Project Structure

netflix-project/
│
├── dashboards/
│   └── app.py
│
├── data/
│   ├── raw/netflix1.csv
│   └── clean/netflix_cleaned.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── reports/
│   ├── Netflix_Reports.md
│   ├── Netflix_Reports.pdf
│   └── images/
│       ├── movies_vs_tvshows.png
│       ├── titles_added_per_year.png
│       ├── top10_genres.png
│       ├── wordcloud.png
│       ├── filters.jpeg
│       ├── metrics.png
│       └── filtered_dataset_table.png
│
└── requirements.txt


---

📝 Conclusion

This project provides a full analysis of Netflix’s catalog and an interactive dashboard to explore patterns.
It helps understand:

Growth trend after 2015

Movie dominance

Popular genres

Country trends
