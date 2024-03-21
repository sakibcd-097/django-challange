

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
