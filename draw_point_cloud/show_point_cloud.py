# 결과물인 .bin 파일들 보여주는거, 로컬에서 해야함
# !pip install viser
import numpy as np
from pathlib import Path
import viser
from viser.extras.colmap import (
    read_cameras_binary,
    read_images_binary,
    read_points3d_binary,
)

cameras_bin = "C:/Users/soohyun/Desktop/3d_vision/sparse/cameras.bin"
images_bin = "C:/Users/soohyun/Desktop/3d_vision/sparse/images.bin"
points3D_bin = "C:/Users/soohyun/Desktop/3d_vision/sparse/points3D.bin"
# colmap_path = Path("/path/to/colmap_model")  # cameras.bin, images.bin, points3D.bin이 있는 폴더
server = viser.ViserServer()

# COLMAP 데이터 읽기
cameras = read_cameras_binary(cameras_bin)
images = read_images_binary(images_bin)
points3d = read_points3d_binary(points3D_bin)

# 포인트 클라우드 준비
points = np.array([points3d[p_id].xyz for p_id in points3d])
colors = np.array([points3d[p_id].rgb for p_id in points3d])

# 3D 포인트 클라우드 시각화
server.scene.add_point_cloud(
    name="/colmap/pcd",
    points=points,
    colors=colors / 255.0,  # RGB 값 정규화
    point_size=0.02,
)

# 카메라 위치 시각화 (프레임)
for img in images.values():
    server.scene.add_frame(
        f"/colmap/frame_{img.id}",
        wxyz=img.qvec,  # 쿼터니언
        position=img.tvec,
        axes_length=0.1,
        axes_radius=0.005,
    )

# 서버 실행 (웹 브라우저에서 localhost:8080 등으로 접속)
# run() 메서드 대신 서버가 자동으로 실행됩니다
print("Viser 서버가 시작되었습니다. 웹 브라우저에서 localhost:8080으로 접속하세요.")
print("서버를 중지하려면 Ctrl+C를 누르세요.")

# 서버를 계속 실행 상태로 유지
try:
    import time
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("서버를 종료합니다.")