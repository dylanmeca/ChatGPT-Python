import openai
from gtts import gTTS
import os

# OPENAI API KEY
openai.api_key = ""
# Lista con despedidas comunes para finalizar el ciclo while
despedida = ["Adios", "adios", "bye", "Bye", "Hasta luego", "hasta luego"]

while True:
    # Entrada del usuario y verificacion si la entrada coincide con la lista de despedidas
    usuario = str(input("tu: "))
    if usuario in despedida:
        break
    else:
        prompt = (f"{usuario}")

    # Obteniendo respuestas usando la API de OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024
    )

    respuesta = response["choices"][0]["text"]
    #print("IrisBot:", response["choices"][0]["text"])
    # Convirtiendo texto a audio
    texto = str(respuesta)
    tts = gTTS(texto, lang="es")
    tts.save("audio.mp3")
    # Mostrando la respuesta en pantalla
    print("ChatGPT: ", respuesta)
    # Reproduciendo el audio
    os.system("mpg321 audio.mp3")
