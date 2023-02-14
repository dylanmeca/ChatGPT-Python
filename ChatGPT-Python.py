import openai
import gradio as gr

# Getting responses using the OpenAI API
def respuesta_chatgpt(api_key, mensaje):
  # OPENAI API KEY
  openai.api_key = api_key
  prompt = (f"{mensaje}")
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1024
  )
  # Displaying the answer on the screen
  respuesta = response["choices"][0]["text"]
  return respuesta
      
# User input
chatbot = gr.Interface(
    fn=respuesta_chatgpt, 
    inputs=["text", "text"],
    outputs="text",
)
chatbot.launch()   
