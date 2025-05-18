
# 🎬 Movie Recommender System

A collaborative filtering-based movie recommender system built with Python and pandas.

## 📁 Project Structure

```
├── src/
│   ├── data_loader.py        # Functions to load and preprocess movie rating data
│   ├── recommender.py        # Core recommendation engine
│   └── utils.py              # Utility functions
├── notebooks/                # Jupyter notebooks for EDA and model experiments
├── inputs/                   # Input CSV files (personal & friends' ratings)
├── outputs/                  # Output recommendations for users and friends
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview and instructions
```

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the recommender system (example)
python src/recommender.py
```

## 🧠 Code Example

```python
# From src/recommender.py
def get_top_n_recommendations(user_id, ratings, n=10):
    # Returns top N recommended movies for the given user based on collaborative filtering.
    # Your recommendation logic here
    pass
```

## 📄 Key Files

- [src/recommender.py](src/recommender.py) – Main recommendation engine.
- [src/data_loader.py](src/data_loader.py) – Data loading and preprocessing.
- [notebooks/Recommender_System.ipynb](notebooks/Recommender_System.ipynb) – Interactive development and testing.
- [inputs/personal_ratings.csv](inputs/personal_ratings.csv) – Your personal movie ratings.

---

# Movie Recommender System

This project builds a movie recommendation system using the open-source MovieLens dataset provided by [GroupLens](https://grouplens.org/datasets/movielens/).

## Features
- Exploratory Data Analysis (EDA)
- Content-based and collaborative filtering recommender
- Personal and friends' movie preferences integration

## Folder Structure
- `data/`: Original MovieLens data
- `notebooks/`: Jupyter Notebooks for EDA and modeling
- `src/`: Python modules for data loading and recommendation logic
- `inputs/`: CSVs with personal and friends' ratings
- `outputs/`: CSVs with recommended movies

## How to Use
1. Place the MovieLens dataset in `data/movielens-latest-small/`.
2. Run the notebooks in order.
3. Customize your `personal_ratings.csv` for personalized recommendations.

## Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
```
