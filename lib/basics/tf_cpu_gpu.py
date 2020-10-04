# coding: utf-8
import tensorflow as tf
a = tf.constant([1.0, 2.0], shape=[2], name='a')
b = tf.constant([3.0, 4.0], shape=[2], name='b')
c = a + b
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c))


# ͨ��tf.device������ָ�����ض����豸��
with tf.device('/cpu:0'):
    d = tf.constant([1.0, 2.0], shape=[2], name='d')
    e = tf.constant([3.0, 4.0], shape=[2], name='e')

# with tf.device('/gpu:0'):
with tf.device('/cpu:0'):
    f = d + e

sess2 = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess2.run(f))

# �鿴�������Ͽɹ�tf�õ�gpu��cpu
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
