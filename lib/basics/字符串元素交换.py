txt = 'abcdefg'
def swapstr(t,i,j):
	t = t[:i]+t[j]+t[i+1:j]+t[i]+t[j+1:]
	return t
print(swapstr(txt,1,3))
