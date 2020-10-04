'''
2.Python实现单例模式
'''
class SingleTon():
	def __init__(self, val):
		self.val = val
	def printVal(self):
		print(self.val.title())
if __name__ == '__main__':		
	obj1 = SingleTon('tom')
	obj1.printVal()
	
