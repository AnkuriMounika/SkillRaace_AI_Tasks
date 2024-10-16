!pip install opencv-python face_recognition pandas numpy
from google.colab import files

# Upload images to Colab
uploaded = files.upload()

import face_recognition
import pandas as pd
import os

# Initialize lists to hold images and names
images = []
names = []

# Load the images and their names
for filename in uploaded.keys():
    img = face_recognition.load_image_file(filename)
    images.append(img)
    names.append(os.path.splitext(filename)[0])  # Get name without extension

# Encode faces
encoded_faces = []
for img in images:
    face_encoding = face_recognition.face_encodings(img)
    if face_encoding:  # Check if encoding was found
        encoded_faces.append(face_encoding[0])  # Append the first encoding found

print(f'Loaded {len(encoded_faces)} face encodings.')
# Upload the video file for testing
video_uploaded = files.upload()
import cv2
import numpy as np
from datetime import datetime

# Save attendance records
attendance = pd.DataFrame(columns=["Name", "Timestamp"])  # Create a DataFrame for attendance

# Load the video file (replace 'your_video.mp4' with the uploaded video filename)
video_path = list(video_uploaded.keys())[0]  # Get the filename of the uploaded video
video_capture = cv2.VideoCapture(video_path)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break  # Break the loop if the video has ended

    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

    # Find all the faces and their encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face found in the frame
    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(encoded_faces, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(encoded_faces, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = names[best_match_index]

        # Mark attendance
        if name != "Unknown":
            attendance = attendance.append({"Name": name, "Timestamp": datetime.now()}, ignore_index=True)
            print(f"Attendance marked for {name} at {datetime.now()}")

        # Draw a rectangle around the face
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Save attendance to CSV file
attendance.to_csv('attendance.csv', index=False)

video_capture.release()
from google.colab import files

# Download the attendance file
files.download('attendance.csv')


