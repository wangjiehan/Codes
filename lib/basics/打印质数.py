def printPrimeNumber(n):
	res = []
	for i in range(2, n + 1):
		j = 2
		while j < i//j + 1:
			if i % j == 0:
				break
			j += 1
		if j > i//j :
			res.append(i)
	return res
if __name__ == '__main__':
	print(printPrimeNumber(100))
