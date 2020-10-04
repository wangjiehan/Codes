import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
'''
PCA 过程
输入：训练样本集 D=x(1),x(2),...,x(m) ,低维空间维数 d′ ;
  过程：.
  1：对所有样本进行中心化（去均值操作）： x(i)j ← x(i)j − 1/m ∑ x(i)j ;
  2：计算样本的协方差矩阵 XXT ;
  3：对协方差矩阵 XXT 做特征值分解 ;
  4：取最大的 d′ 个特征值所对应的特征向量 w1,w2,...,wd′，组成投影矩阵 W
  5：将原样本矩阵与投影矩阵相乘： X⋅W 即为降维后数据集 X′ 。其中 X 为 m×n 维， W=[w1,w2,...,wd′] 为 n×d′ 维。
  6：输出：降维后的数据集 X′
'''
def example():
    x = np.array([2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1])
    y = np.array([2.4, 0.7, 2.9, 2.2, 3, 2.7, 1.6, 1.1, 1.6, 0.9])
    '''
    1. 对数据求平均值和中心化
    '''
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    scaled_x = x - mean_x
    scaled_y = y - mean_y
    data = np.matrix([[scaled_x[i], scaled_y[i]] for i in range(len(scaled_x))])

    '''
    2. 求协方差矩阵和散度矩阵
    '''
    # 协方差矩阵。x, y 共 2 维特征，那么协方差矩阵 M, 为一个 n x n 的矩阵，
    # 其中 Mij 为第 i 和第 j 个特征的协方差，对角线是各个特征的方差。
    # 在我们的数据中，n=2，所以协方差矩阵是 2 x 2 的，
    cov = np.cov(scaled_x, scaled_y)
    print(cov)

    # 散度矩阵
    scatter = np.dot(np.transpose(data), data)
    print(scatter)

    # 其实协方差矩阵和散度矩阵关系密切，散度矩阵 就是协方差矩阵乘以（总数据量-1）。
    # 因此他们的特征根和特征向量是一样的。
    # 散度矩阵是SVD奇异值分解的一步，因此PCA和SVD是有很大联系

    '''
    3. 求协方差矩阵的特征值和特征向量
    '''
    eig_val, eig_vec = np.linalg.eig(cov)
    print(eig_val)
    print(eig_vec)      # 特征矩阵每一列对应一个特征值对应的特征向量

    plt.plot(scaled_x, scaled_y, 'o',)

    # 增大画图上下限范围
    xmin, xmax = scaled_x.min(), scaled_x.max()
    ymin, ymax = scaled_y.min(), scaled_y.max()
    dx = (xmax - xmin) * 0.2
    dy = (ymax - ymin) * 0.2
    plt.xlim(xmin - dx, xmax + dx)
    plt.ylim(ymin - dy, ymax + dy)

    # 添加特征向量
    plt.plot([eig_vec[:, 0][0], 0], [eig_vec[:, 0][1], 0], color='red')
    plt.plot([eig_vec[:, 1][0], 0], [eig_vec[:, 1][1], 0], color='red')

    plt.show()
    '''
    X[:, 0]: 取二维数组中第一维的所有数据，所有行的第一个数，即矩阵的第一列
    X[:, 1]: 取二维数组中第二维的所有数据
    X[:, m: n]: 取二维数组中第m维到第n-1维的所有数据
    X[:,:, 0]: 取三维矩阵中第一维的所有数据
    X[:,:, 1]: 取三维矩阵中第二维的所有数据
    X[:,:, m: n]: 取三维矩阵中第 m 维到第 n-1 维的所有数据
    '''

    '''
    4. 特征向量之间是正交的。特征向量代表着数据的pattern(模式)
    将特征向量矩阵直接乘以数据，则以特征向量为基底，重新构建了空间
    '''
    new_data = np.transpose(np.dot(eig_vec, np.transpose(data)))
    print(new_data)

    new_x = new_data[:, 0][:]
    print(new_x)
    new_y = new_data[:, 1][:]
    print(new_y)
    plt.plot(new_x, new_y, 'o',)
    plt.show()

    '''
    5. 选择主要成分
    '''
    # 特征值和其对应的特征向量结对，按特征值绝对值从大到小排序
    eig_pairs = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(len(eig_val))]
    eig_pairs.sort(reverse=True)
    print(eig_pairs)

    # 选取特征值绝对值最大的对应特征向量为主成分
    feature = eig_pairs[0][1]
    print(feature)

    '''
    6. 用选取的主成分作用在原数据，得到降维后的数据
    '''
    new_data_reduced = np.transpose(np.dot(feature, np.transpose(data)))
    print(new_data_reduced)

    # 整个过程画图
    plt.plot(scaled_x, scaled_y, 'o', color='red')
    plt.plot([eig_vec[:, 0][0], 0], [eig_vec[:, 0][1], 0], color='red')
    plt.plot([eig_vec[:, 1][0], 0], [eig_vec[:, 1][1], 0], color='blue')
    plt.plot(new_data[:, 0], new_data[:, 1], '^', color='blue')
    plt.plot(new_data_reduced[:, 0], [1.2]*10, '*', color='green')
    plt.show()

def PCA(feature_list):
    feature_arr = np.array(np.transpose(np.array(feature_list)))
    # N 个特征（N列）
    N = len(feature_arr[0])
    # 每个特征 M 维（M行）
    M = len(feature_arr)

    def scaled(feature):
        mean = np.mean(feature)
        scaled_feature = feature - mean
        return scaled_feature

    data = []
    for j in range(N):
        # print(feature_arr[:, j])
        # print(scaled(feature_arr[:, j]))
        data.append(np.transpose(scaled(feature_arr[:, j])).ravel())
    data = np.transpose(data)
    # print(data)
    cov = np.cov(np.transpose(data))
    # print(cov)
    if len(cov) == N:
        print("Success in getting covariance...")
    else:
        return

    eig_val, eig_vec = np.linalg.eig(cov)

    # 特征值和其对应的特征向量结对，按特征值绝对值从大到小排序
    eig_pairs = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(len(eig_val))]
    eig_pairs.sort(reverse=True)

    # 选取特征值绝对值最大的对应特征向量为主成分
    feature = eig_pairs[0][1]

    new_data_reduced = np.transpose(np.dot(feature, np.transpose(data))).reshape(-1, 1)
    # print(new_data_reduced.shape)

    return new_data_reduced

def sklearn_PCA(features_list):
    X = np.transpose(np.array(features_list))
    pca = PCA(n_components=1)
    pca.fit(X)
    return pca.transform(X)

if __name__ == "__main__":
    # example()

    # 每一行就是一个特征
    features_list = [[2.5, 0.5, 2.2, 1.9, 3.1],
                [1.3, 2, 1, 1.5, 1.1],
                [2.4, 0.7, 2.9, 2.2, 3],
                [1.7, 1.6, 1.1, 1.6, 0.9]
                ]

    print(PCA(features_list))
    print(sklearn_PCA(features_list))

