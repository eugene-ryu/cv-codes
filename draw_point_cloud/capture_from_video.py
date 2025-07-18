## 동영상 파일에서 이미지 캡쳐
import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video", type="str", default="/content/drive/MyDrive/camera_photos/IMG_5277.MOV")
parser.add_argument("outpath", type="str", default="/content/drive/MyDrive/camera_photos/frames/")
args = parser.parse_args()

def capture_frames(args.video, args.outpath, interval_sec=0.5):
    if not os.path.exists(args.outpath):
        os.makedirs(args.outpath)
    cap = cv2.VideoCapture(args.video)
    if not cap.isOpened():
        print("파일 경로 재확인 필요.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    print(f"Video FPS: {fps}, Total Frames: {total_frames}, Duration: {duration:.2f}s")

    count = 0
    sec = 0.0
    while sec < duration:
        frame_id = int(sec * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
        ret, frame = cap.read()
        if not ret:
            break
        out_path = os.path.join(args.outpath, f"5277_{count:04d}.jpg")
        cv2.imwrite(out_path, frame)
        print(f"Saved {out_path}")
        count += 1
        sec += interval_sec

    cap.release()
    print("Done.")

# video_file = "/content/drive/MyDrive/camera_photos/happy_noodles/IMG_5277.MOV"  # 동영상 파일 경로
# output_folder = "/content/drive/MyDrive/camera_photos/happy_noodles/frames/"  # 저장 폴더
# capture_frames(video_file, output_folder, interval_sec=0.5)