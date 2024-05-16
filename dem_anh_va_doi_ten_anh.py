import os

def count_images(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Initialize a counter for images
    image_count = 0
    
    # Define image file extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    
    # Loop through each file in the directory
    for file in files:
        # Check if the file has an image extension
        if any(file.lower().endswith(ext) for ext in image_extensions):
            # Increment the image count
            image_count += 1
    
    return image_count

def rename_images(directory):
    # Define image file extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    
    # Get the list of image files in the directory
    files = os.listdir(directory)
    
    # Define the base name pattern for renaming
    base_name = "small_maze_"
    
    # Start index for numbering
    index = 1
    
    # Loop through each file in the directory
    for file in files:
        # Check if the file has an image extension
        if any(file.lower().endswith(ext) for ext in image_extensions):
            # Construct the new file name
            new_name = f"{base_name}{index}{os.path.splitext(file)[1]}"
            
            # Rename the file
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            
            # Increment the index
            index += 1

# Example usage:
directory_path = 'C:\\Daihoc\\Ky2nam3\\TK_DGTT\\Baitaplon\\Maze\\SourceImg\\Maze\\New\\Small_Maze'  # Update this with the path to your directory

# Count the number of images
num_images = count_images(directory_path)
print("Number of images:", num_images)

# Rename images
rename_images(directory_path)
print("Images renamed successfully.")
