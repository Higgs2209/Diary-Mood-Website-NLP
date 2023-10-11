import glob
import streamlit as st
import plotly.express as px
from pathlib import Path
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


# use sort fucntion
# use glob to load files
values = {}
# Download nltk lexicon
nltk.download('vader_lexicon')

# Store Filenames
filepaths = glob.glob("files/*.txt")

# Create Date List
dates = []
positivity_values = []
negativity_values = []

stopwords = ['pos:']

for filepath in filepaths:
    with (open(filepath, "r", encoding="utf-8") as file):
        diary = file.read()
        analyser = SentimentIntensityAnalyzer()
        scores = analyser.polarity_scores(diary)


        positivity_values.append(scores["pos"])
        negativity_values.append(scores["neg"])


print(positivity_values)
print(negativity_values)


# Extract Dates
for filepath in filepaths:
    filename = Path(filepath).stem
    dates.append(filename)


st.title("Diary Mood Analysis")
st.text("Positivity")
figure_positivity = px.line(x=dates, y=positivity_values, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure_positivity)
st.text("Negativity")
figure_negativity = px.line(x=dates, y=negativity_values, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure_negativity)


