import tensorflow as tf
import numpy as np

# tf
w1 = tf.Variable([[1,2]])
w2 = tf.Variable([[3,4],[5,6]])

#w1 = tf.Variable(tf.random_normal((2,3),stddev=1,seed=1))
#w2 = tf.Variable(tf.random_normal((3,1),stddev=1,seed=1))

y = tf.matmul(w1,w2)

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	print(sess.run(y))

# np
w3 = np.array([[1,2]])
w4 = np.array([[3,4],[5,6]])

z = np.dot(w3,w4)

print(z)
