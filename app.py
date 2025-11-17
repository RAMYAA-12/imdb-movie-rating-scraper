import streamlit as st
import pandas as pd

df = pd.read_csv("imdb_top_250.csv")

st.set_page_config(page_title="IMDB Top 250", layout="wide")

st.title("🎬 IMDB Top 250 Movies")

st.write("A simple view of the Top 250 Movies from IMDB.")
st.dataframe(df, use_container_width=True)
