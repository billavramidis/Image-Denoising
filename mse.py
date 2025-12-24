from PIL import Image
import numpy as np
from pathlib import Path

denoised_directory_path = Path("outputs/denoised/")
denoised_image_paths = [
    f
    for f in denoised_directory_path.iterdir()
    if f.suffix in [".jpg", ".png", ".webp"]
]

clean_directory_path = Path("inputs/clean/")
clean_image_path = [
    f for f in clean_directory_path.iterdir() if f.suffix in [".jpg", ".png", ".webp"]
]
clean_image = clean_image_path[0]


for denoised_image in denoised_image_paths:
    with Image.open(denoised_image) as img1, Image.open(clean_image) as img2:
        if not img1.size == img2.size:
            raise ValueError(f"Image Dimensions Do Not Match")

        denoised_pixels = np.array(img1.convert("RGB")).astype(np.float64)
        clean_pixels = np.array(img2.convert("RGB")).astype(np.float64)

        mse = np.mean((clean_pixels - denoised_pixels) ** 2)
        print(f"MSE: {mse}")
