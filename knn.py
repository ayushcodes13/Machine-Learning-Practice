import numpy as np
from Collections import counter

def euclidean_distance(x1, x2);
    distance = np.sqrt(np.sum(x1 - x2**2))
    return distance

class knn:
    
    def __init__ (self, k=3):
        self.k = k
        #k refers to the number of points we have to consider nearby
        
    def fit(self,X,y):
        
        self.X_train = X
        self.y_train = y
    
    def predict (self,X):
        #this function is for all the sum of the predictions
        predictions = [self._predict(x) for x in X]
        return predict        
        
    def _predict(self,X):
        #this will calculate the predictions one by one manually
        
        #step1 - calculate the distances using euclidean distance
        distances = [euclidean_distance(X, x_train) for x_train in self.X_train]
        
        #step2 - get the k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        
        #step3 - get the target values of the k nearest neighbors
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        #step4 - get the target values of the k nearest neighbors
        Counter(k_nearest_labels).most_common()
        return most_common