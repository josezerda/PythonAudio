import speech_recognition as sr
r = sr.Recognizer()

#Leemos desde el microfono
with sr.Microphone() as recurso:
    print("Dime algo...")
