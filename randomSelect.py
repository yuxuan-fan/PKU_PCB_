# import os
# import random
# import shutil
# # 源数据路径
# path = r'E:\dataset\PCB_PKU_marked_prepocessing\增强后\labels'
# # 训练文件夹
# train_dir = r'E:\dataset\PCB_PKU_marked_prepocessing\random\train'
# # 测试文件夹
# test_dir = r'E:\dataset\PCB_PKU_marked_prepocessing\random\test'
# # 列出原始数据集路径下的所有文件
# files = os.listdir(path)
# # 随机抽取11725张图片
# random_files = random.sample(files, 2650)
# # 将选出的11725张图片复制到训练文件夹中
# for i in random_files:
#     shutil.copy(os.path.join(path,i), train_dir)
# # 将剩余图片复制到测试文件夹中
# for i in files:
#     if i not in random_files:
#         shutil.copy(os.path.join(path,i), test_dir)



# 图片标签对应
import os
import shutil
labels_dir = r"E:\dataset\PCB_PKU_marked_prepocessing\random\train"
images_dir = r"E:\dataset\PCB_PKU_marked_prepocessing\增强后\images"
new_dir = r"E:\dataset\PCB_PKU_marked_prepocessing\random\train_jpg"
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
for label_name in os.listdir(labels_dir):
    label_name = label_name.split('.')[0]
    file_name = label_name + '.jpg'
    file_src = os.path.join(images_dir, file_name)
    file_dst = os.path.join(new_dir, file_name)
    shutil.copyfile(file_src, file_dst)