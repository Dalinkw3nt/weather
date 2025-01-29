import os

def create_folders_from_extensions(parent_directory):
    # Set to store unique file extensions
    extensions = set()
    
    # Walk through the parent directory
    for root, _, files in os.walk(parent_directory):
        for file in files:
            # Get the file extension
            _, ext = os.path.splitext(file)
            if ext:  # Check if the extension is not empty
                extensions.add(ext[1:])  # Add without the dot

    # Create folders for each unique extension
    for ext in extensions:
        path = os.path.join(parent_directory, ext)
        try:
            os.makedirs(path, exist_ok=True)  # Create folder if it doesn't exist
            print(f"Created folder: {path}")
        except Exception as e:
            print(f"Error creating folder {path}: {e}")

# Prompt user for the parent directory
parent_directory = input("Enter the path to the parent directory: ")

# Call the function with user input
create_folders_from_extensions(parent_directory)
