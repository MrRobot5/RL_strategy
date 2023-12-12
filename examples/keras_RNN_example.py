"""
Sequential 模型的简单示例，该模型可以处理整数序列，将每个整数嵌入 64 维向量中，然后使用 LSTM 层处理向量序列。

循环神经网络 (RNN) 是一类神经网络，它们在序列数据（如时间序列或自然语言）建模方面非常强大。
简单来说，RNN 层会使用 for 循环对序列的时间步骤进行迭代，同时维持一个内部状态，对截至目前所看到的时间步骤信息进行编码。

Keras 中有三种内置 RNN 层：
keras.layers.SimpleRNN，一个全连接 RNN，其中前一个时间步骤的输出会被馈送至下一个时间步骤。
keras.layers.GRU，最初由 Cho 等人于 2014 年提出。
keras.layers.LSTM，最初由 Hochreiter 和 Schmidhuber 于 1997 年提出。

ref: https://tensorflow.google.cn/guide/keras/rnn?hl=zh-cn
@since 2023年12月12日10:12:17
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# tf.keras 是用于构建和训练深度学习模型的 TensorFlow 高阶 API。
model = keras.Sequential()
# Add an Embedding layer expecting input vocab of size 1000, and
# output embedding dimension of size 64.
model.add(layers.Embedding(input_dim=1000, output_dim=64))

# Add a LSTM layer with 128 internal units.
model.add(layers.LSTM(128))

# Add a Dense layer with 10 units.
model.add(layers.Dense(10))

model.summary()