def move(n,a,b,c):			#从a通过b到c
	if n==1:
		print(a+'->'+c)
	else:
		move(n-1,a,c,b) 	#n-1个从a通过c到b
		print(a+'->'+c) 	#最大的盘从a到c
		move(n-1,b,a,c) 	#之前的n-1个从b通过a到c
n=int(input('Enter n: '))
move(n,'A','B','C')
