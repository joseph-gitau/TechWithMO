import face_recognition
import cv2 
import os 
from google.colab.patches import cv2_imshow


KNOWN_FACES = 'known'
UNKNOWN_FACES = 'unknown'

TOLERANCE = 0.6

MODEL = 'cnn'  # default is 'hog' other one can be 'cnn' if CUDA accelerated deep-learning pretrained model is available

known_face = []
known_name = []

print("Loading tranning data ....")
# Each subfolder's name becomes our identity for the image
for name in os.listdir(KNOWN_FACES):

  # loading every image for every subfolder
  for imagename in os.listdir(f'{KNOWN_FACES}/{name}'):
    # Load image
    image = face_recognition.load_image_file(f'{KNOWN_FACES}/{name}/{imagename}')
    # Get 128-dimension face encoding
    # for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
    encoding = face_recognition.face_encodings(image , model=MODEL)[0]

    #store encodings and name
    known_face.append(encoding)
    known_name.append(name)
print("Loading completed")

#now looping over the folder of unknown faces

print("Loading Test data .....")

for imagename in os.listdir(UNKNOWN_FACES):
 
  print(f' Imagename {imagename}', end='')

  # Load image

  image = face_recognition.load_image_file(f'{UNKNOWN_FACES}/{imagename}')

  loaction = face_recognition.face_locations(image , model=MODEL)

  # Now we know the loctions of faces, we can pass them to face_encodings as second argument Without that it will search for faces once again slowing down whole process
  encoding = face_recognition.face_encodings(image,loaction)

  #Converting image from RGB to Grey scal image as we are going to use cv2 
  image = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)

  # now this time we assume that there might be more faces in an image so we can find multiple faces
  for face_encoding ,face_location in zip(encoding,loaction):
    # We use compare_faces and Returns array of True/False values 
    result = face_recognition.compare_faces(known_face ,face_encoding ,  TOLERANCE) 
    # Order is being preserver,So we check if any face was found 
    # then using that index of first matching known face we can name the face those are withing a tolerance
    if True in result :
      
      match_name = known_name[result.index(True)]
      
      print(f' {match_name} from {result}')
      # Each location contains positions in order: top, right, bottom, left
      top_left = (face_location[3] , face_location[0])   
      bottom_right = (face_location[1] , face_location[2])

      #Pick a RGB color code
      color = [0, 255 ,0]

      #create Frame around  face
      cv2.rectangle(image, top_left ,bottom_right , color , 3)
      #now creating some space(small ractangle ) bellow frame for the name
      top_left = (face_location[3], face_location[2])
      bottom_right = (face_location[1], face_location[2] + 22)

      cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
      #Writting the name using putText funtion
      cv2.putText(image, match_name, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200),3)
  #display image 
  cv2_imshow(image)
  
