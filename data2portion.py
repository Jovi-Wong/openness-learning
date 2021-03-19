"""First part is to import necessary modules"""
import os
from PIL import Image
"""Second part is to check color portion in samples and then write into text files """
text = open("portion.txt","a")
#initialize obj_count and path
dataset_path = "./dataset"
all_files = os.listdir(dataset_path)
color_obj = {(0,0,0):"window", (200,0,0):"wall", (0,0,255):"celling", (125,38,205):"floor",(0,127,0):"furniture"}
#color_obj.keys()
#transeval points in the figure
#def determine_obj(point):

for file in all_files:
    window = 0
    wall = 0
    celling = 0
    floor = 0
    furniture = 0
    name = file.split('.')
    image_dir = dataset_path + "/" + file
    fig = Image.open(image_dir)
    height_width = fig.size
    height = height_width[0]
    width = height_width[1]
    r, g, b = fig.split()
    points = zip(r,g,b)
    
    for point in points:
        obj = color_obj[point]
        count_cmd = obj + " = " + obj + " +1"
        eval(count_cmd)
    
    total_points = height * width
    
    new_line = name + " " + str(window/total_points) + " " + str(wall/total_points) + " " + str(celling/total_points) + " " + str(floor/total_points) + "\n"
    text.write(new_line)
    
text.close()
