import chainer
from chainer import cuda,Function,gradient_check,Variable,optimizers,serializers,utils
from chainer import Link,Chain,ChainList
import chainer.functions as F
import chainer.links as L
import numpy as np


x = np.array([[0,0],[0,1],[1,0],[1,1]],dtype = np.float32)
t = np.array([[0],[1],[1],[0]],dtype = np.float32)

class Model(Chain):
  def __init__(self):
    super(Model, self).__init__(
      l1 = L.Linear(2,3),
      l2 = L.Linear(3,1),
    )
  
  def __call__(self, input, target):
    x = Variable(input)
    t = Variable(target)
    h = F.sigmoid(self.l1(x))
    loss = F.mean_squared_error(self.l2(h), t)
    return loss
  

model = Model()
optimizer = optimizers.Adam()
optimizer.setup(model)

print('training now...\n')
for n in range(0, 500):
  model.cleargrads()
  loss = model(x,t)
  loss.backward()
  optimizer.update()
  # print(loss)
  # print(loss.data)

print('Test Loss')
test = model(x,t)
print(test.data)