# NameMC Profile Art Generator

Create a personalized banner for your NameMC profile using this script, which transforms a single input image into an array of custom Minecraft skins. These skins, when uploaded to your Minecraft profile in sequence, will display a cohesive design on your NameMC profile, akin to a mosaic.

<img src="assets/README_EXAMPLE_IMAGE_DO_NOT_TOUCH.png" alt="Example profile art">

## Requirements

Before running the script, ensure you have the following prerequisites:

- Python 3.6 or later
- Pillow (Python Imaging Library Fork)

The Pillow library (if not found) will attempt to install itsself upon running `main.py`. If Pillow returns an error then please manually install Pillow via the terminal with ```pip3 install --upgrade pillow```.

## Setup

1. Clone or download the repository to your local machine.
2. Navigate to the `assets` directory within the cloned repository.

## Usage Instructions

- Place your chosen input image within the `assets` directory. This image will be dissected into individual skin elements. It must be named `input.png` for the script to recognize it automatically.
- If a file named `input.png` already exists, replace it with your chosen banner image.
- Execute the `main.py` script from the root of the repository:

```bash
python main.py
```

- Upon successful execution, the script will output 26 individual skin files to the `assets/output` directory. Each skin file is named in the sequence `skin_1.png` through `skin_26.png`.
- Additionally, the cropped 8x8 blocks extracted from the input image will be stored in the `assets/output2` directory for reference though you can ignore them.

## Important Notes

- Begin by applying the `skin_1.png` to your Minecraft profile and progress sequentially to `skin_26.png`. Finally, apply your regular skin. This sequence will ensure the intended design is displayed correctly on your NameMC profile.
- Make sure to wait approximately 60 seconds between applying each skin to allow NameMC time to update the changes on your profile. This step is crucial to ensure that your NameMC profile art displays correctly and each skin is registered in the proper order.

## Input Image Specifications

To ensure compatibility with the script, adhere to the following image specifications:

- The image must be exactly 72 pixels in width and 24 pixels in height.
- The script divides the image into a grid of 8x8 pixel blocks, creating a 9x3 grid layout.
- Each block from this grid is utilized to generate an individual skin file that corresponds to a segment of the larger image.

## Output

- The script generates 27 Minecraft skin files, which are laid out to form the NameMC profile art when viewed collectively.
- Each generated skin file is a 64x64 pixel PNG image, with the relevant 8x8 block from the input image layered over the face of the skin.
