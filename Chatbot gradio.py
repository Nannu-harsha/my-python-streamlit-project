import gradio as gr

answers = {
    "hi": "Hello Bro 👋",
    "how are you": "I am good!",
    "what is your name": "I am a chatbot!",
    "bye": "Goodbye 😊"
}


def chatbot(user):
    return answers.get(user.lower(), "I don't know that.")


with gr.Blocks() as demo:
    inp = gr.Textbox(label="You")
    out = gr.Textbox(label="Bot")
    gr.Button("Send").click(chatbot, inputs=inp, outputs=out)

demo.launch()
