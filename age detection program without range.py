import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

# Simulated function to "detect" age (returns a random age for simplicity)
def detect_age(face_img):
    return random.randint(10, 80)

# Function to update the video feed
def update_video_feed():
    ret, frame = cap.read()
    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Simulate age detection
            age = detect_age(frame[y:y+h, x:x+w])
            
            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Display the age
            cv2.putText(frame, f'Age: {age}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Convert the frame to an image
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        img_tk = ImageTk.PhotoImage(image=img)
        
        # Update the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.img_tk = img_tk

    # Repeat after a delay
    root.after(10, update_video_feed)

# Initialize the main window
root = tk.Tk()
root.title("Live Age Detection")

# Create a canvas to display the video feed
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Add a button to start the age detection
start_button = ttk.Button(root, text="Start Age Detection", command=update_video_feed)
start_button.pack()

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start the Tkinter event loop
root.mainloop()

# Release the video capture when the program ends
cap.release()
cv2.destroyAllWindows()
