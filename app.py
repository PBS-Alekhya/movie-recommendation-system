import pickle
import streamlit as st
import requests
import pandas as pd

def get_poster(film_id):
    api_url = f"https://api.themoviedb.org/3/movie/{film_id}?api_key=f932f7c9f2411069e2f69b56b50fadcb&language=en-US"
    response_data = requests.get(api_url).json()
    return f"https://image.tmdb.org/t/p/w500/{response_data.get('poster_path', '')}"

def suggest_movies(film_name):
    try:
        movie_index = movie_data.index[movie_data['title'] == film_name].tolist()[0]
    except IndexError:
        return [], []
    
    similarity_scores = [(i, score) for i, score in enumerate(similarity_matrix[movie_index])]
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:6]
    
    suggested_movies = [(movie_data.iloc[i].title, get_poster(movie_data.iloc[i].movie_id)) for i, _ in similarity_scores]
    suggested_titles, suggested_posters = zip(*suggested_movies) if suggested_movies else ([], [])
    
    return suggested_titles, suggested_posters

st.header(' Movie Recommender System ')
movie_data = pd.DataFrame(pickle.load(open('movie_list.pkl', 'rb')))
similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))

user_choice = st.selectbox("Search or choose a movie from the list", movie_data['title'].values)

if st.button('Get Recommendations'):
    suggested_titles, suggested_posters = suggest_movies(user_choice)
    cols = st.columns(len(suggested_titles))
    
    for col, title, poster in zip(cols, suggested_titles, suggested_posters):
        with col:
            st.text(title)
            st.image(poster)
