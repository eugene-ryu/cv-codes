import sqlite3

db_path = "/content/drive/MyDrive/camera_photos/outputs/database.db"  # 파일 경로 지정
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

cursor.execute("SELECT * FROM cameras;")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM images;")
for row in cursor.fetchall():
    print(row)

conn.close()