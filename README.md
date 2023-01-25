# HW3 - Exceptions and Testing

`Step 0.` Create a directory in the base directory of the homework repository: `knn`.  Inside of that directory create a subdirectory `test`.  Be sure to add `__init__.py` files in each of these directories.

### Create a module in the `knn` folder named `knn.py`.

`Step 1.` Inside `knn.py`, write a function, `knn_regression(n_neighbors, data, query)` that implements the k-Nearest Neighbors algorithm for regression. (2 pts for algorithm, 1 pt for exceptions)

The functions takes 3 parameters:
1. Parameter `k`, or `n_neighbors`
2. `data` - 2 dimensional numpy array of shape (m, **n+1**)). `m` denotes the number of samples and `n` is the number of variables in each sample. `+1` is for the labels in each sample. 
3. `query` - 1 dimensional numpy array, shape (n,)

The algorithm returns the predicted value for query, a single numeric value, or raises an appropriate exception (such as `ValueError`) when inappropriate inputs are passed.

We are not grading your homework based on computational complexity or on dimensionality larger than 4, so don't worry about inefficient algorithms.

Note that the creation of data to test your function is up to you. Other than the example below, we do not provide a dataset.

### Example inputs and outputs

```
import numpy as np

n_neighbors = 3
data = np.array([[3, 1, 230],
                 [6, 2, 745],
                 [6, 6, 1080],
                 [4, 3, 495],
                 [2, 5, 260]])

query = np.array([5, 4])

knn_regression(n_neighbors, data, query)  # returns 773.33
```

This is a visualization of the example inputs.

![Example diagram](knn-hw3-diagram.png)

### Pseudocode for kNN Regression

```
A. Load the data

B. Initialize K to your chosen number of neighbors

C. For each example in the data:

    C.1 Calculate the distance between the query example and the current example from the data
    
    C.2 Add the distance and the index of the example to an ordered collection

D. Sort the ordered collection of distances and indices from smallest to largest (in ascending order) by the distances

E. Pick the first K entries from the sorted collection

F. Get the labels of the selected K entries

G. Return the mean of the K labels
```

### Create a Python module `test_knn.py` inside the `tests` folder.

`Step 2.` Inside `test_knn.py`, write a series of test cases to confirm the validity of your implementation in `Step 1.` 

These tests should contain:

a. At least one *smoke* test (1pt).

b. At least two *one-shot* tests (1pt).

c. All appropriate *edge* tests you find useful for the algorithm (at least two) (2 pts).

d. Make sure you can execute all of these tests by running `python -m unittest discover -s knn` in the root of your homework repository.
