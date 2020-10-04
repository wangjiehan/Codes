def isSum(arr,i,sum,aim):
	if i == len(arr):			#可变参数：n为当前位置，sum为当前累加和			
		return sum == aim
	else:									
		return isSum(arr,i+1,sum,aim) or isSum(arr,i+1,sum + arr[i],aim)
print(isSum([3,2,5],0,0,7))
print(isSum([6,5,7,8],0,0,9))
