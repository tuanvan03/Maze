import os

def rename_images_in_subfolders(parent_folder):
    for subdir, _, files in os.walk(parent_folder):
        folder_name = os.path.basename(subdir)
        image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
        
        for i, file in enumerate(image_files):
            old_file_path = os.path.join(subdir, file)
            new_file_name = f"maze_{folder_name}_{i + 1:02d}{os.path.splitext(file)[1]}"
            new_file_path = os.path.join(subdir, new_file_name)
            
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} to {new_file_path}")

if __name__ == "__main__":
    parent_folder = "C:\\Daihoc\\Ky2nam3\\TK_DGTT\\Baitaplon\\Maze\\SourceImg\\Maze\\Type"
    rename_images_in_subfolders(parent_folder)
