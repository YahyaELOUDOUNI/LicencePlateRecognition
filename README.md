# License Plate Recognition System - YOLOv8

## Project Description

This project, developed as part of the PAS (Academic and Scientific Project) module during our Data and Artificial Intelligence program at ESILV, focuses on automatic license plate recognition from images or videos (video input in our case).

It leverages computer vision models, specifically YOLOv8 and OCR, to detect and read license plates from videos.

## Features

- **Vehicle Detection:** Utilizes a pre-trained YOLOv8 model to detect vehicles in a video.  
- **License Plate Detection:** A custom-trained model for locating license plates.  
- **Character Recognition:** Extracts license plate numbers using an OCR module (EasyOCR).  
- **Missing Data Interpolation:** Handles missing values through the `add_missing_data.py` module for smoother results.  
- **Result Visualization:** Displays detections and extracted numbers with smooth video output.  
- **Streamlit Application:** A user-friendly interface for testing videos through drag-and-drop and viewing processed videos.  

## Technologies
- Python  
- Ultralytics YOLOv8  
- OpenCV  
- EasyOCR  
- Streamlit  

## Data 

- The test video used for this project can be downloaded [here](https://drive.google.com/file/d/1JbwLyqpFCXmftaJY1oap8Sa6KfjoWJta/view).  
- A pre-trained YOLOv8n model for vehicle detection is available [here](https://drive.google.com/file/d/1Zmf5ynaTFhmln2z7Qvv-tgjkWQYQ9Zdw/view).  
- A custom license plate detector was trained using the dataset available [here](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4).  

## Dependencies

The project relies on the following modules:

- Python 3.10: Version used for development.  
- Ultralytics YOLOv8: For object detection.  
- OpenCV: For image processing and result visualization.  
- EasyOCR: For character recognition on license plates.  
- SORT: A tracking algorithm for managing plate tracking in videos (requires cloning the repository below).  

### To install and use the SORT module, clone the following repository (Mandatory):

```bash
git clone https://github.com/abewley/sort
```

## Project Structure

```
├── sort # Cloned repository for tracking license plates in videos
│  
├── add_missing_data.py # Interpolates missing values to improve results.
├── app.py # Streamlit application for an interactive user interface.
├── main.py # Generates a test.csv file containing detected data.
├── util.py # Utility functions supporting other scripts.
├── visualize.py # Creates a video displaying detection and recognition results.
├── license_plate_detector.pt : Pre-trained YOLO model file for detecting license plates.
├── yolov8n.pt : Pre-trained YOLOv8 model file for detecting other objects, like vehicles.
│   
├── README.md                   
```

## Setting up a Virtual Environment (Optional)

#### Create a virtual environment:

```bash
python -m venv env
```

#### Activate the environment:

```bash
.\env\Scripts\activate
```

## Install Dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

#### 1. Streamlit Application  

Run the Streamlit app to test your videos through an interactive user interface:

```bash
streamlit run app.py
```

##### Features:

- Drag-and-drop for uploading videos.  
- Automatic video analysis and processing.  
- Displays the processed video directly in the app.  
- Option to download the resulting video.  

#### 2. Initial Detection and Extraction  

Run the `main.py` script on an input video to generate a `test.csv` file with detected data:

```bash
python main.py
```

#### 3. Interpolation of Missing Data  

Execute the `add_missing_data.py` script to interpolate missing values and enhance results:

```bash
python add_missing_data.py
```

#### 4. Final Visualization  

Run the `visualize.py` script to generate a video with smooth and accurate license plate detection and recognition results:

```bash
python visualize.py
```

The resulting video will be saved in the directory as `out.mp4`.  

---  

Feel free to suggest further refinements! 🚀