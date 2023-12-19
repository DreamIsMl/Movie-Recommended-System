import pickle
import pandas as pd
import requests
import streamlit as st

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=816e7e360da31b8177a7972949dfb046'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def load_pickle_from_github(file_url):
    response = requests.get(file_url)
    data = pickle.loads(response.content)
    return data

# Load pickled files from GitHub
movies_dict_url = 'https://raw.githubusercontent.com/DreamIsMl/Movie-Recommended-System/main/movie_dict.pkl'
similarity_url = 'https://raw.githubusercontent.com/DreamIsMl/movie-model/main/similarity.pkl'

movies_dict = load_pickle_from_github(movies_dict_url)
movies = pd.DataFrame(movies_dict)
similarity = load_pickle_from_github(similarity_url)

st.title('Movie Recommender System By Hakim')

Selected_movie_name = st.selectbox(
    'How Would You Like To Be Contacted',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(Selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
