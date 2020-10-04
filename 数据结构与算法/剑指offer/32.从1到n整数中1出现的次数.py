'''
32.从1到n整数中1出现的次数
方法（2）分段，把当前考虑位的高阶位变化和低阶位变化分开计数
难！理解 + 记忆
'''
#（1）常规方法：转化成字符串。时间复杂度O(logN**2)
def get_1_nums1(n):
	count = 0
	for i in range(1, n+1):
		for j in str(i):
			if j == '1':
				count += 1
	return count
#（2）从个位开始判断1有几个，O(logN)
def get_1_nums2(n):
	count = 0
	tmp = n
	base = 1
	while tmp:
		last = tmp % 10
		tmp = int(tmp / 10)
										#考虑当前位的高阶位变化，比如32x看个位x时，计入32个（不管x是不是1）；
		count += tmp * base				#32xa看十位x时，有32*10种变化（a有十种）
										#两个条件考虑当前位的低阶位变化	
		if last == 1:					#区分当前位是不是1，计入base+1（余数个数加上00..位）的个数。
			count += n % base + 1			#比如132要把100到132这33个数都算进去
		elif last > 1:					#当前位大于1时，把为1时的那base个个数计入（余数为上限）
			count += base					#比如当前位为2xx时，要把100到199这100个数计入（满算）
		base *= 10
	return count
if __name__ == '__main__':
	print(get_1_nums1(121))
	print(get_1_nums2(121))
	
	

