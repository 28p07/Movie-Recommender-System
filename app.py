import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=005ca2622782232ac9593d6dcb78ba7b&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original'+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances),reverse=True,key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        id = movies.loc[i[0]].id
        recommended_movies.append(movies['title'][i[0]])
        recommended_movies_poster.append(fetch_poster(id)) 
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movies Recommender System')

option = st.selectbox('Select movie from the list',movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(option)
    col0,col1,col2,col3,col4 = st.columns(5)
    with col0:
        st.text(names[0])
        st.image(posters[0])
    with col1:
        st.text(names[1])
        st.image(posters[1])
    with col2:
        st.text(names[2])
        st.image(posters[2])
    with col3:
        st.text(names[3])
        st.image(posters[3])
    with col4:
        st.text(names[4])
        st.image(posters[4])