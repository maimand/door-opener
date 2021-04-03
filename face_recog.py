import cv2
import face_recognition
import json

def addFace(path, name, DBpath):
  image = face_recognition.load_image_file(path)
  encoding = face_recognition.face_encodings(image)
  if not encoding:
    return 0
  with open(DBpath, "rb") as f:
    data = json.load(f)
    if data.get(name):
      data[name].append(list(encoding[0]))
    else:
      data[name] = [list(encoding[0])]
  with open(DBpath, "w") as f:
      json.dump(data, f)
  return len(data[name])

def deleteFace(name, DBpath):
  with open(DBpath, "rb") as f:
    data = json.load(f)
  if not data.get(name):
    return 0
  number = len(data[name])
  del data[name]
  with open(DBpath, "w") as f:
    json.dump(data, f)
  return number
  
def findFace(path, DBpath):
  unknown_image = face_recognition.load_image_file(path)
  unknown_encodings = face_recognition.face_encodings(unknown_image)
  if not unknown_encodings:
    return []
  with open(DBpath, "rb") as f:
    data = json.load(f)
  faces = []
  for encoding in unknown_encodings:
    tmp = ""
    for face in data:
      results = face_recognition.compare_faces(data[face], encoding)
      if True in results:
        tmp = face
    if tmp:
      faces.append(tmp)
  return faces

