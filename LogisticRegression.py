import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))
    
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

        dw = (1/n_samples) * np.dot(X.T, (y_predicted-y))
        db = (1/n_samples) * np.sum(y_predicted-y)

        self.weights = self.weights - self.lr * dw
        self.bias = self.bias - self.lr * db

def predict():
    linear_pred = np.dot(X, self.weights) + self.bias
    y_predicted = sigmoid(linear_pred)
    class_pred = [0 if y<0.5 else 1 for y in y_predicted]
    return class_pred