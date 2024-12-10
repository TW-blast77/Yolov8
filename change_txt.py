import os
import shutil

# 源資料夾和目標資料夾
source_folder = r"C:\Users\user\Downloads\1-1"
train_labels_folder = r"C:\Users\user\Desktop\case\YoloV8\project\data\lib_training_dataset\train\labels"
val_labels_folder = r"C:\Users\user\Desktop\case\YoloV8\project\data\lib_training_dataset\val\labels"

# 讀取源資料夾中的 .txt 文件
def read_annotation_file(file_path):
    with open(file_path, 'r') as f:
        annotations = f.readlines()
    return annotations

# 複製標註文件到目標資料夾，根據文件名
def copy_annotation_to_target(source_folder, target_folder):
    # 遍歷源資料夾中的所有 .txt 文件
    for filename in os.listdir(source_folder):
        if filename.endswith(".txt"):
            source_txt_path = os.path.join(source_folder, filename)
            
            # 確定對應的標註文件應該在哪個資料夾
            if os.path.exists(os.path.join(train_labels_folder, filename)):
                target_txt_path = os.path.join(train_labels_folder, filename)
            elif os.path.exists(os.path.join(val_labels_folder, filename)):
                target_txt_path = os.path.join(val_labels_folder, filename)
            else:
                print(f"找不到對應的目標資料夾來覆蓋文件: {filename}")
                continue
            
            # 讀取源資料夾中的標註內容
            annotations = read_annotation_file(source_txt_path)
            
            # 複製標註內容到目標資料夾
            with open(target_txt_path, 'w') as f:
                f.writelines(annotations)
            print(f"已覆蓋標註文件: {filename}")

# 執行複製操作
copy_annotation_to_target(source_folder, train_labels_folder)
copy_annotation_to_target(source_folder, val_labels_folder)

print("標註文件更新完成。")
