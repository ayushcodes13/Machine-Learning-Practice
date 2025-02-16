import numpy as np

class LinearRegression:
    
    def __init__(self, lr = 0.001, n_iters = 1000):
    
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
    
    def fit(self, X, y): #x,y refers to the dataset that we will get from the user
    #here we are initialising the weights and bias ie 0
        n_features, n_samples = X.shape #to know how many features and samples we are having in our dataset
        #since we have only one feature in our dataset then only one weight is needed if there would have been more then we would need more number of weights
        self.weights = np.zeros(n_features) #created weights for each feature having initial value as 0
        self.bias = 0
    
        for _ in range(self.n_iters): #looping through the number of iterations
        
            #we will use vectorizaton instead of calculating the y_pred for each point - it will help to predict the samples of all at the same time
            y_pred = np.dot(X, self.weights) + self.bias #main formula for that line
            
            #gradient
            dw = (1/n_samples) * np.dot(X, (y_pred-y)) #the dot thing also does the sum
            db = (1/n_samples) * np.sum(y_pred-y)
            
            #gradient descent - finds the best value for w and b values
            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db
            
    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred