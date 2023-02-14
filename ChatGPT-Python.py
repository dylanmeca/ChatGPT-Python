import openai
import gradio as gr

openai.api_key = None

# Obteniendo respuestas usando la API de OpenAI
def respuesta_chatgpt(api_key, mensaje):
  # OPENAI API KEY
  openai.api_key = api_key
  prompt = (f"{mensaje}")
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1024
  )
  # Mostrando la respuesta en pantalla
  respuesta = response["choices"][0]["text"]
  return respuesta
      
# Entrada del usuario
chatbot = gr.Interface(
    fn=respuesta_chatgpt, 
    inputs=["text", "text"],
    outputs="text",
)
chatbot.launch()   
