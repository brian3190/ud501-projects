import numpy as np
import time

def test_run():
    # List to 1D array
    print np.array([2, 3, 4])

    # List of tuples to 2D array
    print np.array([(2, 3, 4), (5, 6, 7)])

    # Empty array: contains random numbers depending on state of comp memory
    print np.empty(5)

    # Empty 3D array with depth=3, row=5, column=4
    print np.empty((5,4,3))

    #Array of 1s, specifying the datatype=int
    print np.ones((5, 4), dtype=np.int_)

    # Generate an array full of random numbers, uniformly sampled between 0.0 and 1.0
    print np.random.rand(5, 4) # function arguments (not a tuple), row=5, column=4

    # Sample numbers from a Gaussian (normal) distribution
    print np.random.normal(size=(2, 3)) # "standard normal" (mean=0, s.d.=1)

    # Change mean to 50 and s.d. to 10
    print np.random.normal(50, 10, size=(2, 3))

    # Random integers
    print np.random.randint(10) # single integer in
    print np.random.randint(0, 10) # same as above, specifying (low, high) explicit
    print np.random.randint(0, 10, size=5) # 5 random integers as 1D array
    print np.random.randint(0, 10, size=(2,3)) # 2x3 array of random integers

    # Shape, size of array
    a.shape
    a.shape[0] # rows
    a.shape[1] # columns
    len(a.shape) # dimension of array
    a.size # number of elements in array
    a.dtype # float64

def test_run2():
    # Operations on arrays
    np.random.seed(693) # seed random number generator
    a = np.random.randint(0, 10, size=(5, 4))
    print "Array:\n", a

    # Sum of all elements
    print "Sum of all elements:", a.sum()

    # Iterate over rows, to compute sum of each column
    print "Sum of each column:\n", a.sum(axis=0)

    # Iterate over columns to compute sum of each row
    print "Sum of each row:\n", a.sum(axis=1)

    # Statistics: min, max, mean (across rows, cols, and overall)
    print "Minimum of each column:\n", a.min(axis=0)
    print "Maximum of each row:\n", a.max(axis=1)
    print "Mean of all elements:", a.mean() #leave out axis arg

def test_run3():
    # Get Index of Max
    a = np.array([9, 6, 72, 50], dtype=np.int32)

    def get_max_index(a):
        return a.argmax()

    print "Array:", a

    # Find maximmum and its index in array
    print "Maximum value:", a.max()
    print "Index of max:", get_max_index(a)

def time_run():
    t1 = time.time()
    print "ML4T"
    t2 = time.time()
    print "Time taken", t2 - t1, "seconds"

def test_run4():
    a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    print a

    #calculating mean
    mean = a.mean()
    print mean

    #accesses all values less than mean
    a[a<mean]

    #masking
    a[a<mean] = mean #replaces all values less than mean
    print a

def test_run5():
    # Arithmetic operations
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    print "Original array a:\n", a

    #multiply a by 2
    print "\nMultiply a by 2:\n", 2 * a

    #divide by 2 gets a float
    print "\nDivide a by 2:\n", a / 2.0

    b = np.array([(100, 200, 300, 400, 500), (1, 2, 3, 4, 5)])
    print "\nOriginal array b:\n", b

    #add the two arrays
    print "\nAdd a + b:\n", a + b

    #Multiply a and b is elementwise multiplication
    print "\nMultiply a and b:\n", a * b

    

if __name__ == "__main__":
    test_run4()
