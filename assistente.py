import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import os

# Inicializar o motor de voz
engine = pyttsx3.init()
engine.setProperty("rate", 160)  # Velocidade da fala
engine.setProperty("volume", 1.0)  # Volume da fala

# Função para falar
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para ouvir comandos de voz
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Desculpe, não entendi.")
        return ""
    except sr.RequestError:
        speak("Erro ao conectar ao serviço de reconhecimento de voz.")
        return ""

# Função para processar comandos
def process_command(command):
    if "abrir google" in command:
        speak("Abrindo o Google...")
        webbrowser.open("https://www.google.com")

    elif "pesquisar por" in command:
        search_query = command.replace("pesquisar por", "").strip()
        speak(f"Buscando informações sobre {search_query}...")
        try:
            summary = wikipedia.summary(search_query, sentences=2, lang="pt")
            speak(summary)
        except wikipedia.exceptions.DisambiguationError:
            speak("Há muitas opções para essa busca, tente ser mais específico.")
        except wikipedia.exceptions.PageError:
            speak("Não encontrei informações sobre isso.")

    elif "abrir youtube" in command:
        speak("Abrindo o YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "tocar música" in command:
        speak("Tocando sua música favorita.")
        os.system("start wmplayer")  # Abre o Windows Media Player

    elif "sair" in command or "desligar" in command:
        speak("Até mais!")
        exit()

    else:
        speak("Desculpe, não reconheço esse comando.")

# Loop principal
speak("Olá! Eu sou sua assistente pessoal. Como posso ajudar?")
while True:
    user_command = listen()
    if user_command:
        process_command(user_command)
