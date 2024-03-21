

check_tup = (5, 20, 3, 7, 6, 8)


print("The original tuple is : " + str(check_tup))


K = 2

res = []
check_tup = list(sorted(check_tup))

for idx, val in enumerate(check_tup):
	if idx < K or idx >= len(check_tup) - K:
		res.append(val)
res = tuple(res)


print("The extracted values : " + str(res)) 



#Using list slicing + sorted() 


check2_tup = (5, 20, 3, 7, 6, 8)


print("The original tuple is : " + str(check2_tup))


K = 2


check2_tup = list(check2_tup)
temp = sorted(check_tup)
res = tuple(temp[:K] + temp[-K:])

print("The extracted values : " + str(res)) 


#Using heapq module:

import heapq
check3_tup = (5, 20, 3, 7, 6, 8)

print("The original tuple is : " + str(check3_tup))
K = 2
smallest = heapq.nsmallest(K, check3_tup)
largest = heapq.nlargest(K, check3_tup)
result = tuple(sorted(smallest + largest))
print("The extracted values : " +str(result))

