# underwater-targets-recognition

## 项目简介
    本项目基于华为Atlas·200 DK 边缘计算开发套件和YOLOv8，针对海洋场景下的小目标检测任务进行了多方面改进，包括数据、模型结构和训练策略。
    
    我们使用Sea数据集进行训练和评估，该数据集包含海参（holothurian）、海胆（echinus）和、扇贝（scallop）几类海洋生物。

## 环境依赖
    Python >= 3.8
    torch >= 1.8
    ultralytics >= 8.0

## 使用说明
    1. YOLOv8环境安装

    我们使用的是ultralytics(8.0.0) python package,其安装方式如下
   
    'pip install ultralytics'

    2. 构建训练集

    - images/
      - train/
      - val/
    - labels/
      - train/
      - val/

