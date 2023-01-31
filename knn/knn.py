import numpy as np



# Interface
class KnnRegressionInterface:
    def knn_regression(n_neighbors: int, data: np.ndarray, query: np.ndarray):
        pass


# Implementation        
class KnnRegression(KnnRegressionInterface):
    def knn_regression(n_neighbors, data, query):
        print(type(n_neighbors),' ',type(data),' ',type(query))
        try:
            # n_neighbors check
            if type(n_neighbors) != int:
                raise ValueError("n_neighbors is not an integer.")
            if n_neighbors <= 0:
                raise ValueError("n_neighbors should be greater than 0.")

            #data check
            if type(data) != np.ndarray:
                raise ValueError("data should be a numpy array.")
            if data.ndim != 2:
                raise ValueError("data should be a 2-dimensional numpy array.")
            if data.shape[0] < n_neighbors:
                raise ValueError("number of samples in data should be at least as large as n_neighbors.")
            if data.shape[1] < 2:
                raise ValueError("n+1 should be at least 2.(n should be at least 1)")
            if not all(data.shape[1] == len(row) for row in data):
                raise ValueError("all samples in data should have the same number of variables")
            #query check
            if type(query) != np.ndarray:
                raise ValueError("query should be a numpy array.")
            if not np.issubdtype(data.dtype, np.number):
                raise ValueError("all samples and labels should be numeric.")
            if not np.issubdtype(query.dtype, np.number):
                raise ValueError("query should be numeric.")
            if query.ndim != 1:
                raise ValueError("query should be a 1-dimensional numpy array.")
            if query.shape[0] != data.shape[1] - 1:
                raise ValueError("number of variables in query should be the same as in data.")

                
            # Check if all rows have the same number of columns
            n_cols = data.shape[1]
            for i in range(data.shape[0]):
                if data[i].shape[0] != n_cols:
                    raise ValueError("Inhomogeneous shape of data array")
                    

            


                
            #TO IMPLEMENT KNN HERE
            
            
            
            return -1
        except ValueError as e:
            print("Error:", e)
            return -1
   
  
def main():
    n_neighbors = 3
    data = np.array([[5,1, 230],
                 [6, 2, 745],
                 [6, 6, 1080],
                 [4, 3, 495],
                 [2, 5, 260]])

    query = np.array([5, 4])
    try:
        resp = KnnRegression.knn_regression(n_neighbors, data, query)
    except ValueError as e:
        print(e)
        return
    print(resp)
    
if __name__ == "__main__":
    main()