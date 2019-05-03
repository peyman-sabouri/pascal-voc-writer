import os
# import matplotlib.pyplot as plt
import numpy as np
from pascal_voc_writer import Writer
import json
import cv2
#%% src path

src_json_path = '/home/peyman/mnt/data/DATA/ouster_data/create_dataset/PixelAnnotationTool/data/anns/'
img_folder = '/home/peyman/mnt/data/DATA/ouster_data/create_dataset/PixelAnnotationTool/data/images/'


j_file_list = os.listdir(src_json_path)
print (len(j_file_list))

# file_name = os.path.basename()
# print (os.path.splitext('asdfasdf/asdfasf.json'))
# print (os.path.splitext('asdfasdf/asdfasf.json'))


#%%  dst path 
dst_path_xml = '/home/peyman/mnt/data/DATA/ouster_data/create_dataset/PixelAnnotationTool/data/labels/'



for f in j_file_list:
    j_file = src_json_path + f
    print (j_file)
    filename = os.path.basename(j_file)
    path_to_xml = dst_path_xml +  (os.path.splitext(filename)[0])
    xml_file =  path_to_xml + '.xml'
    print (xml_file)
    with open(j_file, 'r') as f:
        data = json.load(f)


    cnts = data['shapes']
    # print (data['shapes'])
    pts =[]
    writer = Writer(data['imagePath'], data['imageWidth'], data['imageHeight'])
    for i in range(len(cnts)):

        # if (data['shapes'][i]['label']) == 'post'
        name = data['shapes'][i]['label']

        if (name=='other'):
            continue
        pts =  data['shapes'][i]['points']
        pts = np.array(pts, np.int32)

        x,y,w,h = cv2.boundingRect(pts)
        xmin, ymin, xmax, ymax = x, y, x+w, y+h
        name = data['shapes'][i]['label']
        path = img_folder + data['imagePath']
        writer.addObject(name, xmin, ymin, xmax, ymax)


    writer.save(xml_file)
    with open(j_file, 'r') as f:
        data = json.load(f)


    cnts = data['shapes']
    # print (data['shapes'])
    pts =[]
    writer = Writer(data['imagePath'], data['imageWidth'], data['imageHeight'])
    for i in range(len(cnts)):

        # if (data['shapes'][i]['label']) == 'post'
        name = data['shapes'][i]['label']

        if (name=='other'):
            continue
        pts =  data['shapes'][i]['points']
        pts = np.array(pts, np.int32)

        x,y,w,h = cv2.boundingRect(pts)
        xmin, ymin, xmax, ymax = x, y, x+w, y+h
        name = data['shapes'][i]['label']
        path = img_folder + data['imagePath']
        writer.addObject(name, xmin, ymin, xmax, ymax)


    writer.save(xml_file)
