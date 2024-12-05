from gtts import gTTS
import pygame

def speak(text):
    tts = gTTS(text, lang='en', tld='com.au')
    tts.save('byebye.mp3')
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('byebye.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
while True:
    command = input("enter text to speak it out : ")
    if command == "exit":
        break
    else:
        speak(command)