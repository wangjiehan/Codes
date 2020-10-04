from sklearn.datasets.samples_generator import make_circles
import matplotlib.pyplot as plt
import time
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import numpy as np
import random

'''
ε-邻域：对于任意xi，其ε-邻域包含D中所有与xi距离不大于ε的样本点。
核心对象：若xi的ε-邻域至少包含MinPts个样本，则称其为核心对象。
密度直达：xj位于xi的ε-邻域，则称xj可由xi密度直达。
密度可达：A由B密度直达，B由C密度直达，则称A由C密度可达。
密度相连：A、B皆有C密度可达，则称AB密度相连。

用更通俗易懂的话描述就是如果一个点的 eps 邻域内的点的总数小于阈值，那么该点就是低密度点。
如果大于阈值，就是低密度点。如果一个高密度点在另外一个高密度点的邻域内，就直接把这两个高密度点相连，这是核心点。
如果一个低密度点在高密度点的邻域内，就将低密度点连在距离它最近的高密度点上，这是边界点。
不在任何高密度点的 eps 邻域内的低密度点，就是异常点。

算法流程为：
从所有样本点中，根据ε和MinPts找出所有核心对象作为种子集合。
以任意核心为起点，找到所有密度可达对象生成簇。
在剩余数据、剩余种子集合中再次随机选择下一个核心，重复操作。
直到所有的样本全部被访问。

DBSCAN 优点：
1、对噪声不敏感。这是因为该算法能够较好地判断离群点，并且即使错判离群点，对最终的聚类结果也没什么影响
2、能发现任意形状的簇。这是因为DBSCAN 是靠不断连接邻域呢高密度点来发现簇的，只需要定义邻域大小和密度阈值，因此可以发现不同形状，不同大小的簇

DBSCAN 缺点：
1、对两个参数的设置敏感，即圈的半径 eps 、阈值 MinPts。
2、DBSCAN 使用固定的参数识别聚类。显然，当聚类的稀疏程度不同，聚类效果也有很大不同。即数据密度不均匀时，很难使用该算法
3、如果数据样本集越大，收敛时间越长。此时可以使用 KD 树优化
'''

#计算两个向量之间的欧式距离
def calDist(X1, X2):
    sum = 0
    for x1 , x2 in zip(X1 , X2):
        sum += (x1 - x2) ** 2
    return sum ** 0.5

#获取一个点的ε-邻域（记录的是索引）
def getNeibor(data, dataSet, e):
    res = []
    for i in range(shape(dataSet)[0]):
        if calDist(data, dataSet[i]) < e:
            res.append(i)
    return res

# 密度聚类算法
def _DBSCAN(dataSet, e, minPts):
    coreObjs = {}#初始化核心对象集合
    C = {}
    n = shape(dataSet)[0]
    #找出所有核心对象，key是核心对象的index，value是ε-邻域中对象的index
    for i in range(n):
        neibor = getNeibor(dataSet[i] , dataSet , e)
        if len(neibor)>=minPts:
            coreObjs[i] = neibor
    oldCoreObjs = coreObjs.copy()
    k = 0#初始化聚类簇数
    notAccess = list(range(n))#初始化未访问样本集合（索引）
    while len(coreObjs)>0:
        OldNotAccess = []
        OldNotAccess.extend(notAccess)
        cores = coreObjs.keys()
        #随机选取一个核心对象
        randNum = random.randint(0,len(cores))
        cores=list(cores)
        core = cores[randNum]
        queue = []
        queue.append(core)
        notAccess.remove(core)
        while len(queue)>0:
            q = queue[0]
            del queue[0]
            if q in oldCoreObjs.keys() :
                delte = [val for val in oldCoreObjs[q] if val in notAccess]#Δ = N(q)∩Γ
                queue.extend(delte)#将Δ中的样本加入队列Q
                notAccess = [val for val in notAccess if val not in delte]#Γ = Γ\Δ
        k += 1
        C[k] = [val for val in OldNotAccess if val not in notAccess]
        for x in C[k]:
            if x in coreObjs.keys():
                del coreObjs[x]
    return C


if __name__ == '__main__':
    X, y_true = make_circles(n_samples=1000, noise=0.15)  # 随机生成1000个圆环形状数据
    print(X)
    print(y_true)

    plt.scatter(X[:, 0], X[:, 1], c=y_true)
    plt.show()

    # DBSCAN 算法
    t0 = time.time()
    y_pred = DBSCAN(eps=.1, min_samples=6).fit_predict(X)  # 该算法对应的两个参数
    t = time.time() - t0
    plt.scatter(X[:, 0], X[:, 1], c=y_pred)
    plt.title('time : %f' % t)
    plt.show()

    # eps为距离阈值ϵ，min_samples 为邻域样本数阈值MinPts, X为数据
    y_pred = DBSCAN(eps=0.1, min_samples=10).fit_predict(X)
    print(len(y_pred))

    X = np.zeros((1, 2))
    for i in range(1000):
        X = np.row_stack((X, np.array([random.randint(1, 100), random.randint(1, 100)])))
    X = X[1:]
    y_pred = DBSCAN(eps=5, min_samples=10).fit_predict(X)
    print(len(y_pred))
    plt.scatter(X[:, 0], X[:, 1], c=y_pred)
    plt.show()