# Project 1: Customer Segmentation using K-Means Clustering

**Name:** Rajendra Singh Bisht
MCA 3rd Semester (2026-2027), COER University, Roorkee | Lab Sheet-07

## What it does

It groups shop customers into segments (groups of similar customers) using age,
annual income, spending score, purchase frequency, average order value and days since
the last purchase. Each segment gets a name and a suggested marketing action.
This is unsupervised learning: the data has no "correct answer" column.

## Files

| File | What it does |
|---|---|
| `customer_segmentation.py` | The full project (one cell per step). |
| `notebooks/customer_segmentation.ipynb` | The same project as a notebook. |
| `predict.py` | Type a customer's details and get the segment (for the demo). |
| `datasets/customer_data.csv` | The dataset (about 400 customers). |
| `scripts/generate_dataset.py` | Creates the dataset again if it is deleted. |
| `models/` | The saved model (made when you run the project). |
| `outputs/` | The graphs and `customers_segmented.csv` (made when you run the project). |

## Steps in the project

1. Load the data and explore it.
2. Clean: remove duplicates, fill missing values (median), cap outliers (IQR rule).
3. Scale the features with StandardScaler.
4. Find the best number of clusters: elbow method, silhouette, Davies-Bouldin, Calinski-Harabasz.
5. Build the K-Means model and draw the clusters (income vs spending, and a PCA picture).
6. Describe each segment (averages, size, name, marketing action).
7. Compare K-Means with Hierarchical clustering (and a dendrogram) and a Gaussian Mixture.
8. Check the result: with and without scaling, and stability over random starts.
9. Save the model and the segmented customers, and place new customers into segments.

