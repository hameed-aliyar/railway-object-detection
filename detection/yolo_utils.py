import cv2
import numpy as np
from config.settings import YOLO_CFG_PATH, YOLO_WEIGHTS_PATH, YOLO_NAMES_PATH

def load_yolo():
    net = cv2.dnn.readNet(YOLO_WEIGHTS_PATH, YOLO_CFG_PATH)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    with open(YOLO_NAMES_PATH, "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]
    return net, classes, output_layers

def detect_objects(img, net, output_layers):
    height, width, _ = img.shape
    blob = cv2.dnn.blobFromImage(img, 0.00392, (224, 224), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    return outs, height, width

def get_box_dimensions(outs, height, width, confidence_threshold=0.5):
    class_ids, confidences, boxes = [], [], []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_threshold:
                center_x, center_y = int(detection[0] * width), int(detection[1] * height)
                w, h = int(detection[2] * width), int(detection[3] * height)
                x, y = int(center_x - w / 2), int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    return class_ids, confidences, boxes
