from PIL import Image
from tkinter import filedialog
import tkinter as tk
import numpy as np
from settings import *

class ImageConverter:
    def __init__(self, app):
        self.app = app
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

    def open_image_dialog(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", ".png;.jpg;*.jpeg")])

        if not file_path:
            print("No file selected. Exiting.")
            exit()

        return file_path

    def find_nearest_color(self, rgb, colors):
        min_distance = float('inf')
        nearest_color = None

        for color in colors:
            distance = sum((a - b) ** 2 for a, b in zip(rgb, color)) ** 0.5
            if distance < min_distance:
                min_distance = distance
                nearest_color = color

        return nearest_color

    def convert_to_single_color_grid(self, image, colors, resolution_width, resolution_height):
        width, height = image.size
        new_image = Image.new('RGB', (width, height))

        grid_size_x = width // resolution_width
        grid_size_y = height // resolution_height

        processed = []
        count = []
        
        for j in range(resolution_height):
            processed_pixels = []
            # c = 0
            for i in range(resolution_width):
                # Lấy màu trung bình trong từng ô lưới
                grid_color = self.find_average_color(image, i * grid_size_x, j * grid_size_y, grid_size_x, grid_size_y)
                
                # Tìm màu gần nhất từ danh sách màu mục tiêu
                new_color = self.find_nearest_color(grid_color, colors)

                # Thêm màu vào ma trận
                if new_color[0] == 0 and new_color[1] == 0:
                    processed_pixels.append("B")
                elif new_color[0] == 0 and new_color[2] == 0:
                    processed_pixels.append("G")
                elif new_color[1] == 0 and new_color[2] == 0:
                    processed_pixels.append("R")
                # c = c + 1
                # # Gán màu mới cho từng pixel trong ô lưới
                # for x in range(i * grid_size_x, min((i + 1) * grid_size_x, width)):
                #     for y in range(j * grid_size_y, min((j + 1) * grid_size_y, height)):
                #         new_image.putpixel((x, y), new_color)
                        
                # # Thêm đường viền đen và lưới
                # for x in range(i * grid_size_x, min((i + 1) * grid_size_x, width)):
                #     new_image.putpixel((x, j * grid_size_y), (0, 0, 0))  # Vertical grid line
                # for y in range(j * grid_size_y, min((j + 1) * grid_size_y, height)):
                #     new_image.putpixel((i * grid_size_x, y), (0, 0, 0))  # Horizontal grid line
            processed.append(processed_pixels)
            # count.append(c)
        return new_image, processed, count

    def find_average_color(self, image, start_x, start_y, grid_size_x, grid_size_y):
        total_r, total_g, total_b = 0, 0, 0
        count = 0

        for x in range(start_x, min(start_x + grid_size_x, image.width)):
            for y in range(start_y, min(start_y + grid_size_y, image.height)):
                pixel_color = image.getpixel((x, y))
                total_r += pixel_color[0]
                total_g += pixel_color[1]
                total_b += pixel_color[2]
                count += 1

        if count == 0:
            return (0, 0, 0)

        average_r = total_r // count
        average_g = total_g // count
        average_b = total_b // count

        return (average_r, average_g, average_b)

    def process_image(self):
        file_path = self.open_image_dialog()
        image = Image.open(file_path)

        # Define three target colors (RGB)
        target_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

        # Resolution of the grid (number of pixels per cell)
        grid_resolution_width = 104
        grid_resolution_height = 60

        # Sử dụng hàm convert_to_single_color_grid thay vì convert_to_3_colors_with_grid
        result_image, matrix, c = self.convert_to_single_color_grid(image, target_colors, grid_resolution_width, grid_resolution_height)
        # result_image.save("output_single_color_grid.png")
        # print(matrix)
        # #print(c)
        # print(len(matrix), len(matrix[0]))
        return matrix
