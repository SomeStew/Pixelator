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
    for x, y, color in selected_pixels:
        # Generate larger random dimensions for the rectangle
        rect_width = random.randint(int(min(width, height) / 30), int(min(width, height) / 5))
        rect_height = random.randint(int(min(width, height) / 30), int(min(width, height) / 5))
        top_left = (x - rect_width // 2, y - rect_height // 2)
        bottom_right = (x + rect_width // 2, y + rect_height // 2)
        
        # Border color
        rgb = Image.new("RGB", (1, 1), color).getpixel((0, 0))
        darker_rgb = tuple(int(c * 0.7) for c in rgb)
        darker_color = '#{:02x}{:02x}{:02x}'.format(*darker_rgb)
        
        # Draw the rectangle with the border
        draw.rectangle([top_left, bottom_right], outline=darker_color, fill=darker_color)

        # Filler
        inset = 2  # Border size
        inner_top_left = (top_left[0] + inset, top_left[1] + inset)
        inner_bottom_right = (bottom_right[0] - inset, bottom_right[1] - inset)
        draw.rectangle([inner_top_left, inner_bottom_right], fill=color)

    # Save the resulting image
    white_img.save(output_image_path)
    print(f"Modified image saved at: {output_image_path}")