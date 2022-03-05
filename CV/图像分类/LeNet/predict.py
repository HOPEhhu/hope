import torch
import torchvision.transforms as transforms
from PIL import Image

from model import LeNet

#预测
def main():
    transform = transforms.Compose(
        [transforms.Resize((32, 32)),#调整图片尺寸
         transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    net = LeNet()
    net.load_state_dict(torch.load('Lenet.pth'))#载入权重文件

    im = Image.open('1.jpg')#载入图像
    im = transform(im)  # [C, H, W]#图片预处理
    im = torch.unsqueeze(im, dim=0)  # [N, C, H, W]，#增加维度

    with torch.no_grad():
        outputs = net(im)
        predict = torch.max(outputs, dim=1)[1].numpy()#找出最可能的类别
    print(classes[int(predict)])


if __name__ == '__main__':
    main()
