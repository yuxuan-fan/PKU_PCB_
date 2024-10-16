#面具给的数据集划分，应该是有问题，会出现找不到图片的情况

import os, shutil, random

random.seed(0)
import numpy as np
from sklearn.model_selection import train_test_split

val_size = 0.1           #验证集
test_size = 0.2         #测试集
postfix = 'jpg'         #图片后缀
imgpath = r'E:\dataset\PCB_PKU_marked_prepocessing\random\train_jpgs'

txtpath = r'E:\dataset\PCB_PKU_marked_prepocessing\random\train_labels'



os.makedirs(r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\images\train', exist_ok=True)

os.makedirs(r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\images\val', exist_ok=True)

os.makedirs(r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\images\test', exist_ok=True)


os.makedirs(r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\labels\train', exist_ok=True)

os.makedirs(r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\labels\val', exist_ok=True)

os.makedirs(r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\labels\test', exist_ok=True)

listdir = np.array([i for i in os.listdir(txtpath) if 'txt' in i])
random.shuffle(listdir)
train, val, test = listdir[:int(len(listdir) * (1 - val_size - test_size))], listdir[int(len(listdir) * (1 - val_size - test_size)):int(len(listdir) * (1 - test_size))], listdir[int(len(listdir) * (1 - test_size)):]
print(f'train set size:{len(train)} val set size:{len(val)} test set size:{len(test)}')

for i in train:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\images\train/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\labels\train/{}'.format(i))

for i in val:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\images\val/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\labels\val/{}'.format(i))

for i in test:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\images\train\test/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit\labels\test/{}'.format(i))