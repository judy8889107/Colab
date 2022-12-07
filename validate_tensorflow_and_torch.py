import tensorflow as tf
import torch

print(tf.test.is_gpu_available())
print(tf.config.list_physical_devices('GPU'))
print(tf.test.gpu_device_name())

print(torch.__version__)