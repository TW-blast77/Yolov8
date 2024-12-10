import os

# 設定圖片和標註文件所在的目錄
image_folder = 'C:/Users/user/Downloads/1-1'  # 替換為你的圖片目錄路徑

# 遍歷目錄中的所有檔案
for filename in os.listdir(image_folder):
    # 檢查檔案是否是 jpg 文件
    if filename.endswith('.jpg'):
        # 生成對應的 txt 文件名稱
        txt_filename = filename.replace('.jpg', '.txt')
        
        # 檢查是否有對應的 txt 文件
        if not os.path.exists(os.path.join(image_folder, txt_filename)):
            jpg_filepath = os.path.join(image_folder, filename)
            print(f"刪除未標註的圖片: {jpg_filepath}")
            os.remove(jpg_filepath)
