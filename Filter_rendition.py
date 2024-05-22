# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:43:51 2024

@author: Morteza
"""

import cv2
import numpy as np

# Define the Macbeth ColorChecker colors (24 patches)
color_patches = [
    [115, 82, 68], [194, 150, 130], [98, 122, 157], [87, 108, 67],
    [133, 128, 177], [103, 189, 170], [214, 126, 44], [80, 91, 166],
    [193, 90, 99], [94, 60, 108], [157, 188, 64], [224, 163, 46],
    [56, 61, 150], [70, 148, 73], [175, 54, 60], [231, 199, 31],
    [187, 86, 149], [8, 133, 161], [243, 243, 242], [200, 200, 200],
    [160, 160, 160], [122, 122, 121], [85, 85, 85], [52, 52, 52]
]

# Create the color checker image
def create_color_checker(screen_width, screen_height):
    checker = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
    patch_size = screen_height // 4
    for i in range(4):
        for j in range(6):
            color = color_patches[i * 6 + j]
            cv2.rectangle(checker, (j * patch_size, i * patch_size), 
                          ((j + 1) * patch_size, (i + 1) * patch_size), 
                          color, -1)
    return checker

# Apply color filter to the image
def apply_filter(image, filter_color):
    b, g, r = cv2.split(image)
    if filter_color == 'blue':
        filtered = cv2.merge([b, np.zeros_like(g), np.zeros_like(r)])
    elif filter_color == 'green':
        filtered = cv2.merge([np.zeros_like(b), g, np.zeros_like(r)])
    elif filter_color == 'red':
        filtered = cv2.merge([np.zeros_like(b), np.zeros_like(g), r])
    elif filter_color == 'cyan':
        filtered = cv2.merge([b, g, np.zeros_like(r)])
    elif filter_color == 'magenta':
        filtered = cv2.merge([b, np.zeros_like(g), r])
    elif filter_color == 'yellow':
        filtered = cv2.merge([np.zeros_like(b), g, r])
    else: # no filter
        filtered = image
    return filtered

# Display image with filter name
def display_image_with_text(image, filter_color):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thickness = 8
    font_color_black = (0, 0, 0)
    font_color_white = (255, 255, 255)
    line_type = 5
    
    # Position for filter name
    position_name = (20, 100)
    
    # Draw black border
    cv2.putText(image, f'Filter: {filter_color}', position_name, font, font_scale, font_color_black, font_thickness, cv2.LINE_AA)
    # Draw white interior
    cv2.putText(image, f'Filter: {filter_color}', position_name, font, font_scale, font_color_white, font_thickness - 2, cv2.LINE_AA)

    cv2.imshow('Macbeth ColorChecker', image)
    cv2.waitKey(7000)  # Display for 7 seconds


# Main function
def main():
    # Get screen resolution (adjust these values to match your screen)
    screen_width = 1920
    screen_height = 1080
    
    color_checker = create_color_checker(screen_width, screen_height)
    filters = ['no filter', 'blue', 'yellow', 'green', 'red', 'cyan', 'magenta']
    
    for filter_color in filters:
        filtered_image = apply_filter(color_checker.copy(), filter_color)
        display_image_with_text(filtered_image, filter_color)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
