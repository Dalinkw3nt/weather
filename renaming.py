import os
import shutil

def organize_files_by_extension(directory):
    # Check if the provided directory exists
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return

    # Traverse through the files in the directory
    for filename in os.listdir(directory):
        # Get the full file path
        file_path = os.path.join(directory, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(filename)
            extension = extension[1:]  # Remove the leading dot

            # Create a new directory for the extension if it doesn't exist
            if extension:  # Only create a folder if there's an extension
                extension_folder = os.path.join(directory, extension)
                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)

                # Move the file to the corresponding folder
                shutil.move(file_path, os.path.join(extension_folder, filename))
                print(f'Moved: {filename} to {extension_folder}')

if __name__ == "__main__":
    user_directory = input("Enter the directory path to organize: ")
    organize_files_by_extension(user_directory)
