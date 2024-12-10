import os

def update_class_ids(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split()  # 切割每一行
        class_id = int(parts[0])

        # 更新class_id
        if class_id == 1:
            parts[0] = '0'
        elif class_id == 2:
            parts[0] = '1'

        updated_lines.append(' '.join(parts))  # 更新後的行

    with open(file_path, 'w') as file:
        file.write('\n'.join(updated_lines))  # 寫回到文件

def update_labels_in_directory(directory):
    # 遍歷所有的txt文件
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            update_class_ids(file_path)

# 設定你的路徑
txt_files_directory = r"C:\Users\user\Desktop\case\YoloV8\project\data\lib_training_dataset\train\labels"

update_labels_in_directory(txt_files_directory)
