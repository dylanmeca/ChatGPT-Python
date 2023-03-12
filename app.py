import openai
import gradio as gr

model_id = "gpt-3.5-turbo"
conversation = []

# Getting responses using the OpenAI API
def answer_chatgpt(api_key, message, history):
  history = history or []
  prompt = f"{message}"
  conversation.append({"role": "user", "content": f"{prompt}"})
  # OPENAI API KEY
  openai.api_key = api_key
  response = openai.ChatCompletion.create(
  model=model_id,
  messages=conversation
  )
  # Displaying the answer on the screen
  answer = response["choices"][0]["message"]["content"]
  history.append((message, answer))
  conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
  return history, history


def Clean():
    global history
    global conversation
    history = []
    conversation = []
      
# User input
block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>🤖 ChatGPT-Assistant 🐍</center></h1>
                   <p><center>ChatGPT-Assistant is a chatbot that uses the gpt-3.5-turbo model</center></p>
    """)
    api_key = gr.Textbox(type="password", label="Enter your OpenAI API key here")
    chatbot = gr.Chatbot()
    message = gr.Textbox(label="Message")
    state = gr.State()
    submit = gr.Button("Send")
    submit.click(answer_chatgpt, inputs=[api_key, message, state], outputs=[chatbot, state])
    clean = gr.Button("Clean")
    clean.click(Clean)

block.launch(debug=True) 
