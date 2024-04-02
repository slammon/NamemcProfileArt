# NameMCtools
yup

## Profile Art Generator

This script generates Minecraft skin files from a given input image.

### Requirements

- Python 3.6 or higher
- Pillow library

To install the required Python library, run the following command:

```bash
```pip install -r requirements.txt```

Usage
Place your input image and skin template in the src/assets/PAG directory. The input image should be named input.png and the skin template should be named skin_template.png.
Run the ProfileArtGen.py script.
The generated skin files will be saved in the src/assets/PAG/output directory, and the cropped 8x8 blocks from the input image will be saved in the src/assets/PAG/output2 directory.
Input Image Requirements
The input image must be 72 pixels wide and 24 pixels high. The script will divide this image into 8x8 blocks (9 blocks wide by 3 blocks tall), and each block will be used to generate a separate skin file.

