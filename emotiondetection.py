import cv2
from deepface import DeepFace
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading

# Function to perform face and emotion detection
def detect_attributes(frame):
    img = frame.copy()
    
    # Detect faces in the frame
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        face_img = img[y:y+h, x:x+w]
        
        # Use DeepFace to analyze emotion
        analysis = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
        
        emotion = analysis[0]['dominant_emotion']
        
        # Draw rectangle around the face and put text
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, f'Emotion: {emotion}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    return img

def video_loop():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect attributes in the frame
        frame = detect_attributes(frame)
        
        # Convert the frame to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        
        # Update the GUI in a thread-safe manner
        panel_lock.acquire()
        try:
            panel.config(image=frame)
            panel.image = frame
        finally:
            panel_lock.release()
        
    cap.release()

# Function to start the video loop in a separate thread
def start_video():
    threading.Thread(target=video_loop, daemon=True).start()

# Create the main window
root = tk.Tk()
root.title("Continuous Emotion Detection")

# Create a panel to display the video
panel = tk.Label(root)
panel.pack()

# Create a lock for thread-safe GUI updates
panel_lock = threading.Lock()

# Create a button to start the video
btn = tk.Button(root, text="Start Video", command=start_video)
btn.pack()

# Run the GUI loop
root.mainloop()
