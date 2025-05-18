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
