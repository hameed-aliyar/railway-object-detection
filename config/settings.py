import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TELEGRAM_BOT_TOKEN = "7889811135:AAGiJbLpbtGhM1w1kKWEhTkmZbW0bUeylUo"
TELEGRAM_CHAT_IDS = ["7314060816"]

DETECTION_LOG_FILE = os.path.join(BASE_DIR, "detection_log.txt")
DETECTED_OBJECTS_DIR = os.path.join(BASE_DIR, "detected_objects")
OUTPUT_VIDEO_DIR = os.path.join(BASE_DIR, "output_videos")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

YOLO_CFG_PATH = os.path.join(ASSETS_DIR, "yolov4-tiny.cfg")
YOLO_WEIGHTS_PATH = os.path.join(ASSETS_DIR, "yolov4-tiny.weights")
YOLO_NAMES_PATH = os.path.join(ASSETS_DIR, "coco.names")

# Create folders if not exist
os.makedirs(DETECTED_OBJECTS_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEO_DIR, exist_ok=True)
