import os
from PIL import Image
import shutil

source_dir = 'assests/images'
cache_dir = os.path.join(source_dir, 'cache')

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

MAX_SIZE = (1200, 1200)

def compress_image(src_path, dest_path):
    try:
        with Image.open(src_path) as img:
            # Convert to RGB if necessary (e.g. RGBA to RGB for JPEG)
            if img.mode in ('RGBA', 'P') and dest_path.lower().endswith(('.jpg', '.jpeg')):
                img = img.convert('RGB')
            
            # Resize preserving aspect ratio
            img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
            
            # Save with optimized settings
            if dest_path.lower().endswith(('.jpg', '.jpeg')):
                img.save(dest_path, 'JPEG', quality=80, optimize=True)
            elif dest_path.lower().endswith('.png'):
                img.save(dest_path, 'PNG', optimize=True)
            else:
                img.save(dest_path)
        print(f"Compressed: {src_path} -> {dest_path}")
    except Exception as e:
        print(f"Failed to compress {src_path}: {e}")
        # fallback to copy
        shutil.copy2(src_path, dest_path)

for root, dirs, files in os.walk(source_dir):
    # skip cache dir itself
    if cache_dir in root:
        continue
    
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            src_path = os.path.join(root, file)
            # determine relative path to recreate structure
            rel_path = os.path.relpath(src_path, source_dir)
            dest_path = os.path.join(cache_dir, rel_path)
            
            dest_dir = os.path.dirname(dest_path)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
                
            compress_image(src_path, dest_path)
