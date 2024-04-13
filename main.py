import os
import subprocess
import time

try:
    from PIL import Image
except ImportError:
    print("Pillow library not found. Installing now...")
    try:
        subprocess.check_call(["python", "-m", "pip", "install", "pillow"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Pillow: {e}")
        exit(1)

input_image = Image.open('assets/input.png')
skin_template = Image.open('assets/skin_template.png')

if input_image.size != (72, 24):
    raise ValueError('Input image must be 72x24 pixels')

os.makedirs('assets/output', exist_ok=True)
os.makedirs('assets/output2', exist_ok=True)

counter = 0

start_time = time.time()

for i in range(3):
    for j in range(9):
        block = input_image.crop((j*8, i*8, j*8+8, i*8+8))
        
        block.save(f'assets/output2/block_{counter}.png')
        
        skin = skin_template.copy()
        skin.paste(block, (8, 8))
        
        skin.save(f'assets/output/skin_{counter}.png')
        
        counter += 1

end_time = time.time()

elapsed_time = (end_time - start_time) * 1000

print(f'Done! {elapsed_time:.2f} ms')
