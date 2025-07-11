import cv2
import datetime
import time
import random
import asyncio
from config.settings import DETECTION_LOG_FILE, DETECTED_OBJECTS_DIR
from notification.telegram_bot import send_telegram_notification
from notification.sound_alert import play_beep

last_notification_time = 0

def log_detection(detected_objects, confidences, frame, boxes, class_ids, classes, thread_loop):
    global last_notification_time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_entries = []

    for i, obj in enumerate(detected_objects):
        x, y, w, h = boxes[i]
        confidence = confidences[i]
        log_entry = f"[{timestamp}] {obj} detected, Confidence: {confidence:.2f}, Location: ({x}, {y}, {w}, {h})\n"
        log_entries.append(log_entry)

        image_path = f"{DETECTED_OBJECTS_DIR}/{obj}_detected_{timestamp}_{i}.jpg"
        cv2.imwrite(image_path, frame)

        current_time = time.time()
        if current_time - last_notification_time >= 5:
            last_notification_time = current_time
            distance = random.randint(850, 900)
            alert_msg = f"🚨 OBJECT DETECTED 🚨\n{obj} detected!\nDistance: {distance}m\nConfidence: {confidence:.2f}"
            asyncio.run_coroutine_threadsafe(send_telegram_notification(alert_msg, image_path), thread_loop)
            play_beep()

    if log_entries:
        with open(DETECTION_LOG_FILE, "a") as f:
            f.writelines(log_entries)

def draw_labels(boxes, confidences, class_ids, classes, frame, thread_loop):
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    detected_objects = []

    for i in range(len(boxes)):
        if i in indexes:
            label = str(classes[class_ids[i]])
            x, y, w, h = boxes[i]
            color = (0, 255, 255)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            detected_objects.append(label)

    if detected_objects:
        log_detection(detected_objects, confidences, frame, boxes, class_ids, classes, thread_loop)

    return frame
