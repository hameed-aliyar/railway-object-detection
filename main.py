import cv2
import threading
import asyncio
from detection.yolo_utils import load_yolo, detect_objects, get_box_dimensions
from detection.detection_logic import draw_labels
from ui.file_selector import get_video_path

thread_loop = asyncio.new_event_loop()

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

threading.Thread(target=start_loop, args=(thread_loop,), daemon=True).start()

def simulate_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Video open error")
        return

    net, classes, output_layers = load_yolo()
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps) if fps > 0 else 30

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        outs, height, width = detect_objects(frame, net, output_layers)
        class_ids, confidences, boxes = get_box_dimensions(outs, height, width)
        frame = draw_labels(boxes, confidences, class_ids, classes, frame, thread_loop)

        cv2.imshow("Detection", frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    path = get_video_path()
    if path:
        simulate_video(path)
    else:
        print("No video selected.")
