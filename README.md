Movie Recommender System

 Overview
This is a Movies Recommendation System built using Python and Streamlit. It suggests movies similar to the one selected by the user, using a similarity matrix generated from movie data.

 Features
- Select a movie from the dropdown list.
- Get five recommended movies based on similarity.
- View movie posters for better user experience.

 Technologies Used
- Python
- Streamlit (for the web app UI)
- Pandas (for data handling)
- Requests (for fetching movie posters via API)
- Pickle (for loading precomputed data)


 Data Files
- `moviesList.pkl`: Contains movie titles and their respective IDs.
- `similarity.pkl`: Stores the precomputed similarity matrix.

 How It Works
1. The user selects a movie from the dropdown.
2. The system finds similar movies using a precomputed similarity matrix.
3. It fetches movie posters using The Movie Database (TMDb) API.
4. Recommendations are displayed with titles and images.

 API Key Configuration
This project uses **TMDb API** for fetching movie posters. To use it:
- Replace the existing API key in `get_poster(film_id)` with your own from [TMDb](https://www.themoviedb.org/).



