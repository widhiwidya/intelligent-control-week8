from ultralytics import YOLO
import cv2

# Load model sekali saja
model = YOLO("best.pt")  # Ganti dengan model custom kalau ada

def detect_objects(frame, conf=0.3):
    results = model.predict(source=frame, conf=conf, verbose=False)
    annotated_frame = results[0].plot()
    return annotated_frame, results[0].boxes.data  # Bisa dipakai untuk logika lebih lanjut
