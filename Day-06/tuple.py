#Find the size of a Tuple in Python

import sys

# sample Tuples
Tup1 = ("A", 1, "B", 2, "C", 3)
Tup2 = ("Sakib", "Raju", "Abir", "Nikhil", "Zabir", "Deepanshu")
Tup3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))


print("Size of Tuple1: " + str(sys.getsizeof(Tup1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tup2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tup3)) + "bytes")

