import os
import shutil

source_folder = input("Enter the folder path: ")

destination_folder = os.path.join(source_folder, "jpg_files")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for file in os.listdir(source_folder):

    if file.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")

print("All JPG files have been moved successfully!")
