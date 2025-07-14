import os
import random
import shutil
from pathlib import Path

# 原始数据路径
image_dir = 'score/images/all'
label_dir = 'score/labels/all'

# 目标划分路径
train_image_dir = 'score/images/train'
val_image_dir = 'score/images/val'
train_label_dir = 'score/labels/train'
val_label_dir = 'score/labels/val'

# 创建目标文件夹
for d in [train_image_dir, val_image_dir, train_label_dir, val_label_dir]:
    os.makedirs(d, exist_ok=True)

# 获取所有图像文件名（不带后缀）
image_files = [f.stem for f in Path(image_dir).glob('*.jpg')]
random.shuffle(image_files)

# 设定划分比例
split_ratio = 0.8
train_num = int(len(image_files) * split_ratio)

train_files = image_files[:train_num]
val_files = image_files[train_num:]

def move_files(file_list, image_dst, label_dst):
    for fname in file_list:
        shutil.copy(f'{image_dir}/{fname}.jpg', f'{image_dst}/{fname}.jpg')
        label_path = f'{label_dir}/{fname}.txt'
        if os.path.exists(label_path):
            shutil.copy(label_path, f'{label_dst}/{fname}.txt')

# 执行移动
move_files(train_files, train_image_dir, train_label_dir)
move_files(val_files, val_image_dir, val_label_dir)

print(f"划分完成：训练集 {len(train_files)}，验证集 {len(val_files)}")
