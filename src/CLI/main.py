import os
import sys
import time
from PIL import Image


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)


def get_executable_path():
    return os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)

try:
    input_image_path = input("[Input]: Path to input image: ")
    input_image = Image.open(input_image_path)
    skin_template = Image.open(resource_path("assets/skin_template.png"))
except Exception as e:
    print(f"[Error]: Failed to load image: {e}")
    exit(1)

if input_image.size != (72, 24):
    print("[Log]: Input image must be 72x24 pixels. Resizing...")
    try:
        input_image = input_image.resize((72, 24))
        print("[Log]: Image resized successfully.")
    except Exception as e:
        print(f"[Error]: Failed to resize image: {e}")
        exit(1)

base_output_dir = get_executable_path()
output_dir = os.path.join(base_output_dir, "output")
#output2_dir = os.path.join(base_output_dir, "output2")
os.makedirs(output_dir, exist_ok=True)
#os.makedirs(output2_dir, exist_ok=True)

#resized_image_path = os.path.join(output2_dir, "resized_image.png")
#input_image.save(resized_image_path)
#print(f"[Log]: Resized image saved to {resized_image_path}")

counter = 26
start_time = time.time()

for i in range(3):
    for j in range(9):
        if i == 0 and j == 0:
            continue
        block = input_image.crop((j * 8, i * 8, j * 8 + 8, i * 8 + 8))
        
        #block_path = os.path.join(output2_dir, f"block_{i}_{j}.png")
        #block.save(block_path)
        
        skin = skin_template.copy()
        skin.paste(block, (8, 8))
        skin.save(os.path.join(output_dir, f"skin_{counter}.png"))
        counter -= 1

elapsed_time = (time.time() - start_time) * 1000
print(f"[Done]: Process completed in {elapsed_time:.2f} ms.")
