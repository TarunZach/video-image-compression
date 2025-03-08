from PIL import Image
import os


def compress_image(image_path, quality=50):
    output_path = os.path.join("output", os.path.basename(image_path))

    try:
        img = Image.open(image_path)
        img.save(output_path, optimize=True, quality=quality)
        return output_path
    except Exception as e:
        print(f"Error compressing image: {e}")
        return None
