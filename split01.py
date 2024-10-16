#数据集划分，需要自己创建train、val、test文件夹


import os
import shutil
import random


def SplitDatasets(src_img_folder, src_label_folder, Dest_Folder, train_ratio, val_ratio, test_ratio):
    # 创建数据集存放文件夹

    Dest_train_img_folder = os.path.join(Dest_Folder, 'train', 'images')
    Dest_train_label_folder = os.path.join(Dest_Folder, 'train', 'labels')
    Dest_valid_img_folder = os.path.join(Dest_Folder, 'valid', 'images')
    Dest_valid_label_folder = os.path.join(Dest_Folder, 'valid', 'labels')
    Dest_Test_img_folder = os.path.join(Dest_Folder, 'test', 'images')
    Dest_Test_label_folder = os.path.join(Dest_Folder, 'test', 'labels')
    Dir_List = [Dest_train_img_folder, Dest_train_label_folder,
                Dest_valid_img_folder, Dest_valid_label_folder,
                Dest_Test_img_folder, Dest_Test_label_folder]
    for dir in Dir_List:
        if not os.path.exists(dir):
            os.mkdir(dir)

    All_Files = [item for item in os.listdir(src_img_folder)] 
    random.shuffle(All_Files)  # 打乱顺序
    Train_Sets = All_Files[:int(len(All_Files)*train_ratio)]  # 随机选取一定比例作为训练集
    Valid_Sets, Test_Sets = [], []

    # 获取验证集和测试集
    if val_ratio > 0:
        if test_ratio > 0:  # 验证集和测试集同时存在
            Valid_Sets = All_Files[int(len(All_Files)*train_ratio):int(len(All_Files)-int(len(All_Files)*test_ratio))]
            Test_Sets = All_Files[int(len(All_Files)-test_ratio*len(All_Files)):]
        else:  # 测试集不存在，那就只制作验证集咯
            Valid_Sets = All_Files[int(len(All_Files)*train_ratio):]
    elif test_ratio > 0:  # 验证集不存在，那就只制作测试集咯
        Test_Sets = All_Files[int(len(All_Files)*train_ratio):]

    # 拷贝训练集文件到相应目录
    for file in Train_Sets:
        shutil.copy2(os.path.join(src_img_folder, file), Dest_train_img_folder)
        print(f"copied {file} to {Dest_train_img_folder}")
        shutil.copy2(os.path.join(src_label_folder, file.split('.')[0]+'.txt'), Dest_train_label_folder)
        print(f"copied {file.split('.')[0]+'.txt'} to {Dest_train_label_folder}")

    # 拷贝验证集文件到相应目录
    for file in Valid_Sets:
        shutil.copy2(os.path.join(src_img_folder, file), Dest_valid_img_folder)
        print(f"copied {file} to {Dest_valid_img_folder}")
        shutil.copy2(os.path.join(src_label_folder, file.split('.')[0]+'.txt'), Dest_valid_label_folder)
        print(f"copied {file.split('.')[0]+'.txt'} to {Dest_valid_label_folder}")

    # 拷贝测试集文件到相应目录
    for file in Test_Sets:
        shutil.copy2(os.path.join(src_img_folder, file), Dest_Test_img_folder)
        print(f"copied {file} to {Dest_Test_img_folder}")
        shutil.copy2(os.path.join(src_label_folder, file.split('.')[0]+'.txt'), Dest_Test_label_folder)
        print(f"copied {file.split('.')[0]+'.txt'} to {Dest_Test_label_folder}")


# 定义训练集和测试集的比例
train_ratio = 0.6
val_ratio = 0.2
test_ratio = 0.2

# 源文件夹路径
src_img_folder = r'E:\dataset\PCB_PKU_marked_prepocessing\random\train_jpgs'
src_label_folder = r'E:\dataset\PCB_PKU_marked_prepocessing\random\train_labels'

# 目标文件夹
Dest_Folder = r'E:\dataset\PCB_PKU_marked_prepocessing\random\afterSplit'

# 调用函数， 进行数据集划分
SplitDatasets(src_img_folder, src_label_folder, Dest_Folder, train_ratio, val_ratio, test_ratio)
