import tensorflow as tf

x = tf.constant([
    [[2, 3], [4, 5]],
    [[6, 7], [8, 9]]

],
    tf.int32)

d1 = tf.range(0, tf.shape(x)[0])

print(d1.numpy())

d2 = tf.tile(d1, multiples=[tf.shape(x)[1]])

print(d2.numpy())

d3 = tf.reshape(d2, shape=tf.shape(x)[:-1])

print(d3.numpy())


