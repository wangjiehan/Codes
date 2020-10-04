import tensorflow as tf
x = tf.Variable(0)
y = tf.Variable(1)
# y.assign(x)    # 没用
y = y.assign(x)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print (sess.run(x))
    print (sess.run(y))
    print (sess.run(x))

