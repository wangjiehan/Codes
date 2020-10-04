import numpy as np
import random
from matplotlib import pyplot as plt


class K_means(object):
	'''
	K-means 步骤：
	（1）首先确定K值（即你想把数据聚为几类，K值是K-Means算法中唯一的参数）；
	（2）从原始数据集中随机选择K个点作为初始均值点；
	（3）依次从原始数据集中取出数据，每取出一个数据就和K个均值点分别计算距离（默认计算点间的欧氏距离），和谁更近就归为这个均值点所在的簇；
	（4）当步骤3结束后，分别计算各簇当前的均值点（即求该簇中所有点的平均值）；
	（5）比较当前的均值点和上一步得到的均值点是否相同，如果相同，则K-Means算法结束，否则，将当前的均值点替换掉之前的均值点，然后重复步骤3。
	'''
	def __init__(self, X, k, maxIter):
		self.X = np.array(X)					# 数据集矩阵
		self.k = k								# 所需要分的类的数
		self.maxIter = maxIter					# 所允许的程序执行的最大的循环次数

	def K_means(self):
		# 得到矩阵的行和列
		row, col = self.X.shape
		# 新生成一个矩阵，行数不变，列数加1 新的列用来存放分组号别  矩阵中的初始值为0
		dataset = np.zeros((row, col + 1))
		dataset[:, :-1] = self.X
		# print("begin:dataset:\n" + repr(dataset))
		# centerpoints = dataset[0:k,:]		# 取数据集中的前k个点为中心点
		centerpoints = dataset[np.random.randint(row, size=k)]		# 采用随机函数任意取k个点

		centerpoints[:, -1] = range(1, self.k+1)		# 每行最后一列打上类别 label
		oldCenterpoints = None 							# 用来在循环中存放上一次循环的中心点
		iterations = 1 									# 当前循环次数
		while not self.stop(oldCenterpoints, centerpoints, iterations):
			print("corrent iteration:" + str(iterations))
			print("centerpoint:\n" + repr(centerpoints))
			print("dataset:\n" + repr(dataset))

			oldCenterpoints = np.copy(centerpoints)			# 将本次循环的点拷贝一份 记录下来
			iterations += 1
			self.updateLabel(dataset, centerpoints)			# 将本次聚类好的结果存放到矩阵中
			centerpoints = self.getCenterpoint(dataset)		# 得到新的中心点，再次进行循环计算

		np.save("kmeans.npy", dataset)
		return dataset

	def stop(self, oldCenterpoints, centerpoints, iterations):
		if iterations > self.maxIter:
			return True
		return np.array_equal(oldCenterpoints, centerpoints)		# 返回两个点多对比结果

	def updateLabel(self, dataset, centerpoints):
		'''
			因为 python 的数组是地址引用，此处直接更新了外部的 dataset 数组
		'''
		row, col = self.X.shape
		for i in range(0, row):
			dataset[i, -1] = self.getLabel(dataset[i, :-1], centerpoints)
			# [i,j] 表示 i 行 j 列

	# 返回当前行和中心点之间的距离最短的中心点的类别，即当前点和那个中心点最近就被划分到哪一部分
	def getLabel(self, datasetRow, centerpoints):
		label = centerpoints[0, -1]										# 先取第一行的标签值赋值给该变量
		minDist = np.linalg.norm(datasetRow - centerpoints[0, :-1])		# 计算两点之间的直线距离
		for i in range(1, centerpoints.shape[0]):
			dist = np.linalg.norm(datasetRow-centerpoints[i, :-1])
			# 当该变距离中心点的距离小于预设的最小值，那么将最小值进行更新
			if dist < minDist:
				minDist = dist
				label = centerpoints[i, -1]
		# print("minDist:" + str(minDist) + ",belong to label:" + str(label))
		return label

	def getCenterpoint(self, dataset):
		newCenterpoint = np.zeros((self.k,dataset.shape[1]))#生成一个新矩阵，行是k值，列是数据集的列的值
		for i in range(1, self.k+1):
			oneCluster = dataset[dataset[:, -1] == i, :-1]#取出上一次分好的类别的所有属于同一类的点，对其求平均值
			newCenterpoint[i-1, :-1] = np.mean(oneCluster, axis=0)#axis=1表示对行求平均值，=0表示对列求平均值
			newCenterpoint[i-1, -1] = i#重新对新的中心点进行分类，初始类

		return newCenterpoint

	#将散点图画出来
	def drawScatter(self):
		plt.xlabel("X")
		plt.ylabel("Y")
		dataset = self.K_means()
		x = dataset[:, 0]  # 第一列的数值为横坐标
		y = dataset[:, 1]  # 第二列的数值为纵坐标
		c = dataset[:, -1]  # 最后一列的数值用来区分颜色
		color = ["none", "b", "r", "g", "y", "m", "c", "k"]
		c_color = []

		for i in c:
			c_color.append(color[int(i % len(color))])#给每一种类别的点都涂上不同颜色，便于观察

		plt.scatter(x=x, y=y, c=c_color, marker="o")#其中x表示横坐标的值，y表示纵坐标的
		# 值，c表示该点显示出来的颜色，marker表示该点多形状，‘o’表示圆形
		plt.show()


if __name__ == '__main__':

	# X = np.load("testSet-kmeans.npy")
	# 自动生成数据
	X = np.zeros((1, 2))
	for i in range(1000):
		X = np.row_stack((X, np.array([random.randint(1, 100), random.randint(1, 100)])))
	X = X[1:]
	# print(X)

	# 待分组的组数
	k = 6
	kmeans = K_means(
		X=X,
		k=k,
		maxIter=100
	)
	kmeans.drawScatter()