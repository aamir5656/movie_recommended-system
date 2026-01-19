import pandas as pd
import  streamlit as st
import  pickle
import  requests

def fetch_poster(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{movie_id}?api_key=671100724ba958048404df85347c8b3c"
        .format(movie_id=movie_id)
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movie.append(movies.iloc[i[0]].title)
        #fatch poster from api
        recommended_movie_poster.append(fetch_poster(movie_id))

    return recommended_movie, recommended_movie_poster

movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def compute_similarity(movies):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    similarity = cosine_similarity(vectors)
    return similarity

similarity = compute_similarity(movies)


st.title('Movie Recommender System')

option = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)

if st.button("Recommend"):
    names,posters = recommend(option)

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
