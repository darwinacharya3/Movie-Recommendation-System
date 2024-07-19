import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pk1", 'rb'))
similarity = pickle.load(open("similarity.pk1", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")
select_value = st.selectbox("Select movies", movies_list)


def recommend_movies(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])

    recommend = []
    for i in distance[1:6]:
        recommend.append((movies.iloc[i[0]].title))
    return recommend


if st.button("Show Recommend"):
    movie_name = recommend_movies(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])
