# Project 2: News Article Clustering System

**Name:** <your name>  |  **Roll No:** <your roll number>
MCA 3rd Semester (2026-2027), COER University, Roorkee | Lab Sheet-07

## What it does

It groups similar news articles together automatically, without using their
categories. Articles are turned into numbers with TF-IDF and then clustered with
K-Means and Hierarchical Clustering. The top words of each cluster show its topic.

## Files

| File | What it does |
|---|---|
| `text_utils.py` | The small text cleaning function. |
| `notebooks/news_clustering.ipynb` | The same project as a notebook. |
| `datasets/news_articles.csv` | The dataset (420 articles, 6 topics). |
| `models/` | The saved model (made when you run the project). |
| `outputs/` | The graphs and `news_clustered.csv` (made when you run the project). |

## Steps in the project

1. Load the articles and explore them (length, categories).
2. Clean the text: lowercase, remove punctuation, digits, stop words and short words.
3. TF-IDF: convert every article into a vector (rows are length 1, which is the scaling step).
4. Reduce the dimensions with TruncatedSVD (LSA) to 50 columns.
5. Find the best number of clusters: elbow method, silhouette, Davies-Bouldin, Calinski-Harabasz.
6. K-Means, plus the top words of every cluster.
7. Hierarchical clustering (Ward, and cosine-average) with a dendrogram.
8. Draw the clusters in 2D with t-SNE.
9. Compare the techniques with internal scores and with the real categories (ARI, NMI, V-measure, purity).
10. Save the model and assign new articles to clusters.


