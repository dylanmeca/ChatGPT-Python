import openai
import gradio as gr

class chatgpt: 

      def __init__(self):
          self.model_id = "gpt-3.5-turbo"
          self.conversation = []

      # Getting responses using the OpenAI API
      def answer_chatgpt(self, api_key, message, history):
          self.history = history or []
          prompt = f"{message}"
          self.conversation.append({"role": "user", "content": f"{prompt}"})
          # OPENAI API KEY
          openai.api_key = api_key
          response = openai.ChatCompletion.create(
              model=self.model_id,
              messages=self.conversation
          )
          # Displaying the answer on the screen
          answer = response["choices"][0]["message"]["content"]
          self.history.append((message, answer))
          self.conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
          return self.history, self.history

      def Clean(self):
          self.history.clear()
          self.conversation.clear()
      
# User input
block = gr.Blocks()
chatgpt = chatgpt()

with block:
    gr.Markdown("""<h1><center>🤖 ChatGPT-Assistant 🐍</center></h1>
                   <p><center>ChatGPT-Assistant is a chatbot that uses the gpt-3.5-turbo model</center></p>
    """)
    api_key = gr.Textbox(type="password", label="Enter your OpenAI API key here")
    chatbot = gr.Chatbot()
    message = gr.Textbox(label="Message")
    state = gr.State()
    submit = gr.Button("Send")
    submit.click(chatgpt.answer_chatgpt, inputs=[api_key, message, state], outputs=[chatbot, state])
    clean = gr.Button("Clean")
    clean.click(chatgpt.Clean)
    gr.Examples(
        examples=["Write a poem about artificial intelligence",
                  "What could the future be like?",
                  "If x+1=20, what is the value of x?",
                  "Write a story that gives a message",
                  "What programming language is the most used in the industry?",
                  "How can I be more productive?",
                  "Create me a training schedule to train from home",
                  "Sums up everything we've talked about"],
        inputs=message
    )

block.launch(debug=True) 
