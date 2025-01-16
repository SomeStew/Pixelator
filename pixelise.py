# -*- coding: utf-8 -*-
"""
Created on Mon Dec  23 14:08:13 2024

@author: Eleve
"""

from PIL import Image, ImageDraw
import random

def process_image(input_image_path, output_image_path, num_pixels):
    # Load the image
    img = Image.open(input_image_path)
    width, height = img.size

    # Select random pixels
    selected_pixels = []
    for _ in range(num_pixels):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        hex_color = '#{:02x}{:02x}{:02x}'.format(*img.getpixel((x, y))[:3])
        selected_pixels.append((x, y, hex_color))

    # Create a completely white image
    white_img = Image.new('RGB', (width, height), "white")
    draw = ImageDraw.Draw(white_img)

    # Create quadrilaterals centered on the selected pixels
    rect_size = int(min(width, height) / 10)  # Size of rectangles
    for x, y, color in selected_pixels:
        # Generate a random size for the rectangle, proportional to the image size
        rect_width = random.randint(int(min(width, height) / 50), int(min(width, height) / 10))
        rect_height = random.randint(int(min(width, height) / 50), int(min(width, height) / 10))
        top_left = (x - rect_width // 2, y - rect_height // 2)
        bottom_right = (x + rect_width // 2, y + rect_height // 2)
        draw.rectangle([top_left, bottom_right], fill=color)

    # Save the resulting image
    white_img.save(output_image_path)
    print(f"Modified image saved at: {output_image_path}")