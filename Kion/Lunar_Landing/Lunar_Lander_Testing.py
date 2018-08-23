import tensorflow as tf
import gym
import os
import numpy as np
import Box2D as box
env = gym.make("LunarLander-v2")
max_steps_per_episode = 10000
path = "./lunarlander-pg/"
testing_episodes = 5
num_actions = 4
state_size = 8
class Agent:
    def __init__(self, num_actions, state_size):
        initializer = tf.contrib.layers.xavier_initializer()

        self.input_layer = tf.placeholder(dtype=tf.float32, shape=[None, state_size])

        # Neural net starts here

        hidden_layer = tf.layers.dense(self.input_layer, 8, activation=tf.nn.relu, kernel_initializer=initializer)
        hidden_layer_2 = tf.layers.dense(hidden_layer, 5, activation=tf.nn.relu, kernel_initializer=initializer)
        hidden_layer_3 = tf.layers.dense(hidden_layer_2, 7, activation=tf.nn.relu, kernel_initializer=initializer)
        # Output of neural net
        out = tf.layers.dense(hidden_layer_3, num_actions, activation=None)

        self.outputs = tf.nn.softmax(out)
        self.choice = tf.argmax(self.outputs, axis=1)

        # Training Procedure
        self.rewards = tf.placeholder(shape=[None, ], dtype=tf.float32)
        self.actions = tf.placeholder(shape=[None, ], dtype=tf.int32)

        one_hot_actions = tf.one_hot(self.actions, num_actions)

        cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=out, labels=one_hot_actions)

        self.loss = tf.reduce_mean(cross_entropy * self.rewards)

        self.gradients = tf.gradients(self.loss, tf.trainable_variables())

        # Create a placeholder list for gradients
        self.gradients_to_apply = []
        for index, variable in enumerate(tf.trainable_variables()):
            gradient_placeholder = tf.placeholder(tf.float32)
            self.gradients_to_apply.append(gradient_placeholder)

        # Create the operation to update gradients with the gradients placeholder.
        optimizer = tf.train.AdamOptimizer(learning_rate=3e-2)
        self.update_gradients = optimizer.apply_gradients(zip(self.gradients_to_apply, tf.trainable_variables()))
agent = Agent(num_actions, state_size)
saver = tf.train.Saver(max_to_keep=2)
with tf.Session() as sess:
    checkpoint = tf.train.get_checkpoint_state(path)
    saver.restore(sess, checkpoint.model_checkpoint_path)

    for episode in range(testing_episodes):

        state = env.reset()

        episode_rewards = 0

        for step in range(max_steps_per_episode):

            env.render()

            # Get Action
            action_argmax = sess.run(agent.choice, feed_dict={agent.input_layer: [state]})
            action_choice = action_argmax[0]

            state_next, reward, done, _ = env.step(action_choice)
            state = state_next

            episode_rewards += reward

            if done or step + 1 == max_steps_per_episode:
                print("Rewards for episode " + str(episode) + ": " + str(episode_rewards))
                break

env.close()