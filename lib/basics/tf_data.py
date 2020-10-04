import tensorflow as tf
import numpy as np

a = [[1,2],[3,4],[5,6],[7,8],[9,10]]
b = [25,20,22,24,26]
np.savez('test.npz', np.array(a), np.array(b))
with np.load("test.npz") as data:
	features = data["arr_0"]
	labels = data["arr_1"]

print(features)
print(labels)


'''
with tf.Session() as sess1:
	sess1.run(tf.global_variables_initializer())

	# Assume that each row of `features` corresponds to the same row as `labels`.
	assert features.shape[0] == labels.shape[0]

	features_placeholder = tf.placeholder(features.dtype, features.shape)
	labels_placeholder = tf.placeholder(labels.dtype, labels.shape)

	dataset = tf.data.Dataset.from_tensor_slices((features_placeholder, labels_placeholder))
	iterator = dataset.make_initializable_iterator()
	next_element = iterator.get_next()
	sess1.run(iterator.initializer, feed_dict={features_placeholder: features,
								  labels_placeholder: labels})

	for i in range(4):
		print(sess1.run(next_element))
'''

epoch = 2
batch_size = 3
with tf.Session() as sess2:
	sess2.run(tf.global_variables_initializer())


	# Assume that each row of `features` corresponds to the same row as `labels`.
	assert features.shape[0] == labels.shape[0]

	features_placeholder = tf.placeholder(features.dtype, features.shape)
	labels_placeholder = tf.placeholder(labels.dtype, labels.shape)

	dataset = tf.data.Dataset.from_tensor_slices((features_placeholder, labels_placeholder))
	dataset = dataset.repeat(epoch)
	dataset = dataset.batch(batch_size)
	iterator = dataset.make_initializable_iterator()
	next_element = iterator.get_next()
	sess2.run(iterator.initializer, feed_dict={features_placeholder: features,
								  labels_placeholder: labels})
								  

	while True:
		try:
			batch_x, batch_y = sess2.run(next_element)
			print(batch_x, batch_y)
		except:
			break


epoch = 2
batch_size = 3
with tf.Session() as sess3:
	sess3.run(tf.global_variables_initializer())
	filenames = ["tmp.txt"]
	dataset = tf.data.TextLineDataset(filenames)

	dataset = dataset.repeat(epoch)
	dataset = dataset.batch(batch_size)
	iterator = dataset.make_initializable_iterator()
	next_element = iterator.get_next()
	sess3.run(iterator.initializer)
								  
	while True:
		try:
			batch_seq = sess3.run(next_element)
			print(batch_seq)
			# print(batch_seq[0].split()[0])
		except:
			break
