import numpy as np
import tensorflow as tf
x = tf.placeholder("float",[None,3])
y = x**2
x_data = [[1,2,3],[4,5,6]]
session = tf.Session()
#line used to run final graph
result = session.run(y,feed_dict={x:x_data})
#this is used to print variable
print(result)
session.close()
