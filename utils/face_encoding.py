import face_recognition
import numpy as np 
from PIL import Image, ImageDraw, ImageFont
from IPython.display import display
import os
import random

person_image = face_recognition.load_image_file("modi.jpg")
persons_face_encoding = face_recognition.face_encodings(person_image)[0]

person2_image = face_recognition.load_image_file("amit-shah.jpg")
person2_face_encoding= face_recognition.face_encodings(person2_image)[0]

known_face_encodings = [
    persons_face_encoding,
    person2_face_encoding
]

print("knowwn ", known_face_encodings)

known_face_names = [
    "Modi ji",
    "Amit Shah"
]

print('Learned encoding for', len(known_face_encodings), 'images.')



# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("two_person.jpg")

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]
        if not os.path.exists(name):
            os.makedirs(name)
        pil_image.save(os.path.join(name, f'{random.random()}.jpg'))



    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
    # Draw a label with a name below the face
    print(draw.textlength(name))
    text_height = 0  # Replace 20 with any relevant value
    _, _, text_width, text_height = draw.textbbox((left, bottom - text_height - 10), name)
    draw.rectangle(((left, bottom - text_height), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw
  
display(pil_image)

