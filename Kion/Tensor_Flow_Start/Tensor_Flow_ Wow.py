import matplotlib.pyplot as p
import tensorflow as tf
tf.reset_default_graph()

tf.reset_default_graph()

input_data = tf.placeholder(dtype=tf.float32, shape=None)
output_data = tf.placeholder(dtype=tf.float32, shape=None)

slope = tf.Variable(5.0, dtype=tf.float32)
intercept = tf.Variable(3.4, dtype=tf.float32)
op = slope * input_data + intercept

error = op - output_data
squared_error = tf.square(error)
loss = tf.reduce_mean(squared_error)
x_values = [0, 1, 2, 3, 4]
y_values = [1, 3, 5, 7, 9]
init = tf.global_variables_initializer()

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.005)
train = optimizer.minimize(loss)
with tf.Session() as sess:
    sess.run(init)
    for i in range(2000):
        sess.run(train, feed_dict={input_data: x_values, output_data: y_values})
        if i % 100 == 0:
            print(sess.run([slope, intercept]))
            p.plot(x_values, sess.run(op, feed_dict={input_data: x_values}))
    print(sess.run(loss, feed_dict={input_data: x_values, output_data: y_values}))
    p.plot(x_values, y_values, 'ro', 'Training Data')
    p.plot(x_values, sess.run(op, feed_dict={input_data: x_values}))


    p.show()