import openai
import gradio as gr

# Getting responses using the OpenAI API
def answer_chatgpt(api_key, message, history):
  history = history or []
  lista = list(sum(history, ()))
  lista.append(message)
  # OPENAI API KEY
  openai.api_key = api_key
  prompt = (f"You are GPT-3, you are in a web interface and reply to my following message: {message}")
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1024
  )
  # Displaying the answer on the screen
  answer = response["choices"][0]["text"]
  history.append((message, answer))
  return history, history
      
# User input
block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>🤖 ChatGPT-Python 🐍</center></h1>
                   <p><center>ChatGPT-Python is a software that allows you to talk to GPT-3 with a web interface using the openai api</center></p>
    """)
    api_key = gr.Textbox(placeholder="api_key")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="message")
    state = gr.State()
    submit = gr.Button("Send")
    submit.click(answer_chatgpt, inputs=[api_key, message, state], outputs=[chatbot, state])

block.launch(debug=True)
