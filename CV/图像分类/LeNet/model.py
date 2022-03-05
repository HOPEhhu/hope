import torch.nn as nn
import torch.nn.functional as F

#定义LeNet模型
class LeNet(nn.Module):  #定义类，继承nn.Module
    def __init__(self):  #初始化函数，实现在初始化网络中需要使用的网络层结构
        super(LeNet, self).__init__()#涉及多继承，一般要加上super函数
        self.conv1 = nn.Conv2d(3, 16, 5)#定义卷积层，输入特征层深度3，使用16个卷积核，卷积核大小为5
        self.pool1 = nn.MaxPool2d(2, 2)#定义下采样层，池化核大小围为2*2,步距也为2
        self.conv2 = nn.Conv2d(16, 32, 5)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(32*5*5, 120)#全连接层，输入为一位，所以要将输入展平，输入32*5*5，输出120
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):  #forward定义正向传播过程，当网络实例化后，将参数传入实例中，就会进行正向传播，x:输入数据
        x = F.relu(self.conv1(x))    # input(3(深度), 32(宽度), 32(高度)) output(16, 28, 28)，relu:激活函数
        x = self.pool1(x)            # output(16, 14, 14)
        x = F.relu(self.conv2(x))    # output(32, 10, 10)
        x = self.pool2(x)            # output(32, 5, 5)
        x = x.view(-1, 32*5*5)       # output(32*5*5)；展平为一维，-1：第一个维度自动推理，32*5*5：第二维度
        x = F.relu(self.fc1(x))      # output(120)
        x = F.relu(self.fc2(x))      # output(84)
        x = self.fc3(x)              # output(10)
        #计算卷积交叉熵的内部已经实现了softmax方法，在这里不需要添加softmax层
        return x


