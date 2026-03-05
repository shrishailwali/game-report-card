def generate_analytics(detections):
    total_frames = len(detections)
    enemy_frames = 0

    for frame in detections:
        for obj in frame:
            if obj["class"] == 0:  # Example class ID
                enemy_frames += 1

    accuracy_score = round((enemy_frames / total_frames) * 100, 2)

    return {
        "total_frames": total_frames,
        "enemy_presence_percent": accuracy_score,
        "mistakes": analyze_mistakes(enemy_frames, total_frames),
        "strengths": analyze_strengths(enemy_frames)
    }


def analyze_mistakes(enemy_frames, total_frames):
    if enemy_frames < total_frames * 0.2:
        return ["Low engagement with enemies"]

    return ["Good engagement"]


def analyze_strengths(enemy_frames):
    if enemy_frames > 10:
        return ["High map awareness"]

    return ["Needs improvement in awareness"]
