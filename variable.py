import numpy as np
import tensorflow as tf
a = tf.Variable(0)
b = tf.constant(40)

mid = tf.add(a,b)
final = tf.assign(a,mid)
var = tf.initialize_all_variables()
session = tf.Session()
session.run(var)
for i in range(3):
    #line used to run final graph
    session.run(final)
    #this is used to print variable
    print(session.run(a))
session.close()
