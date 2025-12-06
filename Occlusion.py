from PIL import Image, ImageOps
import numpy as np
import random
import os

#change to the number of cells in the 4 by 4 grid to be selected to be blackened for each annotation
num_regions = 3

#function for occluding a section of an image
def blackout_section(input_image_path, output_image_path, section_coords):
    try:
        image = Image.open(input_image_path)
      
        image = ImageOps.exif_transpose(image)

        image_array = np.array(image)

        x1, y1, x2, y2 = section_coords

        if not (0 <= x1 < x2 <= image.width and 0 <= y1 < y2 <= image.height):
            raise ValueError("Coordinates are out of bounds or invalid.")

        image_array[y1:y2, x1:x2] = [0, 0, 0]

        modified_image = Image.fromarray(image_array)

        modified_image.save(output_image_path)

    except FileNotFoundError:
        print(f"Error: The file at '{input_image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#replace with actual paths - the image files and .txt label files must have the same file names
path_to_images = r""
path_to_image_labels = r""

for image_file in os.listdir(rf"{path_to_images}"):
    changed = ""
    #change the image file name to match the label file name
    for i in range(len(image_file)):
        if i <= len(image_file) - 4:
            changed += image_file[i]
        else:
            changed += "txt"
            break
    image = Image.open(rf"{path_to_images}\{image_file}")
    #selecting the random sections of the image in a 4 by 4 grid
    locations = [(random.randint(1, 4), random.randint(1, 4))]
    while True:
        locations.append((random.randint(1, 4), random.randint(1, 4)))
        locations = list(set(locations))
        if len(locations) == num_regions:
            break
    #opens the label file to access annotations
    with open(rf"{path_to_image_labels}\{changed}", "r") as file:
        for line in file:
            values = line.split()
            values_for_blackout = []
            for i in range(len(values)):
                if i == 0:
                    continue
                else:
                    values_for_blackout.append(values[i])
            
            #choosing the region which to blackout
            values_for_blackout[0] = int(float(values_for_blackout[0]) * image.size[0])
            values_for_blackout[1] = int(float(values_for_blackout[1]) * image.size[1])
            values_for_blackout[2] = int(float(values_for_blackout[2]) * image.size[0])
            values_for_blackout[3] = int(float(values_for_blackout[3]) * image.size[1])
            for j in range(len(locations)):
                #making the choices random according to the previous selection
                region = [round(values_for_blackout[0]-values_for_blackout[2]/2), round(values_for_blackout[1]+values_for_blackout[3]/4), round(values_for_blackout[0]-values_for_blackout[2]/4), round(values_for_blackout[1]+values_for_blackout[3]/2)]
                region[0] += int((locations[j][0] - 1) * values_for_blackout[2] / 4)
                region[2] += int((locations[j][0] - 1) * values_for_blackout[2] / 4)
                region[1] -= int((locations[j][1] - 1) * values_for_blackout[3] / 4)
                region[3] -= int((locations[j][1] - 1) * values_for_blackout[3] / 4)
                #blacking out and saving the image
                blackout_section(rf"{path_to_images}\{image_file}", rf"{path_to_images}\{image_file}", region)
