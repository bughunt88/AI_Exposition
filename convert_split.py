import json

f = open('C:/data/task03_train/labels.json')

training_data = json.load(f)

def get_img_shape(path):
    img = cv2.imread(path)
    try:
        return img.shape
    except AttributeError:
        print('error! ', path)
        return (None, None, None)
def convert_labels(path, x1, y1, x2, y2):
   
    def sorting(l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin
    size = get_img_shape(path)
    xmax, xmin = sorting(x1, x2)
    ymax, ymin = sorting(y1, y2)
    dw = 1./size[1]
    dh = 1./size[0]
    x = (xmin + xmax)/2.0
    y = (ymin + ymax)/2.0
    w = xmax - xmin
    h = ymax - ymin
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

# {"annotations": [{"image_id": 0, "file_name": "image_29829216469167.jpg", 
# "objects": [{"object_id": 0, "class": "face", "position": [225, 718, 545, 1090]}, 
# {"object_id": 1, "class": "eye_opened", "position": [295, 778, 366, 813]}, 
# {"object_id": 2, "class": "eye_opened", "position": [436, 771, 502, 805]}, 
# {"object_id": 3, "class": "mouth_opened", "position": [368, 918, 474, 1009]}]}

import cv2
check_set = set()
for i in range(len(training_data['annotations'])):
    
    image_id = str(training_data['annotations'][i]['file_name'])

    file_name = "C:/data/task03_train/images2/"+str(training_data['annotations'][i]['file_name'])
    
    objects = str(training_data['annotations'][i]['objects'])

    content = ""
    for a in range(len(training_data['annotations'][i]['objects'])):

        bbox = training_data['annotations'][i]['objects'][a]['position']
        category_id = training_data['annotations'][i]['objects'][a]['class']
        image_path = file_name
        kitti_bbox = [bbox[0], bbox[1], bbox[2] + bbox[0], bbox[3] + bbox[1]]

        yolo_bbox = convert_labels(image_path, kitti_bbox[0], kitti_bbox[1], kitti_bbox[2], kitti_bbox[3])

        if category_id == "face":
            category_id = 0
        elif category_id == "eye_opened":
            category_id = 1
        elif category_id == "eye_closed":
            category_id = 2
        elif category_id == "mouth_opened":
            category_id = 3
        elif category_id == "mouth_closed":
            category_id = 4    
        elif category_id == "phone":
            category_id = 5    
        elif category_id == "cigar":
            category_id = 6    

        content += str(category_id) + " " + str(yolo_bbox[0]) + " " + str(yolo_bbox[1]) +   " " + str(yolo_bbox[2]) + " " + str(yolo_bbox[3])
        content += "\n"

    print(content)

    image_id = image_id.replace(".jpg","")
    filename = image_id + '.txt'
        
    file = open('C:/data/task03_train/test/'+filename, 'a')
    file.write(content)
    file.close()