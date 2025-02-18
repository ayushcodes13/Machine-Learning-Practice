import numpy as np

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