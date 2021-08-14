import json

def RFID(uid, DBpath):
    with open(DBpath, "r") as f:
        data = json.load(f)
    for name in data:
        if uid == data[name]:
            return name
    return 'None'


