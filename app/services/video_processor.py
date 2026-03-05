import cv2
from app.services.detector import detect_objects
from app.services.analytics import generate_analytics
from app.services.llm_service import generate_report

def extract_frames(video_path, fps=5):
    cap = cv2.VideoCapture(video_path)
    frames = []

    video_fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(video_fps / fps)

    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % interval == 0:
            frames.append(frame)

        count += 1

    cap.release()
    return frames


def process_video(video_path):
    frames = extract_frames(video_path)
    detections = detect_objects(frames)
    analytics = generate_analytics(detections)
    report = generate_report(analytics)

    return {
        "analytics": analytics,
        "ai_report": report
    }
