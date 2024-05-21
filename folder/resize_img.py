from PIL import Image


def resize_image(input_path, output_path, new_width, new_height):
    # Open an image file
    with Image.open(input_path) as img:
        # Print original image size
        print(f"Original size: {img.size}")

        # Resize image
        resized_img = img.resize((new_width, new_height))

        # Print new image size
        print(f"Resized size: {resized_img.size}")

        # Save resized image
        resized_img.save(output_path)


# Example usage
input_image_path = "D:\\SV\\HK6\\Algorithms and Analysis\\Maze\\441431737_1423994791583395_2191369315377873641_n.png"
output_image_path = "D:\\SV\\HK6\\Algorithms and Analysis\\Maze\\resized_image.png"
new_width = 1536
new_height = 168

resize_image(input_image_path, output_image_path, new_width, new_height)
