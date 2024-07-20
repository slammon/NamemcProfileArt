import os
import subprocess
import time

try:
    from PIL import Image
except ImportError:
    print("[Err]: Pillow library not found. Installing now...")
    try:
        subprocess.check_call(["python", "-m", "pip", "install", "pillow"])
        from PIL import Image
    except subprocess.CalledProcessError as e:
        print(f"[Err]: Failed to install Pillow: {e}")
        exit(1)

input_image = Image.open(input('[Input]: Path to input image: '))
skin_template = Image.open('assets/skin_template.png')

if input_image.size != (72, 24):
    print('[Err]: Input image must be 72x24 pixels\n[Log]: Attempting to resize image')
    try:
        input_image = input_image.resize((72, 24))
        print('[Log]: Image resized successfully')
    except Exception as e:
        print(f'[Err]: Failed to resize image: {e}')
        exit(1)

os.makedirs('assets/output', exist_ok=True)

counter = 26

start_time = time.time()

for i in range(3):
    for j in range(9):
        if i == 0 and j == 0:
            continue
        block = input_image.crop((j*8, i*8, j*8+8, i*8+8))

        skin = skin_template.copy()
        skin.paste(block, (8, 8))
        
        skin.save(f'assets/output/skin_{counter}.png')
        
        counter -= 1

end_time = time.time()

elapsed_time = (end_time - start_time) * 1000

print(f'Done! {elapsed_time:.2f} ms')
