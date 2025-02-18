import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

class knn:
    
    def __init__(self, k=3):
        self.k = k  # k refers to the number of points to consider nearby
        
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions  # ✅ Fixed return statement

    def _predict(self, X):
        # Step 1 - Calculate distances
        distances = [euclidean_distance(X, x_train) for x_train in self.X_train]
        
        # Step 2 - Get k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        
        # Step 3 - Get the labels of the k nearest neighbors
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # Step 4 - Get the most common label
        most_common = Counter(k_nearest_labels).most_common(1)  
        return most_common[0][0]  # ✅ Return the most frequent label
