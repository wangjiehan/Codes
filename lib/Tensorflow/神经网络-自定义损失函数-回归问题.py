'''
训练单层（无隐层）神经网络，自定义损失函数，解决回归问题（P79 销量预测）
'''
import tensorflow as tf
from numpy.random import RandomState

batch_size = 8

# 两个输入节点，两件商品
x = tf.placeholder(tf.float32, shape = (None, 2), name = 'x-input')
# 回归问题一般只有一个输出节点
y_ = tf.placeholder(tf.float32, shape = (None, 1), name = 'y-input')

# 定义一个单层神经网络前向传播过程
w1 = tf.Variable(tf.random_normal([2, 1], stddev = 1, seed = 1))
y = tf.matmul(x, w1)

# 定义损失函数和反向传播算法
learning_rate = 0.001
loss_less = 10
loss_more = 1
loss = tf.reduce_sum(tf.where(tf.greater(y, y_),
								(y - y_) * loss_more,
								(y_ - y) * loss_less))
train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss)

# 通过随机数生成一个模拟数据集。
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
# -0.05 ~ 0.05 的随机数
Y = [[x1 + x2 + rdm.rand()/10.0 - 0.05] for (x1, x2) in X]

with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)

	STEPS = 5000
	for i in range(STEPS):
		# 每次选取batch_size个样本进行训练
		start = (i * batch_size) % dataset_size
		end = min(start + batch_size, dataset_size)

		sess.run(
			train_step,
			feed_dict = {x: X[start:end],y_: Y[start:end]}
			)
		if i % 1000 == 0:
			loss_res = sess.run(loss, feed_dict = {x: X, y_: Y})
			print('After ' + str(i) + 'training step(s), the loss is ' 
			+ str(loss_res) + '. ')
	print(sess.run(loss, feed_dict = {x: X, y_: Y}))
	print(sess.run(w1))
