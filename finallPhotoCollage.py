from PIL import Image, ImageOps
from tkinter import Tk, filedialog

# Open folder dialog to select the folder
Tk().withdraw()
folder_path = filedialog.askdirectory(title="Select Folder")

# Get the list of image files in the selected folder
image_files = filedialog.askopenfilenames(title="Select Images", initialdir=folder_path)

# two  matrices first for photo and second for photo size
matrix = []
size = []

# Iterate over selected image files
for image_path in image_files:
    img = Image.open(image_path)
    matrix.append(img)
    size.append(img.size)
    print(f"matrix {len(matrix)} size: {img.size}")

n = len(matrix)
max_x = 0
max_y = 0

position_mapping = []
border_sizes = []  # List to store border sizes for each image

# Take image positions and border sizes
for i in range(n):
    if i < len(matrix):
        x = None
        y = None
        # Get the x and y coordinates for the current image
        if i == 0:
            # For the first image, position it at the top-left corner
            x = 0
            y = 0
        else:
            # For subsequent images, automatically calculate the position based on the size of the previous image
            prev_x, prev_y = position_mapping[i-1]
            prev_width, prev_height = size[i-1]
            remaining_width = max_x - prev_x
            remaining_height = max_y - prev_y
            if remaining_width >= size[i][0]:
                # Enough space available horizontally, position the image to the right of the previous image
                 y = prev_y
                 x = prev_x + prev_width
            elif remaining_height >= size[i][1]:
                # Not enough space horizontally, but enough space vertically, position the image below the previous image
               y = prev_y + prev_height
               x = 0
            else:
                # Not enough space horizontally or vertically, start a new row at the bottom
                x = 0
                y = max_y

        position_mapping.append((x, y))
        max_x = max(max_x, x + size[i][0])
        max_y = max(max_y, y + size[i][1])

        # Prompt for border size
        border_size =10
        border_sizes.append(border_size)

# Calculate the maximum width and height based on given image coordinates
max_width = max_x
max_height = max_y

# Create a blank canvas for the collage
collage = Image.new('RGB', (max_width, max_height), color='white')

# Paste images in specified positions with borders
for i, position in enumerate(position_mapping):
    if i < len(matrix):
        img = matrix[i]
        border_size = border_sizes[i]  # Get the border size for the current image

        # Create a new image with a border
        bordered_image = ImageOps.expand(img, border=border_size, fill='blue')

        # Paste the bordered image onto the collage at the specified position
        collage.paste(bordered_image, position)

collage.show()
