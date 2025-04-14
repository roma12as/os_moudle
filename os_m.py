import os
import shutil
import psutil
import time

file_name = "ram_log.txt"  # اسم الملف اللي هنسجل فيه

def get_usage():
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]
    video_extensions = [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"]
    pdf_extensions = [".pdf"]

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

def get_memory_usage():
    cpu_usage = psutil.cpu_percent(interval=1)

    # الحصول على نسبة استخدام الرام
    ram_usage = psutil.virtual_memory().percent

    # الحصول على استخدام الهارد
    disk_usage = psutil.disk_usage('/').percent
    net = psutil.users()
    return f"CPU Usage: {cpu_usage}%, RAM Usage: {ram_usage}%, Disk Usage: {disk_usage}%, Users: {net}"

def back_up():
    shutil.copytree("images", "backup/images", dirs_exist_ok=True)
    shutil.copytree("videos", "backup/videos", dirs_exist_ok=True)
    shutil.copytree("pdfs", "backup/pdfs", dirs_exist_ok=True)
    print("Backup completed successfully.")

back_up()

while True:
    memory_info = get_memory_usage()
    print(memory_info)
    
    with open(file_name, "w") as file:
        file.write(f"{memory_info}\n")
    
    time.sleep(5)  
