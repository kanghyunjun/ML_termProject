
# coding: utf-8

# In[7]:


import tensorflow as tf
import numpy as np
tf.set_random_seed(777)  # for reproducibility

xy = np.loadtxt('yeast data.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

train_size = int(len(y_data)*0.8)
test_size = len(y_data) - train_size

trainX = np.array(x_data[0:train_size])
trainY = np.array(y_data[0:train_size])

testX = np.array(x_data[train_size:len(x_data)])
testY = np.array(y_data[train_size:len(y_data)])

#parameters
nb_classes = 10  # 0 ~ 9
learning_rate = 0.1
count = 0
correct_count = 0

#input place holders
X = tf.placeholder(tf.float32, [None, 8])
Y = tf.placeholder(tf.int32, [None, 1])  # 0 ~ 9, shape=(?, 1)
Y_one_hot = tf.one_hot(Y, nb_classes)  # one hot shape=(?, 1, 10)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes]) # shape=(?, 10)

W1 = tf.Variable(tf.random_normal([8, 20]), name='weight1')
b1 = tf.Variable(tf.random_normal([20]), name='bias1')
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)

#Hidden Layer1
W2 = tf.Variable(tf.random_normal([20, 30]), name='weight2')
b2 = tf.Variable(tf.random_normal([30]), name='bias2')
layer2 = tf.nn.relu(tf.matmul(layer1, W2) + b2)

#Hidden Layer2
W3 = tf.Variable(tf.random_normal([30, 40]), name='weight3')
b3 = tf.Variable(tf.random_normal([40]), name='bias3')
layer3 = tf.nn.relu(tf.matmul(layer2, W3) + b3)

W4 = tf.Variable(tf.random_normal([40, nb_classes]), name='weight4')
b4 = tf.Variable(tf.random_normal([nb_classes]), name='bias4')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(layer3, W4) + b4
hypothesis = tf.nn.softmax(logits)

# Cross entropy cost/loss
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(3000):
        sess.run(optimizer, feed_dict={X: trainX, Y: trainY})
        if step % 100 == 0:
            loss, acc = sess.run([cost, accuracy], feed_dict={
                                 X: trainX, Y: trainY})
            print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(
                step, loss, acc))

    pred = sess.run(prediction, feed_dict={X: testX})
    for p, y in zip(pred, testY.flatten()):
        print("Prediction: {} True Y: {} [{}]".format(p, int(y), p == int(y)))
        count = count + 1
        if p == int(y):
            correct_count = correct_count + 1
print("\nPrecision: {:.4}".format(correct_count/count))

