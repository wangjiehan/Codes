# coding: utf-8
import tensorflow as tf
a = tf.constant([1.0, 2.0], shape=[2], name='a')
b = tf.constant([3.0, 4.0], shape=[2], name='b')
c = a + b
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c))


# 通过tf.device将运算指定到特定的设备上
with tf.device('/cpu:0'):
    d = tf.constant([1.0, 2.0], shape=[2], name='d')
    e = tf.constant([3.0, 4.0], shape=[2], name='e')

# with tf.device('/gpu:0'):
with tf.device('/cpu:0'):
    f = d + e

sess2 = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess2.run(f))

# 查看服务器上可供tf用的gpu和cpu
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
