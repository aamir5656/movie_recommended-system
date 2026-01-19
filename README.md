# 🎬 Content-Based Movie Recommender System

This project is a **Content-Based Movie Recommendation System** built using **Python, Machine Learning, and Streamlit**.  
It recommends movies similar to a selected movie based on textual features such as genres, keywords, cast, and overview.

The application is deployed on **Streamlit Community Cloud** and can be accessed using the link below:

👉 **Live App:** https://content-based-movie-recommender123.streamlit.app/

---

## 🔍 How It Works
- Movie metadata is processed and combined into a single textual feature (`tags`).
- A **CountVectorizer** is used to convert text into numerical vectors.
- **Cosine similarity** is applied to compute similarity scores between movies.
- Based on the selected movie, the system recommends the top similar movies.

---

## 🚀 Features
- Content-based movie recommendations  
- Interactive and user-friendly UI using Streamlit  
- Fast similarity computation with caching  
- Deployed and accessible online  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Pickle  

---

## 📁 Project Structure
app.py  
movies_dict.pkl  
requirements.txt  
README.md  
Movie_Recommend_System_code.ipynb  

---

## ▶️ Run the App Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment
This application is deployed using **Streamlit Community Cloud** via GitHub.

---

## 📌 Author
**Aamir Shahzad**  
Data Science & Machine Learning Enthusiast  

---

⭐ If you find this project useful, feel free to give it a star!
