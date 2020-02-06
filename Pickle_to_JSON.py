import os
import json
import pickle

try:
    import jsonpickle
except:
    os.system("pip install jsonpickle")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
    if file[-4:] == ".pkl":
        print("Dumping " + file + " as JSON.")
        picklefile = open(file, 'rb')
        jsonfile = open(file[:-4] + ".json", 'w')
        pickleload = pickle.load(picklefile)
        picklefile.close()
        jsondata = json.dumps(pickleload)
        jsonfile.write(jsondata)
        jsonfile.close()