import json
import pandas as pd
import sys

data = open('C:/data/task03_train/labels.json', 'r', encoding='utf-8-sig')
json_data = json.load(data)

for a in json_data['annotations']:
    pp = a['file_name'][:-4]
    sys.stdout = open('C:/data/task03_train/labels/'+str(pp)+'.txt','w')
    for b in range(len(a['objects'])):
        if a['objects'][b]['class'] == "face":
            print(0, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "eye_opened":
            print(1, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "eye_closed":
            print(2, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "mouth_opened":
            print(3, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "mouth_closede":
            print(4, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "phone":
            print(5, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "cigar":
            print(6, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)

for a in json_data['annotations']:
    pp = a['file_name'][:-4]
    sys.stdout = open('C:/data/task03_train/labels/'+str(pp)+'.txt','w')
    for b in range(len(a['objects'])):
        if a['objects'][b]['class'] == "face":
            print(0, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "eye_opened":
            print(1, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "eye_closed":
            print(2, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "mouth_opened":
            print(3, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "mouth_closede":
            print(4, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "phone":
            print(5, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)
        elif a['objects'][b]['class'] == "cigar":
            print(6, a['objects'][b]['position'][0]/800, a['objects'][b]['position'][1]/1280, a['objects'][b]['position'][2]/800, a['objects'][b]['position'][3]/1280)