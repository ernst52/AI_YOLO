import os

folder = r"D:\1Software\Singing_Uncle\AI_YOLO_ASSET\ina2"

files = sorted(os.listdir(folder))
for i, f in enumerate(files, 801):
    ext = os.path.splitext(f)[1]
    os.rename(os.path.join(folder, f), os.path.join(folder, f"{i:03d}{ext}"))