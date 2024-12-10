
# YOLO Segmentation Model Project

This repository contains various scripts used for training, testing, and managing a YOLO-based segmentation model. The scripts cover tasks from video prediction to dataset augmentation and model training.

## Scripts Overview

### `YOLOV8-Annotation-Converter.py`
This script converts annotations into YOLOv8-compatible format and splits datasets into training and validation sets.

### `change_txt.py`
This script updates annotation files by replacing their content based on corresponding training or validation labels.

### `change_txt2.py`
This script modifies class IDs within annotation files, such as remapping class IDs from 1 and 2 to 0 and 1.

### `check_cuda.py`
This script checks if CUDA (GPU acceleration) is available on the system and provides details about the available devices.

### `clean_images.py`
This script removes image files that do not have corresponding annotation files, cleaning the dataset.

### `dataset_augmentation.py`
This script performs data augmentation on the training images and synchronizes the augmentation with the associated annotations.

### `train.py`
This is the main training script for YOLOv8 segmentation. It initializes the YOLOv8 model, trains it on the dataset, and saves the results.

### `Video_to_predict.py`
This script processes video files to apply YOLOv8 inference on each frame, visualizing object detection results in real time.

## Directory Structure

Here is a breakdown of the main directories and files in the project:

```
C:.
├─ cfg
│   └─ Configuration files for model setup
├─ data
│   └─ Dataset for training and validation
│       ├─ lib_training_dataset
│       │   ├─ train          # Training images and labels
│       │   └─ val            # Validation images and labels
└─ runs
    ├─ detect                 # Outputs from detection tasks
    └─ train                  # Training results, including model weights and metrics
        └─ yolo_seg_model
            └─ weights        # Model weights and checkpoint files
```

## Requirements

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### Additional Notes

- Ensure CUDA is installed for GPU acceleration. Use `check_cuda.py` to verify CUDA installation.
- Augment datasets using `dataset_augmentation.py` to improve model performance.


## Operation Steps

1. **Prepare Dataset**
   - Organize your dataset into the `data/lib_training_dataset/train` and `data/lib_training_dataset/val` directories.
   - Ensure each image has a corresponding annotation file in `.txt` format.

2. **Clean Dataset**
   - Run `clean_images.py` to remove any images without annotations.

3. **Verify GPU Setup**
   - Execute `check_cuda.py` to ensure your system is GPU-ready for training.

4. **Convert Annotations**
   - Use `YOLOV8-Annotation-Converter.py` to split and convert dataset annotations into YOLOv8 format.

5. **Perform Data Augmentation**
   - Execute `dataset_augmentation.py` to enhance your dataset with transformations.

6. **Modify Annotation Files (Optional)**
   - Run `change_txt.py` or `change_txt2.py` to update or remap class IDs if needed.

7. **Train the Model**
   - Execute `train.py` to start training the YOLOv8 segmentation model. Adjust the configuration file (`cfg/coco8.yaml`) if necessary.

8. **Test the Model**
   - Use `Video_to_predict.py` to perform inference on a video and visualize predictions.

### Notes
- Ensure the paths in each script match your dataset's actual directory structure.
- Review and adjust hyperparameters in `train.py` to optimize training performance.

