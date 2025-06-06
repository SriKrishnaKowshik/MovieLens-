import streamlit as st
import pickle
import pandas as pd
import numpy as np
import json
from streamlit_lottie import st_lottie
import requests

def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Lottie animation file not found. Using an online fallback.")
        return None

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

file = load_lottiefile("81986-movie.json")
if not file:
    file = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_06a6pf9i.json")

st_lottie(file, speed=1, reverse=False, quality="high", loop=True, height=400)

st.title("🎬 Movie Recommendation System")


try:
    movie_df = pd.read_pickle("movie_recm.pkl")  # Using pd.read_pickle for compatibility
    similarity = pickle.load(open("similarity.pkl", "rb"))
except FileNotFoundError:
    st.error("Pickle file(s) not found. Please check the file paths.")
    st.stop()
except Exception as e:
    st.error(f"Error loading pickle files: {e}")
    st.stop()


if "title" not in movie_df.columns:
    st.error("Column 'title' not found in movie dataset. Please check the data format.")
    st.stop()
if "urls" not in movie_df.columns:
    movie_df["urls"] = "URL Not Available"  # Adding fallback if 'urls' column is missing


list_movie = np.array(movie_df["title"])

option = st.selectbox("🎥 Select a Movie:", list_movie)

def show_url(movie):
    x = []
    index = movie_df[movie_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    for i in distances[1:6]:  # Get top 5 recommendations
        x.append(movie_df.iloc[i[0]].urls)
    
    return x

def movie_recommend(movie):
    index = movie_df[movie_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in distances[1:6]:  # Get top 5 recommendations
        recommended_movies.append(movie_df.iloc[i[0]].title)

    return recommended_movies

if st.button('🎬 Recommend Me'):
    st.subheader('✨ Movies Recommended for You:')
    
    recommendations = movie_recommend(option)
    urls = show_url(option)

    df = pd.DataFrame({
        'Movie Recommended': recommendations,
        'Movie URL': urls
    })

    st.table(df)  # Display as a table
