import os
import shutil

# Get the directory path from the user
ddir = input("Enter the directory path: ")

# Validate the path
if not os.path.exists(ddir):
    print("Invalid path. Please provide a valid path.")
    exit()

# Create subdirectories if they don't exist
if not os.path.exists(os.path.join(ddir, "Images")):
    os.mkdir(os.path.join(ddir, "Images"))
if not os.path.exists(os.path.join(ddir, "Videos")):
    os.mkdir(os.path.join(ddir, "Videos"))
if not os.path.exists(os.path.join(ddir, "Music")):
    os.mkdir(os.path.join(ddir, "Music"))
if not os.path.exists(os.path.join(ddir, "Documents")):
    os.mkdir(os.path.join(ddir, "Documents"))
if not os.path.exists(os.path.join(ddir, "Code")):
    os.mkdir(os.path.join(ddir, "Code"))
if not os.path.exists(os.path.join(ddir, "Other")):
    os.mkdir(os.path.join(ddir, "Other"))

# Lists of file extensions for different categories
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
music_extensions = [".mp3", ".wav", ".aiff"]
video_extensions = [".mp4"]
doc_extension = [".txt", ".pdf", ".docx", ".doc"]
code_extensions = [".html", ".py", ".css", ".bat", ".js"]

# Iterate through the files in the directory
for file in os.listdir(ddir):
    # Skip processing if the item is a subdirectory
    if os.path.isdir(os.path.join(ddir, file)):
        continue

    # Skip processing of .DS_Store files
    if file == ".DS._store":
        continue

    # Get the file extension in lowercase
    extension = os.path.splitext(file)[1].lower()

    # Move the file to appropriate subdirectories based on the extension
    if extension in image_extensions:
        shutil.move(os.path.join(ddir, file), os.path.join(ddir, "Images"))
    elif extension in music_extensions:
        shutil.move(os.path.join(ddir, file), os.path.join(ddir, "Music"))
    elif extension in doc_extension:
        shutil.move(os.path.join(ddir, file), os.path.join(ddir, "Documents"))
    elif extension in video_extensions:
        shutil.move(os.path.join(ddir, file), os.path.join(ddir, "Videos"))
    elif extension in code_extensions:
        shutil.move(os.path.join(ddir, file), os.path.join(ddir, "Code"))
    else:
        shutil.move(os.path.join(ddir, file), os.path.join(ddir, "Other"))

print("Files successfully organized.")