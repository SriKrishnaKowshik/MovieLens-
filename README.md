# A_Movie_Recommendation_System 🎬

This project is a content-based movie recommendation system built using Python. It suggests similar movies based on user input, leveraging metadata like genres, cast, and crew from the MovieLens dataset.

## 🚀 Features

- Recommend similar movies using content-based filtering  
- Preprocessed and vectorized movie metadata  
- Pickle-based model for fast similarity matching  
- Simple and interactive Python interface  

---

## 🗂️ Files Included

| File Name              | Description                                      |
|------------------------|-------------------------------------------------|
| `MOVIE.py`             | Main Python script to run the recommendation system |
| `movies.csv`           | Movies metadata dataset                          |
| `movie_credit.csv`     | (Large file) Contains movie credit details      |
| `movie_recm.pkl`       | Pre-trained model for recommendations            |
| `81986-movie.json`     | Additional data used in recommendations          |
| `similarity.pkl`       | (Large file) Precomputed similarity matrix       |

---

## 📦 Installation

```bash
git clone https://github.com/SriKrishnaKowshik/MovieLens-.git
cd MovieLens-
pip install -r requirements.txt


## 📥 Download Large Files

**Due to GitHub's file size restrictions, some large files are not included in this repository.**

Please download these files manually from the Google Drive folder below and place them in the project root directory:

**📁 Google Drive Folder:**  
https://drive.google.com/drive/folders/1CDfH7DFjhnXA_2rY5MbhU4IB5hrXGiAf

**Files to download:**  
- **movie_credit.csv**  
- **similarity.pkl**

**Make sure these files are in the same folder as `MOVIE.py` before running the project.**
