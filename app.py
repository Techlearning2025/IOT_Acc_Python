import os

# Folder containing images
folder_path = r"E:\UTC project\utc\cctv\CCTV_Project\newQImages\test"

# File extensions to rename
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

# Get list of image files
images = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]

# Sort and rename
for i, filename in enumerate(sorted(images), start=1):
    ext = os.path.splitext(filename)[1]  # Get file extension
    new_name = f"testimage_{i:04d}{ext}"     # e.g., image_0001.jpg
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)

print(f"✅ Renamed {len(images)} images in folder.")
