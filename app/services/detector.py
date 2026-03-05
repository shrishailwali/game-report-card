from ultralytics import YOLO

# Load pretrained model (later you train custom)
model = YOLO("yolov8n.pt")

def detect_objects(frames):
    results_data = []

    for frame in frames:
        results = model(frame)

        frame_data = []
        for r in results:
            for box in r.boxes:
                frame_data.append({
                    "class": int(box.cls[0]),
                    "confidence": float(box.conf[0])
                })

        results_data.append(frame_data)

    return results_data
