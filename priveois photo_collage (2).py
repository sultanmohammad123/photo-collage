from PIL import Image
import os

folder_path = input("Enter path of your folder : ")
# folder_path = "C:/Users/User/Desktop/images"

#image file from folder
image_file = os.listdir(folder_path)

# Create matrix and determine image sizes
matrix = []
size = []

# count of images
n = int(input("Enter count of images:"))

for i in range(n):
    image_path = os.path.join(folder_path, image_file[i])
    img = Image.open(image_path)
    matrix.append(img)
    size.append(img.size)
    print(f"matrix {i+1} size: {img.size}")

max_width = 0
max_height = 0

position_mapping = []

# takes image position
for i in range(n):
    if i < len(matrix):
        x = int(input(f"Enter the x_coordinat for {i+1} image : "))
        y = int(input(f"Enter the y_coordinat for {i+1} image : "))
        position_mapping.append((x, y))
        max_width = max(max_width, x + size[i][0])
        max_height = max(max_height, y + size[i][1])

# Calculate the maximum width and height based on given image coordinates
collage_width = max_width
collage_height = max_height

def paste_image(collage, matrix, position):
    collage.paste(matrix, position)

# Create a blank canvas for collage
collage = Image.new('RGB', (collage_width, collage_height), color='white')

# paste images in specified positions
for i, position in enumerate(position_mapping):
    if i < len(matrix):
        paste_image(collage, matrix[i], position)

collage.show()
