# Importing random
import random
# Importing Time
import time
# Importing For data representation
import numpy as np
import matplotlib.pyplot as plt

IS = {}
SS = {}
MS = {}

class Operation:
    # Constructor
    def __init__(self,n):
        self.n = n

    # Random self.array generator        
    def generator(self):
        self.arr = []
        for i in range(self.n):
            element = random.randint(1,100)
            self.arr.append(element)
        
        print(self.arr)
        # Calling other functions
        self.InsertionSort()
        self.SelectionSort()
        self.MergeSortSubmission()

    # Insertion Sort
    def InsertionSort(self):
        exp = self.arr.copy()
        start = time.perf_counter_ns()
        for i in range(len(exp)):
            key = exp[i]
            j = i - 1
            while j >= 0 and key < exp[j]:
                exp[j + 1] = exp[j]
                j -= 1
            exp[j + 1] = key
        end = time.perf_counter_ns()
        timetaken = end - start
        IS[len(exp)] = timetaken
    
    # Selection Sort
    def SelectionSort(self):
        exp = self.arr.copy()
        start = time.perf_counter_ns()
        for i in range(len(exp)-1, 0, -1):
            positionMax = 0
            for j in range(1, i+1):
                if exp[j] > exp[positionMax]:
                    positionMax = j
            temp = exp[i]
            exp[i] = exp[positionMax]
            exp[positionMax] = temp
        end = time.perf_counter_ns()
        timetaken = end - start
        SS[len(exp)] = timetaken
    
    # Merge Sort
    def MergeSort(self,arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.MergeSort(L)
            self.MergeSort(R) 
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr
    
    # Merge sort time calculation
    def MergeSortSubmission(self):
        start = time.perf_counter_ns()
        self.MergeSort(self.arr)
        end = time.perf_counter_ns()
        timetaken = end - start
        MS[len(self.arr)] = timetaken

# Data Representation
def Graph(IS, SS):
    ISK,ISV = list(IS.keys()), list(IS.values())
    SSV = list(SS.values())
    MSV = list(MS.values())
    result = [ISV] + [SSV] + [MSV]
    X = np.arange(len(ISV))
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_title("Time Comparison with increasing no. of items")
    ax.set_xlabel("Number of items")
    ax.set_ylabel("Time in nano-seconds")
    ax.grid(b = True, color ='grey',linestyle ='-.', linewidth = 0.5, alpha = 0.2)
    ax.bar(X, result[0], color = 'lightblue', width = 0.25)
    ax.bar(X + 0.25, result[1], color = 'slateblue', width = 0.25)
    ax.bar(X + 0.50, result[2], color = 'lightgreen', width = 0.25)
    ax.legend(labels=["Insertion Sort","Selection Sort","Merge Sort"])
    plt.xticks([r + 0.25 for r in range(len(ISK))],ISK)
    plt.show()

a = Operation(10).generator()
b = Operation(20).generator()
c = Operation(30).generator()

# Calling Data Representation
Graph(IS,SS)