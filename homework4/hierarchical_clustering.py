# Starting homework3
import pandas as pd

delimiter = "\s+"
directory = "/Users/CheickSissoko/Documents/CS6140/homework4/"
C1 = pd.read_csv(directory + "C1.txt", delimiter=delimiter, header=None)
C2 = pd.read_csv(directory + "C2.txt", delimiter=delimiter, header=None)
C3 = pd.read_csv(directory + "C3.txt", delimiter=delimiter, header=None)

print(C1.shape)
print(C2.shape)
print(C3.shape)

# We will always measure distance with Euclidean distance.
