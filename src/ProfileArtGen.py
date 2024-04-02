from PIL import Image
import os

input_image = Image.open('src/assets/PAG/input.png')
skin_template = Image.open('src/assets/PAG/skin_template.png')

if input_image.size != (72, 24):
    raise ValueError('Input image must be 72x24 pixels')

os.makedirs('src/assets/PAG/output', exist_ok=True)
os.makedirs('src/assets/PAG/output2', exist_ok=True)

counter = 0

for i in range(3):
    for j in range(9):
        block = input_image.crop((j*8, i*8, j*8+8, i*8+8))
        
        block.save(f'src/assets/PAG/output2/block_{counter}.png')
        
        skin = skin_template.copy()
        skin.paste(block, (8, 8))
        
        skin.save(f'src/assets/PAG/output/skin_{counter}.png')
        
        counter += 1