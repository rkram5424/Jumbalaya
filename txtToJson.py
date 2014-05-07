import json

filelist = ['Entertainment', 'Geography', 'History', 'ScienceNature', 'Misc']

for file in filelist:
    with open(file+'.txt', 'r') as f:
        jsonObj = {}
        lines = f.readlines()
        for line in lines:
            arr = line.split('|')
            # We'll add the newlines back in during dumps
            arr[0] = arr[0].strip('\n')
            arr[1] = arr[1].strip('\n')
            jsonObj[arr[0]] = arr[1]
        _json = json.dumps(jsonObj, encoding="latin1", separators=(',', ': '), indent=4)
        jsonFile = open(file+'.json', 'w')
        jsonFile.write(_json)
        jsonFile.close()
