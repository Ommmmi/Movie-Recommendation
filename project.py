import pandas as pd
import numpy as np
from urllib.parse import urlparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

df=pd.read_csv("movies.csv")
print(df.head())
print(df.shape)
print(df.describe())
print(df.columns.tolist())
print(df.isnull().sum())

df["homepage"].fillna("No Homepage", inplace=True)

def extract_domain(url):
    if url=="No Homepage":
        return None
    else:
        return urlparse(url).netloc
    
df['homepage_domain']=df['homepage'].apply(extract_domain)
#import seaborn as sns
#import matplotlib.pyplot as plt

#correlation_matrix = df.corr()
#plt.figure(figsize=(10, 8))
#sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
#plt.show()


selected_features=["genres","keywords", "director","tagline",'cast']
print(df[selected_features].head())
print(df.info())
print(df[selected_features].isna().sum())


for  feature in selected_features:
    df[feature]=df[feature].fillna("")
print(df.head())


combined_features=df["genres"]+" "+df["keywords"]+" "+df['tagline']+' '+df["cast"]+' '+df["director"]
print(combined_features)



# transforming text data into numerical vectors

vectorizer=TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(combined_features)
print(feature_vectors.shape)
print(feature_vectors)


similarity = cosine_similarity(feature_vectors)
print  (similarity )
print(similarity.shape)
list_of_all_titles =df['title'].tolist()
print(list_of_all_titles)
len(list_of_all_titles)




movie_name=input("Enter your favourite movie name  : ")
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)
close_match = find_close_match[0]
print(close_match)

index_of_the_movie = df[df.title == close_match]['index'].values[0]
print(index_of_the_movie)

similarity_score=list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
print(sorted_similar_movies)


print("Movies sugessed for you : \n")

i=1
for movie in sorted_similar_movies:
    index=movie[0]
    title_from_index=df[df.index==index]['title'].values[0]
    if i<=30:
        print(i,".",title_from_index)
        i+=1