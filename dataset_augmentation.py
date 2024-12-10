import os
import cv2
import numpy as np
from albumentations import (HorizontalFlip, RandomBrightnessContrast, ShiftScaleRotate, RandomGamma, RandomSizedCrop, Compose)

# 定義資料增強的變換
augmentations = {
    'flip': HorizontalFlip(p=1.0),
    'rotate': ShiftScaleRotate(shift_limit=0.1, scale_limit=0.1, rotate_limit=30, p=1.0),
    'translate': ShiftScaleRotate(shift_limit=0.2, scale_limit=0.2, rotate_limit=0, p=1.0),
    'brightness_contrast': RandomBrightnessContrast(p=1.0),
    'crop': RandomSizedCrop(min_max_height=(200, 400), height=400, width=400, p=1.0),
}

# 讀取標註檔並進行增強操作
def augment_label(label_path, output_label_path, augment_type):
    with open(label_path, 'r') as f:
        lines = f.readlines()
    
    augmented_lines = []
    
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        x_center, y_center, width, height = map(float, parts[1:])
        
        if augment_type == 'flip':
            x_center = 1 - x_center  # 水平翻轉
        elif augment_type == 'rotate':
            # 若進行旋轉，根據旋轉角度更新 bounding box
            pass  # 這裡需要進行旋轉後的 bounding box 計算
        elif augment_type == 'translate':
            # 若進行平移，根據平移調整 bounding box
            pass  # 這裡需要進行平移後的 bounding box 計算
        elif augment_type == 'brightness_contrast':
            # 調整亮度對比度後的變化
            pass
        elif augment_type == 'crop':
            # 隨機裁剪時可能會改變 bounding box，這裡需要重新計算
            pass
        
        # 創建新的標註
        augmented_lines.append(f"{class_id} {x_center} {y_center} {width} {height}\n")
    
    # 保存增強後的標註
    with open(output_label_path, 'w') as f:
        f.writelines(augmented_lines)

# 增強圖像並保存，對應標註文件同步增強
def augment_image_and_label(image_path, label_path, output_image_path, output_label_path, augment_type):
    image = cv2.imread(image_path)
    if image is None:
        return
    
    # 進行資料增強
    augmented = augmentations[augment_type](image=image)['image']
    cv2.imwrite(output_image_path, augmented)
    
    # 同步增強標註文件
    augment_label(label_path, output_label_path, augment_type)

# 處理整個資料集
def augment_dataset(image_dir, label_dir, augment_count=5):
    # 瀏覽所有圖像文件
    for root, _, files in os.walk(image_dir):
        for file in files:
            if file.endswith(('.jpg', '.png', '.jpeg')):
                image_path = os.path.join(root, file)
                # 尋找對應的標註文件
                label_file = file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt')
                label_path = os.path.join(label_dir, label_file)
                
                # 確保標註文件存在
                if not os.path.exists(label_path):
                    continue
                
                # 生成增強後的圖片和標註
                for augment_type in augmentations.keys():
                    aug_image_name = f"{os.path.splitext(file)[0]}_{augment_type}.jpg"
                    output_image_path = os.path.join(image_dir, aug_image_name)  # 保存在原圖資料夾
                    output_label_path = os.path.join(label_dir, f"{os.path.splitext(file)[0]}_{augment_type}.txt")  # 保存在標註資料夾
                    
                    augment_image_and_label(image_path, label_path, output_image_path, output_label_path, augment_type)
               

# 使用範例，將路徑對應到你的訓練資料夾
image_directory = r"C:/Users/user/Desktop/case/YoloV8/project/data/lib_training_dataset/train/images"  # 訓練圖像資料夾
label_directory = r"C:/Users/user/Desktop/case/YoloV8/project/data/lib_training_dataset/train/labels"  # 標註資料夾
augment_count = 5  # 每張圖片生成 5 張增強圖像

# 執行增強
augment_dataset(image_directory, label_directory, augment_count)
