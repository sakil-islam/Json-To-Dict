import json
import os

#path to short_template.json file

CWD = os.getcwd()
JSON_SHORT_TEMPLATE_FILE_PATH = '%s/%s' % (CWD, 'short_template.json')

#Dictionary holding json values
CONFIG_PROPERTIES = {}

#Open json , parse value andstore them in dictionary

try:
    with open(JSON_SHORT_TEMPLATE_FILE_PATH) as data_file:
        CONFIG_PROPERTIES = json.load(data_file)
except IOError as eo:
    print (eo)
    print ("IOError: unable to open json file.")
    exit(1)

json_file = CONFIG_PROPERTIES

print(json_file)

new_json = json.dumps(json_file)
with open('create_json.json', 'w') as file:
    file.write(new_json)
    file.close()
