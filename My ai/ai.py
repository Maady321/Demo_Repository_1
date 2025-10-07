from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import threading
import pyttsx3
import speech_recognition as sr
from openai import OpenAI

# OpenAI setup
client = OpenAI(api_key="YOUR_API_KEY_HERE")

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""

def ai_response(query):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Kivy UI
class VoiceAIApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Press 'Talk' and speak to AI", size_hint=(1, 0.8))
        self.button = Button(text="Talk", size_hint=(1, 0.2))
        self.button.bind(on_press=self.start_listening)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def start_listening(self, instance):
        threading.Thread(target=self.listen_and_respond).start()

    def listen_and_respond(self):
        self.label.text = "🎤 Listening..."
        command = listen()
        if command:
            self.label.text = f"You said: {command}"
            response = ai_response(command)
            self.label.text = f"🤖 AI: {response}"
            speak(response)
        else:
            self.label.text = "I couldn't understand. Try again."

if __name__ == "__main__":
    VoiceAIApp().run()
