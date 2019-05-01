import os
import numpy as np
import chainer
from chainer import serializers
import chainer.functions as F
from model import myLinear

class test_myModel():
  def __init__(self, epoch):
    # 学習モデルの読み込み
    # 結果の保存先dirの設定
    self.save_result_src = './myModel_Linear'
    self.my_model = myLinear(k_num = 10)
    serializers.load_npz('{}/epoch{}_myLinearmodel.npz'.format(self.save_result_src.epoch), self.my_model)


  def calc_loss_and_accurancy(self):
    # テストデータ全てを読み込み、lossとaccuracyを計算
    sum_loss = 0
    sum_accu = 0
    # STEP 1---------------------------------------------------
    # load MNIST
    train, test = chainer.datasets.get_mnist()
    test_num = len(test)
    # ---------------------------------------------------------
    # set batch size
    batch_size = 100
    # データを読み込む順番をシャッフルする
    for epoch in range(0, n_epoch):
      perm = np.random.permutation(test_num)
      proceed = 0
      for i in range(0, len(perm), batch_size):
        # STEP 2 ------------------------------------------------
        # input data、target、each datumをminibatchで読み込む
        input,target = train[perm[i:i+batch_size]]
        # reshape each datum
        input = input.reshape(input.shape[0], input.shape[1])
        target = np.array(target, np.int32)
        # increment
        proceed += input.shape[0]
        # input to model
        output = self.my_model(input)
        # -------------------------------------------------------
        # STEP 3 ------------------------------------------------
        # 変数lossに誤差を、変数accuracyに正答率を代入
        loss = F.softmax_cross_entropy(output, target)
        accuracy = F.accuracy(output, target)
        # -------------------------------------------------------
        # add sum of loss and sum of accuracy
        sum_loss += loss.data*input.shape[0]
        sum_accu += accuracy.data*input.shape[0]
        print('test {}/{}'.format(proceed, test_num))
        # lossとaccuracyの値を出力

    # calc loss average and accuracy average
    ave_loss = sum_loss/test_num
    ave_accu = sum_accu/test_num
    print('---------------------------------------')
    print('Test Result')
    print('\t average loss:{} average accuracy:{}'.format(ave_loss, ave_accu))


  def visualize_recognition(self):
    # テストデータから一部を取り出し、モデルの認識方法を可視化
    # 3x3マスの結果画像を生成したい
    import matplotlib.pyplot as plt
    # STEP 1 ----------------------------------------------------
    # load MNIST
    train, test = chainer.datasets.get_mnist()
    test_num = len(test)
    # -----------------------------------------------------------
    # set batch size
    vis_num = 9
    perm = np.random.permutation(test_num)
    # STEP 2 ---------------------------------------------------
    input, target = train[perm[0:0+vis_num]]
    # reshape each datum
    input = input.reshape(input.shape[0], input.shape[1])
    target = np.array(target, np.int32)
    # STEP 3 ---------------------------------------------------
    output = self.my_model(input)
    # ----------------------------------------------------------
    plt.figure(1)
    # visualize process
    for i in range(0, vis_num):
      # set to image
      img = np.array(input[i]*255.0, np.uint8)
      img = np.reshape(img, (28, 28))
      # get target answer
      target_answer = target[i]
      # get output answer
      # np.argmaxで最も高い要素を持つ引数を取得
      output_answer = np.argmax(output[i].data)

      # append image and label to subplot
      plt.subplot(3,3,i+1) # 引数はrow数、col数、何番目に入れるか
      plt.gray() # mnistはグレースケール画像
      plt.imshow(img) # 画像を入れ込む
      plt.xlabel('real answer:{} \n model answer:{}'.format(target_answer, output_answer))
    
    # adjust
    plt.tight_layout()
    # save image 
    plt.savefig('{}/result.png'.format(self.save_result_src)) # 保存先のpathを指定して画像を保存
    # visualize
    plt.show() # 画像を表示
