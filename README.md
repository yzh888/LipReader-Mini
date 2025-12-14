
🚀 Mini LipReader – Simplified Lip Reading Demo

迷你唇语识别模型

📌 Overview | 项目概述

EN:
Mini LipReader is a simplified, ready-to-run lip-reading demo based on the general architecture of TCN-style lip-reading models.
It does not require large datasets or model training.
Simply load a lightweight pre-trained model and run inference on a short lip-movement video.

This project is perfect for:

AI/ML beginners

Students preparing portfolio / interview demos

Anyone who wants a functional lip-reading pipeline without heavy computation

中文：
Mini LipReader 是一个基于 TCN 唇语识别思想构建的 可直接运行的轻量化 Demo。
你无需训练模型，也无需下载大型数据集，只需加载一个轻量模型并对短视频进行推理即可。

本项目非常适合：

人工智能入门学习

需要制作求职作品集或面试 Demo 的同学

希望体验“唇语识别”完整流程但不想折腾训练的人

📁 Project Structure | 项目结构
LipReader-Mini/
│
├── models/
│     └── lipreader_tiny.pth         # Tiny pre-trained model | 轻量预训练模型
│
├── sample/
│     └── sample_lip.mp4             # Sample input video | 示例视频
│
├── infer.py                         # Inference script | 推理脚本
├── requirements.txt                 # Environment deps | 环境依赖
└── README.md                        # This file | 本说明文件

⚙️ Installation | 安装环境
1. Install dependencies | 安装依赖
pip install -r requirements.txt

2. (Optional) Create virtual environment | 可选：创建虚拟环境
python -m venv venv
source venv/Scripts/activate        # Windows Git Bash
# 或
venv\Scripts\activate               # Windows PowerShell

▶️ How to Run Inference | 如何运行推理

Use the provided sample video:

EN:

python infer.py --video sample/sample_lip.mp4 --model models/lipreader_tiny.pth


中文：

使用示例视频运行推理：

python infer.py --video sample/sample_lip.mp4 --model models/lipreader_tiny.pth


If everything works, you will see output like:

Predicted: HELLO


若运行正常，你会看到：

Predicted: HELLO

🧠 How It Works | 原理说明

EN:
The tiny model is a simplified version of lip-reading architectures commonly built using:

CNN backbone for visual feature extraction

Temporal Convolutional Network (TCN) for sequence modeling

FC output layer for classification

Pipeline steps:

Load video

Extract & preprocess frames (resize + normalize)

Stack frames into (Batch × Time × C × H × W)

Feed into the model

Output predicted class

中文：
该轻量模型是常见唇语识别结构的简化版，通常由以下部分组成：

CNN 主干提取视觉特征

时间卷积网络（TCN）建模时序信息

全连接层进行分类输出

整个流水线包括：

加载视频

提取并预处理帧（缩放 + 归一化）

将所有帧堆叠为模型可识别的输入格式

输入模型进行前向传播

输出预测类别# LipReader-Mini
