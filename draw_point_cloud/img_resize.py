import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("path", type="str", default="/content/drive/MyDrive/camera_photos/")
args = parser.parse_args()

def resizing(args.path):
    if not os.path.exists(args.path + "resized/"):
        os.mkdir(args.path + "resized/")
        
    # 원본 이미지 경로와 저장할 경로
    images = os.listdir(args.path)
    for img in images:
        input_path = args.path + img
        output_path = args.path + "resized/" + f'{img[:-4]}_resized.jpg'
        
        img = Image.open(input_path)
        width, height = img.size
        print(f"original width:{width}, height:{height}")

        if width < 2000:
            scale = 0.4       # 40% size
        else:
            scale = 0.3       # 30% size
            
        new_width = int(width * scale)
        new_height = int(height * scale)

        # resizing, LANCZOS: 고화질의 downsampling
        img_resized = img.resize((new_width, new_height), Image.LANCZOS)
        # save with high quality
        img_resized.save(output_path, quality=100, subsampling=0)

        print(f"이미지 저장완료: {output_path}, 가로와 세로:({new_width} {new_height})")