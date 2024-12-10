import os
import shutil
import random
import tkinter as tk
from tkinter import filedialog

# 選擇資料夾功能
def select_folder(title="選擇資料夾"):
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗
    folder_path = filedialog.askdirectory(title=title)
    return folder_path

# 解析標註文件中的每一行
def parse_annotation_line(line):
    # 假設標註格式為： <<ImageDisplayed>> image_name.jpg class_id x_center y_center width height
    parts = line.strip().split(' ')
    if len(parts) != 7 or parts[0] != "<<ImageDisplayed>>":
        return None
    image_name = parts[1]
    class_id = int(parts[2])
    x_center = float(parts[3])
    y_center = float(parts[4])
    width = float(parts[5])
    height = float(parts[6])
    return (image_name, class_id, x_center, y_center, width, height)

# 選擇圖片和標註文件所在的資料夾
image_folder = select_folder("選擇圖片資料夾")
label_folder = image_folder  # 假設圖片和標註文件在同一資料夾

# 選擇保存訓練集和驗證集的資料夾
output_folder = select_folder("選擇保存訓練集和驗證集的資料夾")

# 設定目標資料夾，並按比例分配
train_image_folder = os.path.join(output_folder, 'train/images')
train_label_folder = os.path.join(output_folder, 'train/labels')
val_image_folder = os.path.join(output_folder, 'val/images')
val_label_folder = os.path.join(output_folder, 'val/labels')

# 創建資料夾結構
os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(train_label_folder, exist_ok=True)
os.makedirs(val_image_folder, exist_ok=True)
os.makedirs(val_label_folder, exist_ok=True)

# 獲取所有的圖片和標註文件
files = os.listdir(image_folder)

# 過濾出所有的圖片和標註文件
image_files = [f for f in files if f.endswith('.jpg')]
label_files = [f.replace('.jpg', '.txt') for f in image_files]  # 假設每個 jpg 檔案對應一個 txt 檔案

# 確保每個圖片都有對應的標註文件
image_label_pairs = [(img, lbl) for img, lbl in zip(image_files, label_files)
                     if os.path.exists(os.path.join(label_folder, lbl))]

# 設定訓練集和驗證集的比例
train_ratio = 0.8
train_size = int(len(image_label_pairs) * train_ratio)

# 隨機打亂圖片和標註文件的順序
random.shuffle(image_label_pairs)

# 分配訓練集和驗證集
train_pairs = image_label_pairs[:train_size]
val_pairs = image_label_pairs[train_size:]

# 轉換標註格式並寫入 YOLOv8 格式
def convert_to_yolo_format(annotation_lines, image_width, image_height):
    yolo_annotations = []
    for line in annotation_lines:
        # 每行的格式應該是 image_name, class_id, x_center, y_center, width, height
        image_name, class_id, x_center, y_center, width, height = line
        # 寫入 YOLO 格式，座標已經是相對比例，範圍 [0, 1]
        yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")
    return yolo_annotations

# 移動檔案到對應資料夾並轉換標註格式
def move_files_and_convert(pairs, image_folder, label_folder, target_image_folder, target_label_folder):
    for img, lbl in pairs:
        # 圖片和標註檔案的原路徑
        img_path = os.path.join(image_folder, img)
        lbl_path = os.path.join(label_folder, lbl)
        
        # 目標路徑
        target_img_path = os.path.join(target_image_folder, img)
        target_lbl_path = os.path.join(target_label_folder, lbl)

        # 讀取標註文件
        with open(lbl_path, 'r') as f:
            annotation_lines = []
            for line in f:
                parsed_line = parse_annotation_line(line)
                if parsed_line:
                    annotation_lines.append(parsed_line)
        
        # 假設圖片的尺寸已知，這裡需要根據你的圖片大小來進行設置
        # 一般來說，你可以使用 PIL 或 OpenCV 來獲取圖片的寬高
        # 這裡我們假設所有圖片的尺寸都相同，例如 1920x1080
        image_width, image_height = 1920, 1080
        
        # 轉換為 YOLO 格式
        yolo_annotations = convert_to_yolo_format(annotation_lines, image_width, image_height)
        
        # 寫入新的 YOLO 格式標註文件
        with open(target_lbl_path, 'w') as f:
            f.write('\n'.join(yolo_annotations))

        # 移動圖片和標註檔案
        shutil.move(img_path, target_img_path)

# 將訓練集和驗證集的圖片和標註檔案移動到對應資料夾並轉換格式
move_files_and_convert(train_pairs, image_folder, label_folder, train_image_folder, train_label_folder)
move_files_and_convert(val_pairs, image_folder, label_folder, val_image_folder, val_label_folder)

print(f"訓練集和驗證集資料已經成功移動並轉換格式。")
