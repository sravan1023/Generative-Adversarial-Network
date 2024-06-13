import os
import shutil
from pathlib import Path
from PIL import Image

RAW_DATA_DIR = Path('C:/Users/Sran/Desktop/GAN1/data/raw/images')  
PROCESSED_DATA_DIR = Path('C:/Users/Sran/Desktop/GAN J/data/processed/train') 

# Parameters
IMAGE_SIZE = (64, 64)

def create_directory_structure():
    if PROCESSED_DATA_DIR.exists():
        shutil.rmtree(PROCESSED_DATA_DIR)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

def get_image_files(directory):
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff']
    image_files = []
    for ext in image_extensions:
        image_files.extend(directory.rglob(ext))
    return image_files

def process_images():
    genres = [d for d in RAW_DATA_DIR.iterdir() if d.is_dir()]
    
    for genre_dir in genres:
        images = get_image_files(genre_dir)
        
        print(f"Processing genre: {genre_dir.name}, Number of images: {len(images)}")

        process_and_save_images(images, PROCESSED_DATA_DIR / genre_dir.name)

def process_and_save_images(images, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for img_path in images:
        try:
            with Image.open(img_path) as img:
                img = img.convert("RGB") 
                img = img.resize(IMAGE_SIZE, Image.LANCZOS)
                img.save(output_dir / img_path.name)
                print(f"Processed and saved: {output_dir / img_path.name}")
        except Exception as e:
            print(f"Error processing {img_path}: {e}")

if __name__ == "__main__":
    RAW_DATA_DIR = RAW_DATA_DIR.resolve()
    PROCESSED_DATA_DIR = PROCESSED_DATA_DIR.resolve()
    
    create_directory_structure()
    
    process_images()
    print("Data processing complete.")