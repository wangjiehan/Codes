'''
训练单隐层神经网络解决二分类问题
训练神经网络的三个步骤：
（1）定义神经网络的结构和前向传播的输出结果
（2）定义损失函数以及选择反向传播优化算法
（3）生成会话tf.Session并且在训练集上反复运行反向传播优化算法
'''
import tensorflow as tf
from numpy.random import RandomState

# 定义训练数据batch的大小
batch_size = 8

# 随机初始化两层权重矩阵
# 标准差stddev为1，均值mean默认为0，也可以设置。默认类型dtype = tf.float32
# 设置随机种子seed，保证每次出来的随机数都是一样的
w1 = tf.Variable(tf.random_normal([2,3], stddev = 1, seed = 1), name = 'w1')
w2 = tf.Variable(tf.random_normal([3,1], stddev = 1, seed = 1), name = 'w2')

# 定义placeholder位置，让数据通过该位置传入Tensorflow计算图
# 在shape的一个维度上使用None可以方便使用不大的batch大小，防止一个batch中放入大量数据集导致溢出
x = tf.placeholder(tf.float32, shape = (None, 2), name = 'x-input')
y_ = tf.placeholder(tf.float32, shape = (None, 1), name = 'y-input')

# x = tf.constant([[0.7, 0.9]])

# 矩阵相乘，前向算法
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播算法
# tf.clip_by_value(A, min, max)：输入一个张量A，把A中的每一个元素的值都压缩在min和max之间。
# 小于min的让它等于min，大于max的元素的值等于max。
# tf.reduce_mean()函数的作用是求平均值。
learning_rate = 0.001
y = tf.sigmoid(y)
cross_entropy = - tf.reduce_mean(
	y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
	+ (1 - y_) * tf.log(tf.clip_by_value(1 - y, 1e-10, 1.0)))
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

# 通过随机数生成一个模拟数据集。
# X为128行2列，Y：x1 + x2 < 1的样例为正样本，标1；其余为负样本，标0。128行0/1值
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

# 创建会话来运行Tensorflow程序，开始真正运行计算（session之前变量初始化只是定义，并没有真正运行）
# 在使用sess.run(y)获取y的取值之前，必须先初始化w1和w2
with tf.Session() as sess:
	'''
	sess.run(w1.initializer)
	sess.run(w2.initializer)
	'''
	# 或者使用全体参数初始化，不用一个个初始化
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	print(sess.run(w1))
	print(sess.run(w2))
	
	# 设定训练轮数
	STEPS = 5000
	for i in range(STEPS):
		# 每次选取batch_size个样本进行训练
		start = (i * batch_size) % dataset_size
		end = min(start + batch_size, dataset_size)
		
		# 通过选取的样本训练神经网络并在每次循环自动更新参数
		sess.run(
			train_step,
			feed_dict = {x: X[start:end],y_: Y[start:end]}
			)
		if i % 1000 == 0:
			# 每隔一段时间计算在所有数据上的交叉熵并输出
			total_cross_entropy = sess.run(
				cross_entropy, feed_dict = {x: X, y_: Y})
			# %d对应i，整型；%g对应total_cross_entropy，浮点数，根据大小采用%e或%f
			print('After %d training step(s), cross entropy on all data is %g'%
			(i, total_cross_entropy))

