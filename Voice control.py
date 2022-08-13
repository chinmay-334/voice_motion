import turtle
turtle.bgcolor("black")
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
query=""
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
print(voice[0].id)
def speak(audio):
                engine.say(audio)
                engine.runAndWait()
def takecommand(query):
                r=sr.Recognizer()
                with sr.Microphone() as source:
                                print("Listening...")
                                r.pause_threshold=1
                                audio=r.listen(source)
                                try:
                                                query=r.recognize_google(audio)
                                                print(query)
                                                if query in "Frontfront":
                                                                turtle.fd(50)
                                                elif query in "Backback":
                                                                turtle.bk(50)
                                                elif query in "Rightright":
                                                                turtle.rt(90)
                                                                turtle.fd(50)
                                                elif query in "Leftleft":
                                                                turtle.lt(90)
                                                                turtle.fd(50)
                                                
                                                
                                except Exception as a:
                                                print("Try again")
                return query

speak("Hello Lets play")
turtle.shape("circle")
turtle.setpos(x=-100,y=-100)
turtle.color("red")
turtle.clear()
turtle.lt(90)
while takecommand(query)!="stop":
                turtle.fd(50)
                takecommand(query)
