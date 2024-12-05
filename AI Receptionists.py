import tkinter as tk
import random
import datetime
import pyttsx3
import speech_recognition as sr

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Function to speak out the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle AI responses based on user input
def handle_response(user_input):
    user_input = user_input.lower()
    
    # Get the current time of day
    current_time = datetime.datetime.now().hour
    
    # Time-based greeting
    if current_time < 12:
        greeting = "Good morning!"
    elif 12 <= current_time < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    
    # Sample responses
    responses = {
        'hello': f"{greeting} How can I assist you today?",
        'how are you': "I'm doing well, thank you for asking!",
        'what is your name': "I am your AI receptionist, here to help you.",
        'bye': "Goodbye! Have a great day!",
        'help': "I can assist with scheduling, answering questions, and more."
    }
    
    # Check if input matches predefined responses
    for key in responses:
        if key in user_input:
            speak(responses[key])
            return responses[key]
    
    # Default response if no match found
    default_response = "I'm sorry, I didn't quite understand that. Can you please rephrase?"
    speak(default_response)
    return default_response

# Function to take speech input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            command_label.config(text=f"You said: {command}")
            handle_response(command)
        except sr.UnknownValueError:
            command_label.config(text="Sorry, I couldn't understand that.")
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            command_label.config(text="Sorry, there's an issue with the speech service.")
            speak("Sorry, there's an issue with the speech service.")

# Setting up the tkinter window (GUI)
root = tk.Tk()
root.title("AI Receptionist")
root.geometry("400x300")

# Add an input text box
text_input = tk.Entry(root, width=40)
text_input.pack(pady=20)

# Add a button to submit the input
def on_submit():
    user_input = text_input.get()
    response = handle_response(user_input)
    response_label.config(text=response)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Add a label to display the AI's response
response_label = tk.Label(root, text="", width=40, height=4, bg="lightgray")
response_label.pack(pady=20)

# Add a label to show speech recognition result
command_label = tk.Label(root, text="", width=40, height=4, bg="lightyellow")
command_label.pack(pady=20)

# Add a button to listen for speech input
listen_button = tk.Button(root, text="Listen", command=listen)
listen_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
