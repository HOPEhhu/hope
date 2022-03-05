import torch
import torchvision
import torch.nn as nn
from model import LeNet
import torch.optim as optim
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np


def main():
    #数据集预处理
    transform = transforms.Compose(
        [transforms.ToTensor(),#图像格式转换
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])#使用均值和标准差标准化

    # 50000张训练图片
    # 第一次使用时要将download设置为True才会自动去下载数据集，train:下载训练集，root:下载位置,transform:预处理方法
    train_set = torchvision.datasets.CIFAR10(root='./data', train=True,
                                             download=False, transform=transform)
    #导入训练集，每批36，shuffle：是否随机排序，num_workers:载入数据的线程数，Windows系统只能为0
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=36,
                                               shuffle=True, num_workers=0)

    # 10000张验证图片（测试集）
    # 第一次使用时要将download设置为True才会自动去下载数据集
    val_set = torchvision.datasets.CIFAR10(root='./data', train=False,
                                           download=False, transform=transform)
    val_loader = torch.utils.data.DataLoader(val_set, batch_size=5000,
                                             shuffle=False, num_workers=0)
    val_data_iter = iter(val_loader)#将参数转换为可迭代的迭代器
    val_image, val_label = val_data_iter.next()#通过next方法就可以得到一批数据
    """
    #标签
    classes = ('plane', 'car', 'bird', 'cat',
                'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


    #查看图片
    def imshow(image):
        img = img/2+0.5     #对图像反标准化
        nping=img.numpy()   #转化为原格式
        plt.imshow(np.transpose(nping,(1,2,0)))
        plt.show()

    #打印标签
    print(' '.join('%5s' % classes[val_label[j]] for j in range(4)))
    #打印图片
    imshow(torchvision.utils.make_grid(val_image))
    """ 

    net = LeNet()#实例化模型
    loss_function = nn.CrossEntropyLoss()#定义损失函数
    optimizer = optim.Adam(net.parameters(), lr=0.001)#定义优化器，参数一为要训练的参数，lr:学习率

    for epoch in range(5):  #训练集迭代5次

        running_loss = 0.0#累加损失
        for step, data in enumerate(train_loader, start=0):#遍历训练集样本
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data#分为图像和标签

            # zero the parameter gradients
            optimizer.zero_grad()#清零历史损失梯度
            # forward + backward + optimize
            outputs = net(inputs)#放入模型
            loss = loss_function(outputs, labels)#计算损失
            loss.backward()#反向传播
            optimizer.step()#参数更新

            # print statistics
            running_loss += loss.item()#累加损失
            if step % 500 == 499:    # 每500步打印一次
                with torch.no_grad():#with：上下文管理器，在with内不计算损失梯度
                    outputs = net(val_image)  # [batch, 10]放入测试集到模型
                    predict_y = torch.max(outputs, dim=1)[1]#找到预测最可能的类别
                    accuracy = torch.eq(predict_y, val_label).sum().item() / val_label.size(0)#求预测正确个数
                    #打印：第几轮，第几批，训练误差多少，准确率多少
                    print('[%d, %5d] train_loss: %.3f  test_accuracy: %.3f' %
                          (epoch + 1, step + 1, running_loss / 500, accuracy))
                    running_loss = 0.0

    print('Finished Training')
    #保存训练参数
    save_path = './Lenet.pth'
    torch.save(net.state_dict(), save_path)


if __name__ == '__main__':
    main()
