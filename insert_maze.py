from PIL import Image
from tkinter import filedialog
import tkinter as tk
import numpy as np
from settings import *
# import cv2


class MazeConverter:
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
    
    def process_maze(self):
        file_path = self.open_image_dialog()
        img = Image.open(file_path)
        target_size=(104, 60)
        img_resized = img.resize(target_size, resample=Image.BILINEAR)

        # Convert the resized image to a NumPy array
        matrix = np.array(img_resized)

        # Convert to binary matrix (0 for white, 1 for black)
        binary_matrix = (matrix[:,:,0] > 128).astype(int)
        print(len(binary_matrix), len(binary_matrix[0]))

        return binary_matrix