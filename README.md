# Movie-Recommendation
 This project is a content-based Movie Recommendation System that suggests movies similar to a user’s favorite movie. It uses TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization to transform text-based features into numerical representations and Cosine Similarity to calculate movie relevance. The system analyzes genres, keywords, tagline, cast, and director to find and rank similar movies. 
Features

Content-based filtering using natural language processing (NLP) techniques.

Fuzzy matching to find the closest movie titles.

Top 30 movie recommendations based on similarity scores.

Handles missing values and optimizes data processing.

Efficient for large datasets with scalable text-based similarity computation.

Installation

Prerequisites

Ensure you have Python 3.x installed along with the required dependencies.

Clone the Repository

git clone https://github.com/yourusername/Movie-Recommendation-System.git
cd Movie-Recommendation-System

Install Dependencies

pip install pandas numpy scikit-learn

Usage

Run the script and enter your favorite movie name.

The system will find the closest matching movie from the dataset.

It will compute similarity scores and display the top 30 recommended movies.
Technologies Used

Python

Pandas, NumPy (Data Handling)

Scikit-learn (TF-IDF, Cosine Similarity)

difflib (Fuzzy Matching)

Example Output

Enter your favorite movie name: Inception
Movies suggested for you:
1. Interstellar
2. The Matrix
3. The Dark Knight
...
30. Minority Report

Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.
