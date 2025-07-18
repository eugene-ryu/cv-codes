import argparse
from PIL import Image
from PIL.ExifTags import TAGS

parser = argparse.ArgumentParser()
parser.add_argument("imgpath", type="str", default="/content/drive/MyDrive/camera_photos/frames/0001.jpg")
args = parser.parse_args()


def print_exif(args.imgpath):
    image = Image.open(args.imgpath)
    exif_data = image._getexif()
    ret_dict = {}
    if exif_data is not None:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            ret_dict[tag] = value
    else:
        print("EXIF 데이터 없음")
    return ret_dict

# img_path = "/content/drive/MyDrive/camera_photos/frames/IMG_5278.JPG"
# print_exif(img_path)