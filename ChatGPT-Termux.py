# ChatGPT-Python for Termux
import openai
from gtts import gTTS
import os

# OPENAI API KEY
openai.api_key = ""
# List with common departures to end the while loop
despedida = ["Adios", "adios", "bye", "Bye", "Hasta luego", "hasta luego"]

while True:
    # User input and check if the input matches the list of goodbyes
    usuario = str(input("tu: "))
    if usuario in despedida:
        break
    else:
        prompt = (f"Tu eres ChatGPT y responde mi siguiente mensaje: {usuario}")

    # Getting responses using the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024
    )

    respuesta = response["choices"][0]["text"]
    #print("ChatGPT:", response["choices"][0]["text"])
    # Converting text to audio
    texto = str(respuesta)
    tts = gTTS(texto, lang="es")
    tts.save("audio.mp3")
    # Displaying the answer on the screen
    print("ChatGPT: ", respuesta)
    # Playing the audio
    os.system("pulseaudio -D")
    os.system("play audio.mp3")
    os.system("pulseaudio -k")
