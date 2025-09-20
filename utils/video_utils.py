import cv2

# read the frames of the video
def read_video(video_path):
    capture = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        frames.append(frame)
    capture.release()
    return frames


def save_video(output_video, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = 24
    height, width, _ = output_video[0].shape
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    for frame in output_video:
        out.write(frame)
    out.release()