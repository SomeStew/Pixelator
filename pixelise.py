# -*- coding: utf-8 -*-
"""
Created on Mon Dec  23 14:08:13 2024

@author: Eleve
"""

from PIL import Image, ImageDraw
import random

def process_image(input_image_path, output_image_path, num_pixels):
    # Charger l'image
    img = Image.open(input_image_path)
    width, height = img.size

    # Sélectionner des pixels aléatoires
    selected_pixels = []
    for _ in range(num_pixels):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        hex_color = '#{:02x}{:02x}{:02x}'.format(*img.getpixel((x, y))[:3])
        selected_pixels.append((x, y, hex_color))

    # Blanchir complètement l'image
    white_img = Image.new('RGB', (width, height), "white")
    draw = ImageDraw.Draw(white_img)

    # Créer des quadrilatères centrés sur les pixels sélectionnés
    rect_size = int(min(width, height) / 100)  # Taille des rectangles
    for x, y, color in selected_pixels:
        top_left = (x - rect_size // 2, y - rect_size // 2)
        bottom_right = (x + rect_size // 2, y + rect_size // 2)
        draw.rectangle([top_left, bottom_right], fill=color)

    # Sauvegarder l'image résultante
    white_img.save(output_image_path)
    print(f"Image modifiée sauvegardée sous : {output_image_path}")

# Exemple d'utilisation
# Fournir le chemin d'une image en entrée et en sortie, ainsi que le nombre de pixels
input_image_path = "votre_image_entree.jpg"
output_image_path = "votre_image_sortie.jpg"
num_pixels = 50  # Nombre de pixels aléatoires à sélectionner

process_image(input_image_path, output_image_path, num_pixels)
