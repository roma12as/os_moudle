import os
import shutil

# الامتدادات المختلفة
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]
video_extensions = [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"]
pdf_extensions = [".pdf"]

# إنشاء المجلدات لو مش موجودة
os.makedirs("images", exist_ok=True)
os.makedirs("videos", exist_ok=True)
os.makedirs("pdfs", exist_ok=True)

# نلف على كل الملفات في المجلد الحالي
for file in os.listdir():
    if os.path.isfile(file):  # نتأكد إنه ملف مش فولدر
        ext = os.path.splitext(file)[1].lower()

        if ext in image_extensions:
            print(f"{file} is an image file.")
            shutil.move(file, os.path.join("images", file))
        elif ext in video_extensions:
            print(f"{file} is a video file.")
            shutil.move(file, os.path.join("videos", file))
        elif ext in pdf_extensions:
            print(f"{file} is a PDF file.")
            shutil.move(file, os.path.join("pdfs", file))
        else:
            print(f"{file} is not a known file type.")
