import numpy as np
from PIL import Image

def get_camera_matrix(image_width, image_height, focal_length_mm=4.2, sensor_width_mm=5.6, sensor_height_mm=4.2):
    """ 아이폰12 기준 """
    fx = (focal_length_mm / sensor_width_mm) * image_width
    fy = (focal_length_mm / sensor_height_mm) * image_height
    cx = image_width / 2
    cy = image_height / 2

    K = [[fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]]
    print("카메라 intrinsic (K):")
    for row in K:
        print(row)
    return K


def camera_matrix(img_path, zoom=1.):
  img = Image.open(img_path)
  img_width, img_height = img.size

  if zoom == 1.:
    focal_length = 4.2
    sensor_width = 5.6        # iphone12 기준
    sensor_height = 4.2       # iphone12 기준

  elif zoom == 0.5:
    focal_length = 1.54
    sensor_width = 4.0
    sensor_height = 3.0

  cam_matrix = get_camera_matrix(img_width, img_height, focal_length, sensor_width, sensor_height)
  '''
  - scene type
  0 = standard
  1 = landscape
  2 = portrait
  3 = night scne
  '''
  return cam_matrix

# camera_matrix("/content/drive/MyDrive/camera_photos/happy_noodles/frames/IMG_5301.JPG")
# camera_matrix("/content/drive/MyDrive/camera_photos/happy_noodles/frames/IMG_5278.JPG")