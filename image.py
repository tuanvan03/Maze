#First Idea

from PIL import Image
from tkinter import filedialog
import tkinter as tk

def find_nearest_color(rgb, colors):
    min_distance = float('inf')
    nearest_color = None

    for color in colors:
        distance = sum((a - b) ** 2 for a, b in zip(rgb, color)) ** 0.5
        if distance < min_distance:
            min_distance = distance
            nearest_color = color

    return nearest_color

def convert_to_3_colors_with_grid(image, colors, resolution_with,resolution_height):
    width, height = image.size[0] ,image.size[1]
    new_image = Image.new('RGB', (width, height))

    # Tính số lượng ô lưới trên chiều ngang và chiều dọc
    grid_size_x = width // resolution_with               #Lưới dọc
    grid_size_y = height // resolution_height      #Lưới ngang

    for i in range(width):
        for j in range(height):
            pixel_color = image.getpixel((i, j))
            new_color = find_nearest_color(pixel_color, colors)
            new_image.putpixel((i, j), new_color)

            # Thêm đường viền đen và lưới
            if i >= 0 and i % grid_size_x == 0:
                new_image.putpixel((i, j), (0, 0, 0))  # Vertical grid line
            if j >= 0 and j % grid_size_y == 0:
                new_image.putpixel((i, j), (0, 0, 0))  # Horizontal grid line

    return new_image

def convert_to_single_color_grid(image, colors, resolution_width, resolution_height):
    width, height = image.size
    new_image = Image.new('RGB', (width, height))

    grid_size_x = width // resolution_width
    grid_size_y = height // resolution_height

    for i in range(0, width, grid_size_x):
        for j in range(0, height, grid_size_y):
            # Lấy màu trung bình trong từng ô lưới
            grid_color = find_average_color(image, i, j, grid_size_x, grid_size_y)
            
            # Tìm màu gần nhất từ danh sách màu mục tiêu
            new_color = find_nearest_color(grid_color, colors)

            # Gán màu mới cho từng pixel trong ô lưới
            for x in range(i, min(i + grid_size_x, width)):
                for y in range(j, min(j + grid_size_y, height)):
                    new_image.putpixel((x, y), new_color)

            # Thêm đường viền đen và lưới
            for x in range(i, min(i + grid_size_x, width)):
                new_image.putpixel((x, j), (0, 0, 0))  # Vertical grid line
            for y in range(j, min(j + grid_size_y, height)):
                new_image.putpixel((i, y), (0, 0, 0))  # Horizontal grid line

    return new_image


def find_average_color(image, start_x, start_y, grid_size_x, grid_size_y):
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








# Use tkinter to open a file dialog and get the path to the image
root = tk.Tk()
root.withdraw()  # Hide the main window

file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", ".png;.jpg;*.jpeg")])

if not file_path:
    print("No file selected. Exiting.")
    exit()

# Load the image
image = Image.open(file_path)
image_size = image.size

# Define three target colors (RGB)
target_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Resolution of the grid (number of pixels per cell)
grid_resolution_width = int(52)
grid_resolution_height = int(30)

# # Convert the image to 3 colors and add black borders and grid lines
# result_image = convert_to_3_colors_with_grid(image, target_colors, grid_resolution_width, grid_resolution_height)

# # Save the resulting image
# result_image.save("output.png")

# Sử dụng hàm convert_to_single_color_grid thay vì convert_to_3_colors_with_grid
result_image = convert_to_single_color_grid(image, target_colors, grid_resolution_width, grid_resolution_height)
result_image.save("output_single_color_grid.png")