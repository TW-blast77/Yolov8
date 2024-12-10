from ultralytics import YOLO

# 設定訓練配置
def train_yolo_v8_segmentation():
    # 初始化模型
    model = YOLO("yolov8n.pt")  # 請根據實際路徑替換

    # 訓練配置參數
    model.train(
        data=r".\cfg\coco8.yaml",  # 使用原始字串處理路徑
        epochs=50000,          # 設定訓練的輪次
        batch=88,              # 設定每個訓練批次的大小
        imgsz=640,            # 設定圖片大小 (例如 640x640)
        device=0,             # 設定使用的設備，0 代表 GPU
        workers=4,            # 設定數據加載的工作線程數量
        project="runs/train", # 設定保存訓練結果的目錄
        name="yolo_seg_model",# 訓練結果的文件夾名稱
        exist_ok=True,        # 訓練過程中如果文件夾已經存在，則覆蓋
    )

if __name__ == "__main__":
    train_yolo_v8_segmentation()
