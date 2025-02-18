import numpy as np


def sigmoid(x):
    
    
    
    
def __init__(self, n_iters = 1000, lr = 0.001):
    self.n_iters = n_iters
    self.lr = lr
    self.bias = bias
    self.weights = weights
    
def fit(self,X,y):
    n_samples, n_features = X.shape
    self.weights = np.zeros(n_features)
    self.bias = 0
    
    for _ im range(self.n_iters)
    
    linear_pred = np.dot(X, self.weights) + self.bias
    y_predicted = sigmoid(linear_pred)
    
    dw = 
    db = 
    
    
    self.weights = self.weights - self.lr * dw
    self.bias = self.bias - self.lr * db

def predict():