import json
import pandas as pd


# use the built-in json module
with open('C:/data/task03_train/labels.json') as json_file:
    students0 = json.load(json_file)

# use the pandas module
with open('C:/data/task03_train/labels.json') as json_file:
    students1 = pd.read_json(json_file, orient='index')

print(students0)
print(students1)