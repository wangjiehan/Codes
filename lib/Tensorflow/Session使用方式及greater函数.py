import tensorflow as tf
'''
tf.greater(A, B)返回bool值，即A是否比B大
'''
v = tf.Variable(tf.constant(1.0, shape=[1]), name = 'v')
with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	print(v)
	print(sess.run(v))
	print(v.eval())

tmp = tf.greater(5,4)
with tf.Session() as sess_0:
	print(tmp.eval())

with tf.Session() as sess_1:
	print(sess_1.run(tmp))

v1 = tf.constant([1.0,2.0,3.0,4.0])
v2 = tf.constant([4.0,3.0,2.0,1.0])
sess_3 = tf.InteractiveSession()
print(tf.greater(v1, v2).eval())
sess_3.close()
